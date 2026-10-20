# SSH Failed Logins Parser

Парсер журнала `journalctl` для обнаружения попыток брутфорса SSH.

## Что делает
- Читает логи указанного сервиса через `journalctl`
- Ищет `Failed password`
- Извлекает IP, логин, время
- Считает топ IP и логинов
- Сохраняет отчёт в JSON

## Запуск
```bash
python3 parser.py --service sshd --since "10 days ago"
