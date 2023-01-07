# NET HW2

### Барабанщиков Лев, ИУ5-54Б, 2022-2023 гг.

## Задание

Необходимо разработать два сервиса для отправки сообщений: брокер с очередью сообщений и сервис отправки. У каждого
студента один из источников (email, телеграм, vk) по варианту. За счет очереди должна быть предусмотрена гарантированная
отправка в случае недоставки сообщения. Если сообщение не было доставлено, оно повторно отправляется из очереди.

Требования к приложению:

1. Брокер
2. Демонстрация с помощью клиентов почты/телеграм/vk

Порядок показа:

1. При включенном подключении к интернету отправить сообщение в брокер. Сообщение должно быть отправлено один раз
   получателю
2. Отключить от интернета. В шлюзе сообщений должна быть видна история попыток отправить уведомление. После последней
   попытки должно быть выведено сообщение об ошибке/ручной обработке

## Реализация и запуск

1. Установить зависимости:

   ```bash
   pip install -r requirements.txt
   ```
2. Создать базу данных, используя команды из `script.sql`

3. Запустить приложение для обновления базы данных:

   ```bash
   python3 db_updater.py
   ```

4. Запустить приложение для отправки сообщений:

   ```bash
   python3 sender.py
   ```
