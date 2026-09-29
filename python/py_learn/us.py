class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_active = True
    def deactive(self):
        self.is_active = False

def Create():
    n = input("Введите имя пользователя: ")
    a = int(input("Введите возраст пользователя: "))
    user = User(n,a)
    print(f"Ваш пользователь создан: Name: {user.name}\nAge: {user.age}\nis_active: {user.is_active}")
    user.deactive()
    print(user.is_active)
    

def Menu():
    print("--- Меню ---")
    print("1) Создать Пользователя")
    print("--- Конец ---")
    s = int(input("Введите команду: "))
    match s:
        case 1:
            Create()

def main():
    st = True
    while(st == True):
        Menu()
        f = input("Продолжить: (y/n) ")
        if( f.lower() != "y" ):
            st = False

if __name__ == "__main__":
    main()
