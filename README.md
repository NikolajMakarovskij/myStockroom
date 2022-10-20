# myBase1
  
  
migrate database
  python3 manage.py makemigrations
  python3 manage.py migrate
  python3 manage.py collectstatic
  python3 manage.py migrate --run-syncdb
  


Develop
  docker-compose down -v
  docker-compose up -d --build
  docker-compose exec web python manage.py migrate --noinput
  docker-compose exec web python manage.py collectstatic --no-input --clear


Production
  docker-compose -f docker-compose.prod.yml down -v
  docker-compose -f docker-compose.prod.yml up -d --build
  docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
  docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
  docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser



  next
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py collectstatic
    python3 manage.py createsuperuser