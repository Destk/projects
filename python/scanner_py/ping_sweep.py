import subprocess as sb
from concurrent.futures import ThreadPoolExecutor
import time
import sys
from progress.bar import IncrementalBar
from datetime import datetime

class net_test:
    #Инициализируем саму сеть из ввода пользователя и 2 списка(доступные ip и список ip-адресов)
    def __init__(self,nt):
        self.network = nt
        self.avail = []
        self.ips = [] 

    #Генерируем список ip адресов сети
    def gen_ip(self):
        parts = self.network.split("/")
        ip = parts[0].split(".")[:-1]
        ip_b = ".".join(ip)
        mask = int(parts[1])
        hosts = 2**(32-mask)-2
        for i in range(1, hosts):
            self.ips.append(ip_b + f".{i}")
        
    #Проходим по списку ips
    def ping_ip(self, ip):
        res = sb.run(["ping", "-c", "1", "-W", "1",ip], stdout = sb.DEVNULL, stderr = sb.DEVNULL)
        if(res.returncode == 0):
            self.avail.append(ip)
    
    #Многопоточный сканер
    def scan(self):
        self.gen_ip()
        bar = IncrementalBar('Scanning', max = len(self.ips))
        with ThreadPoolExecutor(200) as executor:
            for _ in executor.map(self.ping_ip,self.ips):
                bar.next()
                pass
        bar.finish()

    #Вывод результата
    def Out(self):
        print(f"=== Доступные ip ===\n{self.avail}")

#Функция для работы программы
def start_scan(inet):
    scan_inet = net_test(inet)
    st = time.time()
    scan_inet.scan()
    en = time.time()
    scan_inet.Out()
    print(f"Затраченное Время: {en-st:.2f}")
    return scan_inet.avail
