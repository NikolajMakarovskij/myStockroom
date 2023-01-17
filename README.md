# myStockroom

## Разворачивание в docker-compose для разработки
  1. Открыть папку проекта в терминале  
    - ввести команды по очереди:
      ```
      docker-compose up -d --build
      ```  
      ```
      docker-compose exec web python3 manage.py migrate --noinput
      ```
      ```
      docker-compose exec web python3 manage.py collectstatic --no-input --clear
      ```
      ```
      docker-compose exec web python3 manage.py createsuperuser
      ```
  
  2. Если миграции не сработали из терминала, то открыть терминал контейнера web
    - ввести команды по очереди:
      ```python
          python3 manage.py makemigrations
          python3 manage.py migrate
          python3 manage.py collectstatic
          python3 manage.py createsuperuser
      ```

## Разворачивание в docker-compose для деплоя 
<details><summary>Команды</summary>
<p>

```
  docker-compose -f docker-compose.prod.yml down -v
```
```
  docker-compose -f docker-compose.prod.yml up -d --build
```
```
  docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
```
```
  docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```
```
  docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
```

</p>
</details>

## Удалить все контейнеры  </summary>
<details><summary>Команды</summary>
<p>

  - разработка
      ```
        docker-compose down -v
      ```
  - деплой
      ```
        docker-compose -f docker-compose.prod.yml down -v
      ```

</p>
</details>

## В разработке

- [X] https://github.com/NikolajMakarovskij/myStockroom/issues/6#issue-1536290556
- [ ] https://github.com/NikolajMakarovskij/myStockroom/issues/7#issue-1536290939
- [ ] https://github.com/NikolajMakarovskij/myStockroom/issues/8#issue-1536291827
- [ ] https://github.com/NikolajMakarovskij/myStockroom/issues/9#issue-1536291919
- [ ] https://github.com/NikolajMakarovskij/myStockroom/issues/10#issue-1536292001
    