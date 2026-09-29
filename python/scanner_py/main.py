import ping_sweep
from ping_sweep import start_scan
import port_scan
import sys
from port_scan import scan_ports
from datetime import datetime

def inp():
    if len(sys.argv) >= 4 and sys.argv[2] == '--ports' and sys.argv[3] != "":
        return sys.argv[1], sys.argv[3]

def interface():
    print("=== Сканнер локальной сети ===\n")
    ip = input("Введите ip-adress с маской сети \nПример ввода: 192.0.52.21/24\nВводе: ")
    return ip

def Scanning():
    ip, ports = inp()
    ports = ports.split(",")
    ports = [int(p) for p in ports]
    ips = ""
    if(len(ip) >= 1):
        ips = start_scan(ip)    
    else:
        ips = start_scan(interface())
    scan_ports(ips, ports)

def main():
    Scanning()

if __name__ == '__main__':
    main()
