#Калькулятор

def operations(op:str, num1:int, num2:int) -> int:
    match op:
        case '+':
            print(num1+num2)
        case '-':
            print(num1-num2)
        case '*':
            print(num1*num2)
        case '/':
            if(sum1 == 0 or sum2 == 0):
                print("На 0 делить нельзя!")
            print(num1/num2)
        case _:
            print("Операция не найдена")
def f():
    print("----Калькулятор----")
    op = str(input("Введите операцию из перечисленных (+,-,*,/):"))
    try:
        num1 = int(input("Введите число число: "))
        num2 = int(input("Введите число число: "))
    except 'ValueERROR' :
        print("Вы ввели не целочисленное значение!")
    operations(op,num1,num2)
        
def main():
    stop_ = False
    while(not stop_):
        f()
        que = str(input("Продолжить?: (y/n): "))
        if(que == 'n'):
            stop_ = True

if __name__ == "__main__":
    main()
