#Вывод сумму чисел до заданного значения, включительно!
n = int(input("Введите число: "))
sum=0
for i in range(1,n+1):
    sum+=i
    if(i == n):
        print(f"Сумма чисел от 1 до {n}: {sum}")
        break
    print(i)

