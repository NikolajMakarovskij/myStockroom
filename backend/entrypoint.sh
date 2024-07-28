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
echo "Выполняем миграции"
pdm run manage.py makemigrations
sleep 1
pdm run manage.py migrate
sleep 1
echo "Собираем статику"
pdm run manage.py collectstatic <<EOF
yes
EOF
exec "$@"
