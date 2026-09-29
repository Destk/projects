import socket
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from progress.bar import IncrementalBar

class port_scan:
    
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995, 3306, 3389, 5432, 5900, 8080, 8443, 135, 139, 445, 1433, 1521, 1723, 3306, 3389, 5432, 5900, 8080, 8443]    
    res_scan = "" 
    timer = ""
    def __init__(self,ip,ports):
        self.ip = ip
        self.info = []
        if(len(ports) > 0):        
            self.common_ports = ports
    
    def test_port(self, ip):
        op_port = []
        for port in self.common_ports:
            with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)
                res = sock.connect_ex((ip,port))
                if res == 0:
                    op_port.append(port)
        if op_port:
            return {ip: op_port}

    def scan(self):
        res_scan = {}
        bar = IncrementalBar("Scan_ports", max = len(self.ip))
        st = time.time()
        with ThreadPoolExecutor(max_workers = len(self.ip)) as executor:
            for res in executor.map(self.test_port, self.ip):
                if res:
                    res_scan.update(res)
                #Для красоты, искуственная задержка, для bar 
                time.sleep(0.5)
                bar.next()
        bar.finish()
        en = time.time()
        self.timer = f"Затраченное время: {en-st:.2f}"
        self.info = res_scan
        

    def test_out(self):
        self.res_scan = f"Результат сканирования портов:\n{self.info}\n{self.timer}"
        print(self.res_scan)
    
    def save_f(self):
        now = datetime.now()
        date = now.strftime("%d-%m-%Y_%H-%M")
        fname = f"scan_{date}.txt"
        with open(fname, 'w') as file:
            file.write(f"Результат сканирования: \nАнализ ip-адрессов и просмотр открытых портов {self.res_scan}")


def scan_ports(ip,ports):
    sc_p = port_scan(ip,ports)
    sc_p.scan()
    sc_p.test_out()
    res = input("Сохранить Y/n: ")
    if res == 'y':
       sc_p.save_f()
