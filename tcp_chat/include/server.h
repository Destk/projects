#ifndef SERVER_H
#define SERVER_H
#include <unistd.h>
#include <netinet/in.h>  // для sockaddr_in
#include <sys/socket.h>  // для socket
#include <iostream>
#include <thread> // для управления потоками
#include <chrono> // для разграничения по времени
#include <mutex> //блокировка потоков
#include <vector>
#include <algorithm>
#include <unordered_map> // для сохранения пользователя и его сокета
#include <string>
#include <memory.h>
class Server{
    private:
        int server_sock;
        struct sockaddr_in addr;
        int port;
        std::mutex mtx;
        std::vector<int> clients;
        std::mutex clientMutex;
        std::vector<int> disc;
        std::unordered_map<int, std::string> nameBySocket;
        std::unordered_map<std::string, int> socketByName;
        std::mutex namesMutex;   
    public:
        Server();
        void bindNaccept();
        ~Server();
        void handler(int client_sock);
};
#endif //SERVER_H 