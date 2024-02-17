# OOO-Standart_test_task
Это проект подготовлен как тестовое задание от ООО Стандарт гор. Пермь 2024 год.

**_Проект доступен локально по адресу : http://localhost:8000/_**

**_Репозиторий проекта:_**
```
git@github.com:FluckyGo/foodgram-project-react.git
```

### _Запуск проекта локально:_

**_Репозиторий проекта, клонируйте на локальный компьютер_:**
```
git@github.com:FluckyGo/OOO-Standart_test_task.git
```

**_В директории проекта на примере .env.example создать .env:_**
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
**_Перейти в папку nginx:**
```
cd nginx/
```

**_Запустить проект с помощью Docker_:**
```
sudo docker compose up --build

sudo docker compose exec backend python manage.py makemigrations

sudo docker compose exec backend python manage.py migrate

sudo docker compose exec backend python manage.py collectstatic

sudo docker compose -f docker-compose.production.yml exec backend cp -r /app//backend_static/static/. /backend_static/static/

sudo docker compose exec backend python manage.py createsuperuser

```

**_Наполение проекта данными с помощью DB seeder для Django ORM:**
```
sudo docker compose exec backend python manage.py seed request --number=100

```

### *Бэк написал:*
[FluckyGo](https://github.com/FluckyGo)
