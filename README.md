# Yatube REST API
Учебный проект Яндекс Практикум (курс Python-разработчик).

## Описание
API-сервис для социальной сети [Yatube](https://github.com/bvsvrvb/praktikum-yatube), позволяющий настроить полное взаимодействие с социальной сетью через сторонний интерфейс. Аутентификация реализована с использованием JWT-токенов.

## Технологии
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django_REST_Framework-464646?style=flat-square&logo=django)](https://www.django-rest-framework.org/)
[![SQLite](https://img.shields.io/badge/-SQLite-464646?style=flat-square&logo=sqlite)](https://www.sqlite.org/)

## Доступные эндпоинты
- `api/v1/jwt/create/` (POST): передаём логин и пароль, получаем токен;
- `api/v1/jwt/refresh/` (POST): обновляем токен;
- `api/v1/jwt/verify/` (POST): проверяем токен;
- `api/v1/posts/` (GET, POST): получаем список всех постов или создаём новый пост;
- `api/v1/posts/{post_id}/` (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по `id`;
- `api/v1/groups/` (GET): получаем список всех групп;
- `api/v1/groups/{group_id}/` (GET): получаем информацию о группе по `id`;
- `api/v1/posts/{post_id}/comments/` (GET, POST): получаем список всех комментариев поста с  `id=post_id` или создаём новый, указав `id` поста, который хотим прокомментировать;
- `api/v1/posts/{post_id}/comments/{comment_id}/` (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий по `id` у поста с `id=post_id`;
- `api/v1/follow/` (GET, POST): получаем список всех подписок пользователя или подписываемся на другого пользователя.

## Документация к API
Подробная документация к API будет доступна после запуска проекта по адресу:
```
http://127.0.0.1:8000/redoc/
```

## Запуск проекта в Dev-режиме
Клонировать репозиторий и перейти в директорию проекта:
```bash
git clone https://github.com/bvsvrvb/praktikum-yatube-api.git
```
```bash
cd praktikum-yatube-api
```

Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv
```
```bash
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:
```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Перейти в директорию с manage.py и выполнить миграции:
```bash
cd yatube_api
```
```bash
python manage.py migrate
```

Создать суперпользователя для админ-панели:
```bash
python manage.py createsuperuser
```

Запустить сервер разработчика:
```bash
python manage.py runserver
```
