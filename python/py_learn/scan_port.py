import socket

add=input("Введите ip-адресс: ")
sock = socket.socket()
for i in range(1, 1025):
    if(sock.connect_ex((add, i)) == 0):
        print(f"Порт {i} открыт")

