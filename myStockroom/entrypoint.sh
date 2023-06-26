#!/bin/sh
if [ "$DATABASE" = "buildAndTech" ]
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
python3 manage.py makemigrations
sleep 1
python3 manage.py migrate
sleep 1
python3 manage.py collectstatic
sleep 1
pytest --cov
exec "$@"
