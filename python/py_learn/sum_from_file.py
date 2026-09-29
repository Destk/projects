def sum_f():
    with open('numbers.txt', 'r') as f:
       sum = 0
       for line in f:
           sum+=int(line)
       print(sum)

def main():
    sum_f()

if __name__ == "__main__":
    main()
