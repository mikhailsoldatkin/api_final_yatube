## Yatube API

#### *API для социальной сети "Yatube"*

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
- Выполнить миграции:
```
python manage.py migrate
```
- Запустить сервер:
```
python manage.py runserver
```
### Примеры запросов к API:

- Получить список всех публикаций, GET-запрос:
```
yatube.com/api/v1/posts/
```
- Добавление нового комментария к публикации, POST-запрос:
```
yatube.com/api/v1/posts/{post_id}/comments/
```

### Автор
Михаил Солдаткин
