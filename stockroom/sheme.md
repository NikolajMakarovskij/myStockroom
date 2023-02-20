# Логика склада

## Модели склада, расходника и устройства
    - Склад
    '''
    python
    class Stockroom (ModelMixin, models.Model):
        consumables = models.OneToOneField(Consumables, primary_key = True)
        categories = models.ForeignKey('Categories')
        dateAddToStock = models.DateField(verbose_name="Дата поступления на склад")
        dateInstall = models.DateField(verbose_name="Дата установки")
        rack = models.IntegerField(verbose_name="Стеллаж" )
        shelf = models.IntegerField(verbose_name="Полка")
        mileage #TODO рассмотреть добавление
    '''
    - Расходник
    '''
    python
    class Consumables (ModelMixin, models.Model):
        """
        Модель расходников
        """
        id = models.UUIDField(primary_key=True)
        name = models.CharField(verbose_name="Название")
        categories = models.ForeignKey('Categories', verbose_name="группа")
        serial = models.CharField(verbose_name="Серийный номер")
        invent = models.CharField(verbose_name="Инвентарный номер"            )
        manufacturer = models.ForeignKey(Manufacturer, verbose_name="Производитель")
        buhCode = models.CharField(verbose_name="Код в бухгалтерии")
        score = models.IntegerField(verbose_name="Остаток на складе")
        mileage #TODO рассмотреть добавление
    '''
    - Пример устройства
    '''
    python
    class Printer (ModelMixin, models.Model):
        """
        Модель принтера. Рассмотреть объединение всех устройств в единую модель
        """
        id = models.UUIDField(primary_key=True,)
        name = models.CharField(verbose_name="Название")
        manufacturer = models.ForeignKey(Manufacturer, verbose_name="Производитель")
        serial = models.CharField(verbose_name="Серийный номер")
        invent = models.CharField(verbose_name="Инвентарный номер")
        workplace = models.ForeignKey(Workplace, verbose_name="Рабочее место")
        cartridge = models.ForeignKey(Consumables, verbose_name="Картридж")
        fotoval = models.ForeignKey(Consumables, verbose_name="Фотовал")
        toner = models.ForeignKey(Consumables, verbose_name="Тонер")
        fotodrumm = models.ForeignKey(Consumables, verbose_name="Фотобарабан")
        score = models.IntegerField(verbose_name="Остаток на складе")
        mileage #TODO рассмотреть добавление
    '''

## Методы склада

    - Добавление расходника на склад
    '''
    python
        def add_consumable(self, consumable, quantity=1, number_rack=1, number_shelf=1, mileage=0  update_quantity=False):
            """
            Добавить на склад или обновить его количество.
            """
            consumable_id = str(consumable.id)
            consumable_score = int(str(consumable.score))
            consumable_add = Consumables.objects.get(id = consumable_id)

            if Stockroom.objects.filter(consumables = consumable_id):
                consumable_score += quantity 
                Consumables.objects.filter(id = consumable_id).update(
                                                                score = consumable_score
                                                                )
                Stockroom.objects.filter(consumables = consumable_id).update(
                                                                        dateAddToStock = datetime.date.today()
                )
            else:
                Stockroom.objects.create(
                                        consumables = consumable_add,
                                        dateAddToStock = datetime.date.today(),
                                        rack=int(number_rack),
                                        shelf=int(number_shelf)
                )
                Consumables.objects.filter(id = consumable_id).update(
                                                                score=int(quantity),
                                                                )
                #TODO Рассмотреть необходимость реализации
                Variable_model.objects.filter(id = consumable_id).update(
                                                                mileage=int(mileage),
                                                                )                                                
            self.save()
    '''

    - Установка расходника в устройство
    '''
    python
        def device_add_consumable(self, consumable, quantity=1, mileage=0 update_quantity=False):
            """
            Установка расходника в устройство
            """
            consumable_id = str(consumable.id)
            consumable_score = int(str(consumable.score))
            consumable_score -= quantity 
            Consumables.objects.filter(id = consumable_id).update(
                                                            score = consumable_score
                                                                )
            Stockroom.objects.filter(consumables = consumable_id).update(
                                                                    dateInstall = datetime.date.today()
                )
            #TODO реализовать обновление пробега при установке нового расходника
            Variable_model.objects.filter(id = consumable_id).update(
                                                                mileage += int(mileage), #реализовать обновление пробега при установке нового расходника
                                                                ) 
            self.sav
    '''