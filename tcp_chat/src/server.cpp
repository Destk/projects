#include "../include/server.h"

Server::Server() {
    // Обнуляем структуру addr
    memset(&addr, 0, sizeof(addr));
    
    // 1) Создаем сокет
    server_sock = socket(AF_INET, SOCK_STREAM, 0);
    if (server_sock < 0) {
        std::cerr << "Ошибка создания сокета\n";
        exit(1);
    }
    
    // 2) Устанавливаем параметры
    addr.sin_family = AF_INET;
    addr.sin_port = htons(5252);
    addr.sin_addr.s_addr = INADDR_ANY;
    
    // Опция для переиспользования порта
    int opt = 1;
    setsockopt(server_sock, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
    
    // 3) Связываем сокет
    int b = bind(server_sock, (struct sockaddr*)&addr, sizeof(addr));
    if (b < 0) {
        std::cerr << "Ошибка! Соединение не установлено\n";
        close(server_sock);
        exit(1);
    } else {
        // 4) Переводим в режим ожидания
        listen(server_sock, 5);
    }
}

void Server::handler(int client_sock) {
    if (client_sock < 0) {
        std::lock_guard<std::mutex> lock(mtx);
        std::cerr << "Ошибка установки соединения!\n";
        return;
    }
    
    {
        std::lock_guard<std::mutex> lock(mtx);
        std::cout << "Клиент подключился" << std::endl;
    }
    
    {
        std::lock_guard<std::mutex> lock(clientMutex);
        clients.push_back(client_sock);
    }
    
    // Получение имени
    {
        std::lock_guard<std::mutex> lock(namesMutex);
        char buf[256] = {0};  // Инициализируем нулями
        int byte_name = recv(client_sock, buf, 255, 0);
        if (byte_name > 0) {
            std::string name(buf);
            // Проверяем длину перед удалением
            if (name.length() > 5) {
                name.erase(0, 5);
            } else {
                name.clear();
            }
            
            if (name.empty()) {
                send(client_sock, "Ошибка: имя не может быть пустым", 100, 0);
                close(client_sock);
                return;
            }
            
            if (socketByName.find(name) != socketByName.end()) {
                std::cerr << "Имя занято!\n";
                send(client_sock, "Ошибка, это имя уже занято", 100, 0);
                close(client_sock);
                return;
            } else {
                nameBySocket[client_sock] = name;
                socketByName[name] = client_sock;
                std::cout << "Клиент " << name << " подключен\n";
            }
        } else {
            close(client_sock);
            return;
        }
    }
    
    // Основной цикл обработки сообщений
    while (true) {
        char buf[1024] = {0};
        int bytes_read = recv(client_sock, buf, 1023, 0);
        
        if (bytes_read <= 0) {
            {
                std::lock_guard<std::mutex> lock(mtx);
                std::cout << "Пользователь завершил сессию\n";
            }
            break;
        }
        
        buf[bytes_read] = '\0';
        std::string message(buf);
        
        if (message.empty()) continue;
        
        // Личное сообщение
        if (message[0] == '@') {
            std::string n;
            int i = 1;
            while (i < message.size() && message[i] != ' ') {
                n += message[i];
                i++;
            }
            
            if (n.empty()) {
                send(client_sock, "Укажите имя получателя", 22, 0);
                continue;
            }
            
            int t_s = -1;
            {
                std::lock_guard<std::mutex> lock(namesMutex);
                auto it = socketByName.find(n);
                if (it != socketByName.end()) {
                    t_s = it->second;
                }
            }
            
            if (t_s == -1) {
                send(client_sock, "Пользователь не найден", 22, 0);
                continue;
            }
            
            std::string t = (i + 1 < message.size()) ? message.substr(i + 1) : "";
            if (t.empty()) continue;
            
            int r = send(t_s, t.c_str(), t.size(), 0);
            if (r < 0) {
                // Удаляем отключившегося пользователя
                std::lock_guard<std::mutex> lock(namesMutex);
                std::string targetName = nameBySocket[t_s];
                nameBySocket.erase(t_s);
                socketByName.erase(targetName);
                
                std::lock_guard<std::mutex> lock2(clientMutex);
                auto it = std::find(clients.begin(), clients.end(), t_s);
                if (it != clients.end()) clients.erase(it);
                
                close(t_s);
            }
        } 
        // Общее сообщение
        else {
            {
                std::lock_guard<std::mutex> lock(mtx);
                std::cout << "Получено сообщение: " << buf << '\n';
            }
            
            std::lock_guard<std::mutex> lock(clientMutex);
            for (int client : clients) {
                if (client != client_sock) {
                    int s = send(client, buf, bytes_read, 0);
                    if (s < 0) {
                        disc.push_back(client);
                    }
                }
            }
            
            // Удаляем отключившихся клиентов
            if (!disc.empty()) {
                for (int disconnected : disc) {
                    auto it = std::find(clients.begin(), clients.end(), disconnected);
                    if (it != clients.end()) {
                        clients.erase(it);
                    }
                    
                    std::lock_guard<std::mutex> lock(namesMutex);
                    auto nameIt = nameBySocket.find(disconnected);
                    if (nameIt != nameBySocket.end()) {
                        socketByName.erase(nameIt->second);
                        nameBySocket.erase(nameIt);
                    }
                }
                disc.clear();
            }
        }
    }
    
    // Очистка при отключении клиента
    {
        std::lock_guard<std::mutex> lock(namesMutex);
        auto nameIt = nameBySocket.find(client_sock);
        if (nameIt != nameBySocket.end()) {
            socketByName.erase(nameIt->second);
            nameBySocket.erase(nameIt);
        }
    }
    
    {
        std::lock_guard<std::mutex> lock(clientMutex);
        auto it = std::find(clients.begin(), clients.end(), client_sock);
        if (it != clients.end()) clients.erase(it);
    }
    
    close(client_sock);
}

void Server::bindNaccept() {
    while (true) {
        int client = accept(server_sock, NULL, NULL);
        if (client >= 0) {
            std::thread thr(&Server::handler, this, client);
            thr.detach();
        } else {
            std::lock_guard<std::mutex> lock(mtx);
            std::cout << "Ошибка принятия соединения\n";
        }
    }
}

Server::~Server() {
    close(server_sock);
}