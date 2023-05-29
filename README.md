# myStockroom

## Разворачивание в docker-compose для разработки
  1. Открыть папку проекта в терминале  
    - ввести команды по очереди:
      ```
      docker-compose up -d --build
      ```  
      ```
      docker-compose exec web python3 manage.py collectstatic --no-input --clear
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
  docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
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

## Домашка
  https://habr.com/ru/articles/713490/

## В разработке

 - [X] Рефакторинг старого проекта https://github.com/NikolajMakarovskij/myStockroom/issues/6
 - [ ] Склад https://github.com/NikolajMakarovskij/myStockroom/issues/7
 - [ ] Таски для обработки логики склада https://github.com/NikolajMakarovskij/myStockroom/issues/8
 - [ ] Таски для приложения ЭЦП https://github.com/NikolajMakarovskij/myStockroom/issues/9
 - [ ] Docker-compose для деплоя https://github.com/NikolajMakarovskij/myStockroom/issues/10
 - [ ] добавление расходников на склад [#14](https://github.com/NikolajMakarovskij/myStockroom/issues/14)
 - [ ] добавить форму установки картриджа в принтер с автоматическим списанием со склада [#13](https://github.com/NikolajMakarovskij/myStockroom/issues/13)
 - [ ] добавить лог для склада [#15](https://github.com/NikolajMakarovskij/myStockroom/issues/15)
    
