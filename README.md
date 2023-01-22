### Описание

API-сервис для социальной сети Yatube, позволяющий настроить полное взаимодействие с социальной сетью через сторонний интерфейс.

### Установка

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/bvsvrvb/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Документация к API

После запуска проекта будет доступна по адресу:

```
http://127.0.0.1:8000/redoc/
```