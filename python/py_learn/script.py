from pathlib import Path

def log_analyzer():
    path_ = input("Введите путь к логу: ")
    p = Path(path_)
    l = 0
    with open(p, 'r') as file:
        for line in file:
            l+=1
    info(l, p.stat().st_size)

def info(l,s):
    print(f"=== Log Analyz ===\nLines: {l}\nSize: {s/1024} KB")

def main():
    g = ""
    while g.lower() != 'n':
        log_analyzer()
        g = input("Продолжить? (Y/n): ")

if __name__ == "__main__":
    main()


