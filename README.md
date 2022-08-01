# myBase1
activation env
  source env/bin/activate
  python3 manage.py runserver

docker up
  docker-compose up -d --build
  
authorization
  user: "admin"
  password: "admin"
  
  if notworking
    python3 manage.py createsuperuser
  
  
migrate database
  python3 manage.py makemigrations
  python3 manage.py migrate
