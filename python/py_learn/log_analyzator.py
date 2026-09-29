#Функция по работе с логом и подсчетом файлов
def f(file : open) -> int:
    c = 0 #счетчик строк
    for line in file:
        c += 1
    return c

def menu() -> int:
    print("1.Подсчёт строк")
    return input("Выберите функцию из перечисленных: ")
    

def work():
    print("===Анализатор лога===")
    stop_ = False
    while(not stop_):
        path = input("Введите путь к файлу: ")
        with open(path, 'r') as file:
            Ack = menu()
            match Ack:
                case '1':
                    print(f(file))
                case _:
                    print("Неизвестная команда")
        flag = input("Продолжит y/n: ")
        if(flag != 'y' and flag != 'Y'):
            stop_ = True

def main():
    work()

if __name__ == "__main__":
    main()

    
