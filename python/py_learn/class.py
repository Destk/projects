class Humen:
    name = ""
    age = 0
    city = ""
    def setName(self):
        self.name = input("Введите имя: ")
    def setAge(self):
        self.age = input("Введите возраст: ")
    def setCity(self):
        self.city = input("Введите город: ")
    def out(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет и с города {self.city}")



def main():
    man = Humen()
    man.setName()
    man.setAge()
    man.setCity()
    man.out()

if __name__ == '__main__':
    main()
