# ***Get Starting***

## Requirements before installation

### Additional Software

1. To deploy the program, you will need pre-installed:
    * Docker и Docker compose

    or

    * Docker desktop

2. The installation of Docker can be found at [link](
https://docs.docker.com/engine/).

3. The installation of Docker compose can be found at [link](
https://docs.docker.com/compose/).

4. The installation of Docker desktop can be found at [link](
https://docs.docker.com/get-docker/).

### Setting up Environment variables

1. In the folder ***backend/database/Init_db/*** there is a test database to demonstrate the operation of the program. If you do not need a test database, delete the ***init.sql*** file from the folder;
2. In the ***backend/*** folder, open the ***.env*** file. The values of the variables are shown in the table below:

### Environment variables

|                        Variable | Description                                                                                                             |
|--------------------------------:|-------------------------------------------------------------------------------------------------------------------------|
|                      DEBUG, DEV | Enables debugging mode. Install ***0*** to disable it. To enable it, set ***1***                                        |
|                             SSR | Server-Side Rendering. Install ***0*** to disable it. To enable it, set ***1***                                         |
|                      SECRET_KEY | The key for the cryptographic signature                                                                                 |
|            DJANGO_ALLOWED_HOSTS | Allowed hosts. Specify the list of hosts separated by commas                                                            |
|                   VITE_BASE_URL | Base Server address                                                                                                     |
|                      SQL_ENGINE | When using PostgreSQL, specify ***django.db.backends.postgresql***. It is recommended not to change                     |
|       SQL_DATABASE, POSTGRES_DB | The name of the database. Must match                                                                                    |
|         SQL_USER, POSTGRES_USER | The name of the DB user. Must match                                                                                     |
| SQL_PASSWORD, POSTGRES_PASSWORD | The name of the database user. Must match                                                                               |
|                        SQL_HOST | The name of the database host. It is recommended to leave ***db***                                                      |
|                        SQL_PORT | The database port. It is recommended to leave ***5432***                                                                |
|              SQL_PGDATA, PGDATA | The location of the database inside the container. It is recommended to leave ***/var/lib/postgresql/data/pgdata***     |
|       POSTGRES_HOST_AUTH_METHOD | It is recommended to leave ***trust***                                                                                  |
|                   CELERY_BROKER | Celery broker server settings. It is recommended to leave ***redis://redis:6379/0***                                    |
|                  CELERY_BACKEND | Celery server settings. It is recommended to leave ***redis://redis:6379/0***                                           |

### Installation

1. After setting up the environment variables, open the ***backend folder in the terminal/***;
2. Enter the command:

    ```
    docker-compose up --build
    ```

3. Wait for the containers to be assembled and launched;
4. After starting the containers, open a new console window;
5. To create a superuser, enter:

    ```
    docker exec -it container_name python3 manage.py createsuperuser
    ```

6. Go to [0.0.0.0/](http://0.0.0.0/) or [localhost/home/](http://localhost/);
7. Log in with the data specified in clause 5.

`If the program was deployed from a test database, the user will be available: login: admin password: admin.`

8. Backup

    ```
    docker exec container_name pg_dump -U SQL_USER -W SQL_DATABASE > init_db_$(date +\%Y-\%m-\%d).sql
    ```
