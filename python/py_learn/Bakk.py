class Bank:
    owner = ""
    balance = 0
    def open_(self):
        self.owner = input("Открыть счет на имя: ")
    def deposit(self, money):
        self.balance += money
    def withdraw(self, money):
        self.balance -= money
    def getBalance(self):
        print(f"Ваш баланс на счету составляет {self.balance} рублей")

def main():
    B = Bank()
    B.open_()
    B.deposit(5100)
    B.getBalance()
    B.withdraw(100)
    B.getBalance()

if __name__ == '__main__':
    main()
