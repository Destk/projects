import time
import sys


def Save(err : list):
    date = time.strftime('%y_%m_%d-%H_%M')
    filename = f"errors_{date}.txt"
    with open(filename, 'w') as file:
        for i in err:
            file.write(i + '\n')
        
def log_monitor(path : str):
    err = []
    log_notice = ['error', 'warning', 'critical']
    with open(path, 'r') as file:
        for line in file:
            for word in log_notice:
                if log_notice in line.lower():
                    err.append(line)
                    break
    Save(err) 

def interface():
    print("=== Лог-монитор ===")
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:    
        path = input("Введите полынй путь к логу: ")
    log_monitor(path)

def main():
    interface()



if __name__ == "__main__":
    main()
