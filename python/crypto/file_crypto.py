#Шифрование файлов 
from cryptography.fernet import Fernet
from pathlib import Path
import argparse 


class Crypto:
    def __init__(self,name,d):
        try:
            self.p = Path(name)
            if self.p.exists() == False and Path(str(self.p) + '.enc').exists():
                self.p = Path(str(self.p) + '.enc')
        except TypeError:
            print("Name file : None")
            return
        self.d = d
        self.dir = self.p.parent
        if self.d == None:
            self.k = Fernet.generate_key()
            self.f = Fernet(self.k)
        else:
            #Достаем ключ шифрования
            with open(self.d, "r", encoding='utf-8') as f:
                data = f.read()
            self.f = Fernet(data)
    
    def crypto_f(self):
        #Считываем информацию
        with open(self.p, 'rb') as file:
            data = file.read()
        crypted = self.f.encrypt(data)
        #Перезаписываем в файл
        with open(self.p.with_name(self.p.name + ".enc"), "wb") as file:
            file.write(crypted)
        #Удаляем оригинал
        self.p.unlink()
        #Сохраняем ключ
        self.save_f()

    def decrypto_f(self):
        with open(self.p, 'rb') as file:
            data = file.read()
        decrypt = self.f.decrypt(data)
        #Перезаписываем расшифрованное сообщение
        with open(self.p.with_suffix(""), "wb") as file:
            file.write(decrypt)
        self.p.unlink() 
        Path(self.d).unlink()
    
    def save_f(self):
        try:
            with open(self.dir / "Ckey.txt", 'w') as file:
                file.write(self.k.decode())
        except OSError as e:
            print(f"Не удалось сохранить ключ: {e}")
            return       

def main():
    parser = argparse.ArgumentParser(description="Шифрование файлов в одной директории")
    parser.add_argument("--file", "-f", type=str,default=None, help="Флаг для вставки имени файла для шифрования")
    parser.add_argument("-d", type=str, default=None, help="Файл с крипто-ключом для дешифрования")
    args=parser.parse_args()
    crypto = Crypto(args.file, args.d)
    if(args.d != None and args.file != None):
        crypto.decrypto_f()
    elif args.file != None:
        crypto.crypto_f()

if __name__ == '__main__':
    main()
