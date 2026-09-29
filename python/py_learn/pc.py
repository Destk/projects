from pathlib import Path
import math
def info_f(file_path,count_f):
    out = f"file name: {file_path.name}\nsize: {math.ceil(file_path.stat().st_size / 1024 / 1024)} MB\nfiles: {count_f}"
    for l in out.split('\n'):
        print(l.center(30))
def work(): 
    p = Path("/var/log")
    count_ = 0
    m = 0
    name_m = ""
    for file in p.glob("*.log"):
        if(m <  file.stat().st_size):
            m = file.stat().st_size
            name_m = file
        count_ += 1
    info_f(name_m, count_)

def main():
    print("=== Программа по подсчету логов ===")
    work()

if __name__ == "__main__":
    main()
