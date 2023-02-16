# Kettle_class
Для запуска проекта:
  1. Склонировать репозиторий;
  2. Создать и активировать виртуальное окружение;
  3. Перейти в директорию Kettle_class;
  4. Установить зависимости (pip install -r requirements.txt);
  5. Осуществить миграции в БД SQLite (pyton3 manage.py migrate).
  
После запуска команды python3 manage.py start_boiling начнет исполнятся программа (задать свои параметры для исполнения можно в файле config.ini).
Производится логирование в консоль, также логирование в файл kettle_logs.log, которые создастся в текущей директории.

Ведется запись в БД SQLite (через Django ORM). Для просмотра через панель администратора:
  1. python3 manage.py createsuperuser;
  2. python manage.py runserver;
  3. Перейти localhost:8000/admin, можно просматривать логи в БД.
