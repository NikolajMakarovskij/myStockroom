until cd myStockroom/
do
    echo "Waiting for server volume..."
done
until ./manage.py makemigrations
do
    echo "Waiting for server volume..."
    sleep 5
done
until ./manage.py migrate
do    
    echo "Waiting for server volume..."
    sleep 5
done
./manage.py collectstatic --noinput
