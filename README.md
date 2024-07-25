# **Склад**

##### Основной репозиторий [https://gitlab.com/NikolajMakarovskij/stockroom](https://gitlab.com/NikolajMakarovskij/stockroom)
##### Зеркало [https://github.com/NikolajMakarovskij/myStockroom](https://github.com/NikolajMakarovskij/myStockroom)

___
## О программе
<details>
<summary> Описание </summary>

`Данная программа позволяет задать расстановку техники в помещениях, указать установленные в технику комплектующие 
и расходники, вести историю замены комплектующих. Позволяет добавлять, списывать и утилизировать на(со) склад(а).
В разаделе "На балансе" указываются как числяться расходники и комплектующие в бухгалтерии.
Функционал разделов с программным обеспечением и цифровыми подписями
находится в разработке`

`Доступ в программу осуществляется через браузер во внутренней локальной сети. Присутствует система авторизации, панель администратора,
система прав доступа к разделам`

`Программа написана с помощью фреймворка Django (v 4) на python 3.8. В качестве базы данных используется
PostgreSQL (v. 14). для запуска и развертывания программы используется Doсker`

</details>

___
## Требования перед установкой

<details>
<summary> Дополнительное ПО </summary>

1. Для развертывания программы потребуются предварительно установленные: 
    * [Docker](https://docs.docker.com/engine/) и [Docker compose](https://docs.docker.com/compose/)
    или
    * [Docker desktop](https://docs.docker.com/get-docker/)
   
</details>

___
## Развертывание

<details>
<summary>Настройка переменных окружения</summary>

1. В папке ***backend/database/Init_db/*** расположена тестовая база данных для демонстрации работы Программы. Если вам не нужна тестовая база, удалите файл ***init.sql*** из папки;
2. В папке ***backend/*** откройте файл ***.env***. Значения переменных указаны в таблице ниже:
<details><summary>Переменные окружения</summary>

|                      Переменная | Описание                                                                                            |
|--------------------------------:|-----------------------------------------------------------------------------------------------------|
|                           DEBUG | Включает режим отладки. Установите ***0***, чтобы отключить. Для включения установите ***1***       |
|                      SECRET_KEY | Ключ для криптографической подписи                                                                  |
|            DJANGO_ALLOWED_HOSTS | Разрешенные хосты. Укажите список хостов через запятую ***                                          |
|                      SQL_ENGINE | При использовании PostgreSQL укажите ***django.db.backends.postgresql***. Рекомендуется не изменять |
|       SQL_DATABASE, POSTGRES_DB | Имя БД. Должны совпадать                                                                            |
|         SQL_USER, POSTGRES_USER | Имя пользователя БД. Должны совпадать                                                               |
| SQL_PASSWORD, POSTGRES_PASSWORD | Пароль пользователя БД. Должны совпадать                                                            |
|                        SQL_HOST | Имя хоста БД. Рекомендуется оставить ***db***                                                       |
|                        SQL_PORT | Порт БД. Рекомендуется оставить ***5432***                                                          |
|              SQL_PGDATA, PGDATA | Расположение БД внутри контейнера. Рекомендуется оставить ***"/var/lib/postgresql/data/pgdata"***   |
|       POSTGRES_HOST_AUTH_METHOD | Рекомендуется оставить ***trust***                                                                  |
|                   CELERY_BROKER | Настройки сервера брокера Celery. Рекомендуется оставить ***redis://redis:6379/0***                 |
|                  CELERY_BACKEND | Настройки сервера Celery. Рекомендуется оставить ***redis://redis:6379/0***                         |
</details>
</details>
<details><summary>Установка</summary>

1. После настройки переменных окружения откройте в терминале папку ***backend/***;
2. Введите команду: 
    ```bash
    docker-compose up --build
    ```
3. Дождитесь сборки и запуска контейнеров;
4. После запуска контейнеров откройте новое окно консоли;
5. Для создания суперпользователя введите: 
    <pre>
        ```bash
        docker exec -it  <a href="docker-compose.yaml?plain=1#L5">container_name</a> python3 manage.py createsuperuser
        ```
    </pre>
6. Перейдите по адресу [0.0.0.0/home/](http://0.0.0.0/home/) или [localhost/home/](http://localhost/home/);
7. Авторизуйтесь с данными указанными в п. 5. 
`Если программа разворачивалась с тестовой БД, будет доступен пользователь: login: admin password: admin`.
8. Бэкап
    <pre>
        ```bash
        docker exec <a href="docker-compose.yaml?plain=1#L39">container_name</a> pg_dump -U <a href=".env?plain=1#L6">SQL_USER</a> -W <a href=".env?plain=1#L5">SQL_DATABASE </a> > init_db_$(date +\%Y-\%m-\%d).sql 
        ```
    </pre>
</details>

___
## В разработке

<details>
<summary> Разработка </summary>

1. REST API на основе Django rest api;
2. frontend на основе React;
3. раздел "Программное обеспечение";
4. раздел "Цифровые подписи".

</details>
