# Бот The DelLuxe Family

## Работа в фоновом режиме
Команды для управления фоновым режимом 

1. Перезапуск systemd `sudo systemctl daemon-reload`
2. Включить автозапуск `sudo systemctl enable tdf`
3. Запуск сервиса `sudo systemctl start tdf`
4. Статус сервиса `sudo systemctl status myscript`
5. Остановка сервиса `sudo systemctl stop tdf.service`
6. Логи `journalctl -u tdf -f`
