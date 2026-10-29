import argparse
import subprocess
import re
import json
from collections import Counter

class Parser:
    def __init__(self):
        self.ip = Counter()
        self.login = Counter()
        self.out = []
        self.pars_arg = argparse.ArgumentParser(description='Парсер событий нацеленный на bruteforce')
        self.pars_arg.add_argument('-s', '--service', type=str, help='set service from journalctl', default="sshd")
        self.pars_arg.add_argument('-d', '--since', type=str, help='set since from journalctl (7 days ago...)',default="7 days ago")
        self.pars_arg.add_argument('-o', '--output_name', type=str, help='set output_name to file.json', default='error.json')
        self.args = self.pars_arg.parse_args()
    def check_log(self):
        try:
            self.res = subprocess.run(["journalctl", '-u', self.args.service, '--since', self.args.since], capture_output=True, text=True)
        except FileNotFoundError:
            print("Такого файла не найдено!")
            return 0
        if(self.res.returncode==0):
            self.pars_str(self.res.stdout)
    def pars_str(self, log : str):
        for line in log.splitlines():
            if "Failed password" in line:
               regex = re.search(r'for (\S+) from (\S+) port',line)
               time_m = re.search(r"[а-я]+\s\d{1,2}\s\d{2}:\d{2}:\d{2}", line)
               if regex  and time_m:
                   self.login[regex.group(1)] +=1
                   self.ip[regex.group(2)] += 1
                   self.out.append({'time':time_m.group(0), 'user': regex.group(1), 'ip': regex.group(2)})
    def out_cli(self):
        print("=== Результат сканирования ===")
        print("--- Топ логинов ---")
        for i, (user, count) in enumerate(self.login.most_common(), 1):
            print(f"{i}. {user} — {count} попыток")
        print("\n--- Топ IP ---")
        for i, (ip, count) in enumerate(self.ip.most_common(), 1):
            print(f"{i}. {ip} — {count} попыток")
        self.save_json()
    def save_json(self):
        with open(self.args.output_name, 'w') as f:
            f.write(json.dumps(self.out,ensure_ascii=False,indent=2))

def start_pars():
    print("---- Парсер логов на bruteforce ----")
    p = Parser()
    p.check_log()
    p.out_cli()

def main():
    start_pars()

if __name__ == "__main__":
    main()
