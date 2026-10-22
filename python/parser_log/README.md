# SSH Failed Logins Parser

Парсер журнала `journalctl` для обнаружения попыток брутфорса SSH.

## Что делает
- Читает логи указанного сервиса через `journalctl`
- Ищет `Failed password`
- Извлекает IP, логин, время
- Считает топ IP и логинов
- Сохраняет отчёт в JSON

## Запуск
1)Запуск скрипта с 2 флагами, где --service указания сервиса, --since промежуток времени
```bash
python3 parser.py --service sshd --since "10 days ago"
```
2)флаг -o сохраняем в файл 
```bash
python3 parser.py -o filename.json
```
3)Вывод справки по скрипту
```bash
python3 parser.py --help 
```

## Пример вывода
```
=== SSH Failed Logins Report ===
Всего попыток: 3

--- Top IP ---
1. ::1 - 3 попыток

--- Top Logins ---
1. root - 3 попыток
```

## Стек
Python 3, `subprocess`, `re`, `collections.Counter`, `json`, `argparse`

## Аргументы
- `--service` — сервис journalctl (по умолчанию `sshd`)
- `--since` — период (по умолчанию `7 days ago`)
- `-o`, `--output` — файл для JSON (если не указан — не сохраняется)

---
