## Yatube API

#### *API для социальной сети "Yatube"*

### Технологии:

Python, Django, Git, Django ORM, SQLite

### Запуск проекта:

- Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/mikhailsoldatkin/api_final_yatube.git

cd api_final_yatube
```

- Создать и активировать виртуальное окружение:

```
python -m venv venv 

source venv/bin/activate
```

- Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip 

pip install -r requirements.txt
```

- Перейти в рабочую папку и выполнить миграции:

```
cd yatube_api

python manage.py migrate
```

- Запустить сервер:

```
python manage.py runserver
```

### Примеры запросов к API:

- Получение списка всех публикаций:

*Запрос:*

```
GET yatube.com/api/v1/posts/
```

*Пример ответа:*

```
[
    {
        "id": 1,
        "author": "string",
        "text": "string",
        "pub_date": "2022-04-08T07:51:18.644110Z",
        "image": "string",
        "group": 1
    },
    {
        "id": 2,
        "author": "string",
        "text": "string",
        "pub_date": "2022-04-08T07:54:09.216636Z",
        "image": "string",
        "group": 2
    },
]
```

- Добавление нового комментария к публикации:

*Запрос:*

```
POST yatube.com/api/v1/posts/{post_id}/comments/
```

*Содержимое запроса:*

```
{
  "text": "comment text"
}
```

*Пример ответа:*

```
{
    "id": 2,
    "author": "string",
    "text": "comment text",
    "created": "2022-04-08T20:24:33.044802Z",
    "post": 1
}
```

- Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса:

*Запрос:*

```
POST yatube.com/api/v1/follow/
```

*Содержимое запроса:*

```
{
  "following": "string"
}
```

*Пример ответа:*

```
{
  "user": "string",
  "following": "string"
}
```


### Автор:

Михаил Солдаткин
