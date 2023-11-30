# django-stripe
Тестовое задание "Простые решения"

# Start project with docker
***Важно! Перед запуском приложения подготовить .env файл (файл .env.example переименовать на .env и заполнить данные)***

```
docker-compose up --build
```
Далее создайте суперпользователя (для доступа к админ-панели)
```
docker-compose exec web python manage.py createsuperuser
```

# API
После запуска проекта API будет доступно по адресу
<br>http://127.0.0.1:8000/docs/ либо 
<br>http://127.0.0.1:8000/redoc
