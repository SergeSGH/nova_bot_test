# Тестовый проект - отправка номера телефона из бота Telegram
### Стэк:
```
Telegram API: https://core.telegram.org/bots/api/
```
```
Python, Django
```

###  Основные функции:

```
Проект работает как клиент для Webhook запросов API Telegram
```
```
При инициализации бота проект получает запрос от Telegram
и отправляет приветственное сообщение в чат с предложением прислать номер телефона
```
```
Сообщение отправляется только если команду /start отправляет
новый пользователь. Базу пользователей можно очистить через интерфейс администратора
```
```
Номер телефона клиента направляется на https://s1-nova.ru/app/private_test_python/ 
```
