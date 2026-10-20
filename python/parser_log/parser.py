import subprocess 
import re
from collections import Counter
import json
import argparse

#Функция для парса аргументов командной строки(сервис и since для journalctl)
def inp():
    pars_arg = argparse.ArgumentParser(description='Set service and since')
    pars_arg.add_argument('--service', type=str,default="sshd" ,help="set service from journalctl")
    pars_arg.add_argument('--since', type=str,default="7 days ago" ,help='set date')
    args = pars_arg.parse_args()
    parse(args)

#Основная фкнция программы для парса нашего журнала
def parse(args):
#Отлавливаем ошибку если с journalctl проблемы
    try:
        logs = subprocess.run(["journalctl", "-u",args.service , "-p", "info", "--since", args.since], text=True, capture_output=True)
    except FileNotFoundError:
        print("journalctl не установлен")
        return
#Ключевые объекты(логины, ip, входы, счетчик попыток)
    logins = Counter()
    ips = Counter()
    entries = []
    count_f = 0
#Парсим текст на брутфорс
    if logs.returncode == 0:
        for s in logs.stdout.splitlines():
            if "Failed password" in s:
                count_f+=1
                mes_log = re.search(r"for (\S+) from", s)
                mes_ip = re.search(r"from (\S+) port", s)
                t = re.search(r"[а-я]+\s\d{1,2}\s\d{2}:\d{2}:\d{2}", s)
                if mes_log and mes_ip and t:
                    logins[mes_log.group(1)]+=1
                    ips[mes_ip.group(1)]+=1
                    d = {"time": t.group(0), "user":mes_log.group(1), "ip":mes_ip.group(1)}
                    entries.append(d) 
    else:
        print("Журнал не найден")
        return
    output(logins, ips, entries, count_f)

#Функция для красивого вывода
def output(logins : dict, ips : dict, entries : list, count_f : int):
    log = [f"{i}. {key} - {val} попыток" for i, (key, val) in enumerate(logins.most_common(), 1)]
    ip = [f"{i}. {key} - {val} попыток" for i,(key, val) in enumerate(ips.most_common(),1)]
    print(f"=== SSH Failed Logins Report ===\nВсего попыток: {count_f}\n\n--- Top IP ---\n{f"{'\n'.join(ip)}"}\n\n--- Top Logins ---\n{f"{'\n'.join(log)}"}\n\n")
    save = input("Сохранить в json? (Y/n): ")
    if save.lower() == 'y' or save == "":
        save_json(entries)
#Функция для сохранения резульата в json формате
def save_json(entries):
    with open("failed_logins.json", "w") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)
    
def main():
    print("Парсер bruteforce in ssh")
    inp()

if __name__ == "__main__":
    main()
