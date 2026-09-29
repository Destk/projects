

def binsearch(arr : list ,target : int):
        print("Binary_search")
        arr.sort()
        st = 0
        en = len(arr) - 1
        i = 1
        while st <= en:
            mid = st + (en - st)// 2
            if(arr[mid] == target):
                print(f"Нашёл! Индекс: {mid}")
                return
            elif(arr[mid] < target):
                en = mid + 1
            else:
                st = mid - 1
def inp():
    arr = []
    val = input("Введите список чисел через пробел: ").split()
    arr = [int(x) for x in val]
    target = int(input("Введите число: "))
    return arr, target

def main():
    arr, target = inp()
    binsearch(arr, target)

if __name__ == '__main__':
    main()
