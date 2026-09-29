class user:
    username = ""
    email = ""
    password = ""
    bd = ([])
    def set_name(self):
        self.username = input("Введите имя пользователя: ")
        if(len(self.username) == 0):
            print("Вы не ввели имя!")
            exit(1)
    def set_email(self):
        self.email = input("Введите почту: ")
        if(len(self.email) == 0 or self.email.count("@") < 1):
            print("Вы не ввели почту!")
            exit(1)
    def set_passw(self):
        self.password = input("Введите пароль: ")
        if(len(self.password) <= 6):
            print("Длина пароля меньше 6!")
            exit(1)
def menu() -> int:
    print("---Меню---")
    print("1.Регистрация")
    print("2.Вход")
    print("----------")
    inp = input("Ввод: ")
    if( 1 > inp > 2 ):
        print("Ошибка ввода!")
        exit(1)
    return inp

def work():
    stop = True
    while(stop):
        inp = menu()
        u = user()
        match inp:
            case 1:
                u.set_username()
                u.set_email()
                u.set_password()
            case 2:
                #Пока ничего, потом доделаю
        n = input("Продолжить? (y/n)): ")
        if(n == 'y' or n == 'Y'):
            pass
        else:
            stop = False


def main():
    work()

if __name__ == '__main__':
    main()
