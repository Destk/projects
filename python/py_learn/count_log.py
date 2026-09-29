def f(log : list(int)) -> dict([str, int]):
    res = {}
    for i in log:
        line = i.split()
        info = line[2]
        if info not in res:
            res[info]=1
        else:
            res[info] = res.get(info)+1
    return res

def main():
    logs = [
    "2025-01-01 10:00 INFO Запуск",
    "2025-01-01 10:05 ERROR Ошибка",
    "2025-01-01 10:10 WARNING Нагрузка",
    ]
    res = f(logs)
    print(res)

if __name__ == '__main__':
    main()
    
