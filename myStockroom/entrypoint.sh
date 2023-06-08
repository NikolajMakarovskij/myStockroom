#!/bin/sh
if [ "$DATABASE" = "postgres" ]
then
    # если база еще не запущена
    echo "Ожидание..."
    # Проверяем доступность хоста и порта
    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done
    echo "Старт!"
fi
# Выполняем миграции
python manage.py makemigrations
python manage.py migrate
exec "$@"
