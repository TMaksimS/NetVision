### netvision_case
## ТЕХНИЧЕСКОЕ ОПИСАНИЕ:
 - Проект написан на python3.10
         Для серверного приложения использованы библиотеки FastAPI, SQLalchemy, alembic
         Для клиентского приложения использованы библиотека aiohttp
         Для напсиания тестов использована библиотека pytest
 - Проект запускает базу данных postgresql серверное приложение на FastAPI и клента на aiohttp
 

## ЗАПУСК ПРИЛОЖЕНИЯ:
- Для запуска приложения используйте команду из дирректории проекта:
        ```make up_ci```
  Данная команда соберет docker compose образ, и выведет логи серверного приложения, а так же будет транслировать логи клиентского приложения.
- Для прекращения работы приложения используйте команду:
        ```make down_ci```
  Данная команда выключит запущенные контейнеры и удалит образ клиент-серверного приложения.
- Для прогона тестов серверного приложения используйте команду из дирректории проекта:
        ```pip install -r requirementx.txt```
        ```make up```
  Команда запустит тестовую базу данных, запустит миграции, запустит серверное приложение после чего вам надо будет из дирректории запустить команду:
        ```pytest```

## ТЕХНИЧЕСКОЕ ЗАДАНИЕ:

  Используя Python3, FastAPI, SQLAlchemy написать:
- [REST API сервер](#веб-приложение-микросервис)
- [Клиентское приложение](#клиентское-приложение-микросервис)
 Веб-приложение (микросервис)
Необходимо реализовать следующие endpoint:
- POST `/new`
    Сохраняет запись в базу данных и присваивает ей уникальный идентификатор uuid. Пример тела запроса:
    ```json
    [
        {"uuid": "e48d41d0-6e53-490a-9d9a-fd4337f28038", "text": "test example"},
        {"uuid": "eddd8cd7-1128-4b83-98d4-7cde1514625e", "text": "another example"}
    ]
    ```
-  GET `/all`
    Отдаёт все добавленные записи, пример тела ответа:
    ```json
    [
        {"uuid": "e48d41d0-6e53-490a-9d9a-fd4337f28038", "text": "test example"},
        {"uuid": "eddd8cd7-1128-4b83-98d4-7cde1514625e", "text": "another example"}
    ]
    ```
- GET `/<uuid>`
    Отдаёт конкретную запись по запрошенному uuid. Если записи не существует, отдаёт HTTP 404. Пример успешного ответа:
    ```json
    {"uuid": "e48d41d0-6e53-490a-9d9a-fd4337f28038", "text": "test example"}
    ```
- GET `/<count>`
    Отдаёт запрошенное в <count> количество записей. Пример успешного ответа:
    ```json
    [
        {"uuid": "e48d41d0-6e53-490a-9d9a-fd4337f28038", "text": "test example"},
        {"uuid": "eddd8cd7-1128-4b83-98d4-7cde1514625e", "text": "another example"}
    ]
    ```
- DELETE `/<uuid>`
    Удаляет запись по запрошенному uuid из базы. Если записи не существует, отдаёт HTTP 404. В случае успеха возвращает HTTP 200.
 Клиентское приложение (микросервис)
Запускается вместе с первым и постоянно генерирует случайное количество (от 10 до 100) случайных строк (буквы-цифры, 16 символов) для вставки в базу первого сервиса по API.
Одновременно с этим приложение постоянно запрашивает по API по 10 строк и удаляет их, раз в 10 секунд в стандартный поток вывода необходимо печать количество удалённых записей.
 Примечания
- Базу данных можно использовать любую
- Обеспечить запуск через "docker compose up"
