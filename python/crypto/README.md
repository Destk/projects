# File Crypto

Скрипт по шифрованию файлов.

## Что делает
- шифрует файл через Fernet
- ключ сохраняется рядом с файлом
- при дешифровании .enc и ключ удаляются
- если передать имя без .enc — находит .enc автоматически
 
## Что умеет
```bash
python3 file_crypto.py -f test.txt
```
Шифрует файл. Можно передавать полный путь к файлу из другой директории.

```bash
python3 file_crypto.py -f test.txt -d Ckey.txt
```
Дешифрует файл. Ключ создаётся при шифровании рядом с файлом.

```bash
python3 file_crypto.py --help
```
Справка по скрипту.

## Стек
Python 3, cryptography, pathlib, argparse

## Пример работы
```bash

❯ ls

.rw-r--r-- 2,5k file_crypto.py
.rw-r--r--   18 test.txt


❯ python3 file_crypto.py -f test.txt


❯ ls

.rw-r--r--   44  Ckey.txt
.rw-r--r-- 2,5k  file_crypto.py
.rw-r--r--  120  test.txt.enc


❯ cat Ckey.txt
jOTyqZiu7UsKoWjzBeYqQFnsL5m2xtt_RH5ffGFraPI=⏎

❯ cat test.txt.enc
gAAAAABq8FOHeliFxw1TNa8uwokG0lxkRBgxZqYgjUgpkItDcSTVKpF-T_gYCgdhWK26ZHnZ3JU-57tQ7kUVpH3-SHWPrSp0jpdFmFtS24n4nT9Nb-cFxlE=⏎

❯ python3 file_crypto.py -f test.txt -d Ckey.txt


❯ ls
drwxr-xr-x    - bob 30 окт 21:51  .venv1
.rw-r--r-- 2,5k bob  8 ноя 13:36  file_crypto.py
.rw-r--r--  875 bob  8 ноя 13:47 󰂺 README.md
.rw-r--r--   18 bob  8 ноя 13:48  test.txt


❯ cat test.txt
teeest srcipt lol

```
