import subprocess 
import re
from collections import Counter
import json

def parse():
    try:
        logs = subprocess.run(["journalctl", "-u", "sshd", "-p", "info"], text=True, capture_output=True)
    except FileNotFoundError:
        print("journalctl не установлен")
        return
#Ключевые объекты(логины, ip, входы, счетчик попыток)
    logins = Counter()
    ips = Counter()
    entries = []
    count_f = 0
#парсим текст на брутфорс
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
    #красивый вывод
    output(logins, ips, entries, count_f)

def output(logins : dict, ips : dict, entries : list, count_f : int):
    log = [f"{i}. {key} - {val} попыток" for i, (key, val) in enumerate(logins.most_common(), 1)]
    ip = [f"{i}. {key} - {val} попыток" for i,(key, val) in enumerate(ips.most_common(),1)]
    print(f"=== SSH Failed Logins Report ===\nВсего попыток: {count_f}\n\n--- Top IP ---\n{f"{'\n'.join(ip)}"}\n\n--- Top Logins ---\n{f"{'\n'.join(log)}"}\n\n")
    save = input("Сохранить в json? (Y/n): ")
    if save.lower() == 'y' or save == "":
        save_json(entries)

def save_json(entries):
    with open("failed_logins.json", "w") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)
    

def main():
    print("Парсер bruteforce in ssh")
    parse()

if __name__ == "__main__":
    main()
