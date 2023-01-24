from django.conf import settings
from consumables.models import Cartridge, Toner, Fotoval, Accumulator, Storage

class Stock(object):

    def __init__(self, request):
        """
        Инициализируем склад
        """
        self.session = request.session
        stock = self.session.get(settings.STOCK_SESSION_ID)
        if not stock:
            # Сохранение пустого склада
            stock = self.session[settings.STOCK_SESSION_ID] = {}
        self.stock = stock

    def add_cartridge(self, cartridge, quantity=1, number_rack=1, number_shelf=1, update_quantity=False):
        """
        Добавить картридж на склад или обновить его количество.
        """
        cartridge_id = str(cartridge.id)
        cartridge_score = int(cartridge.score)
        cartridge_rack = int(cartridge.rack)
        cartridge_shelf = int(cartridge.shelf)

        if cartridge_id not in self.stock:
            self.stock[cartridge_id] = {'quantity': cartridge_score,'number_rack': cartridge_rack,'number_shelf': cartridge_shelf }
        if update_quantity:
            self.stock[cartridge_id]['quantity'] = quantity
        else:
            self.stock[cartridge_id]['quantity'] += quantity
            self.stock[cartridge_id]['number_rack'] = number_rack
            self.stock[cartridge_id]['number_shelf'] = number_shelf
        Cartridge.objects.filter(id = cartridge_id).update(
                                                            score=self.stock[cartridge_id]['quantity'],
                                                            rack=self.stock[cartridge_id]['number_rack'],
                                                            shelf=self.stock[cartridge_id]['number_shelf']
                                                            )
        self.save()

    def add_toner(self, toner, quantity=1, number_rack=1, number_shelf=1, update_quantity=False):
        """
        Добавить тонер на склад или обновить его количество.
        """
        toner_id = str(toner.id)
        toner_score = int(toner.score)
        toner_rack = int(toner.rack)
        toner_shelf = int(toner.shelf)

        if  toner_id not in self.stock:
            self.stock[toner_id] = {'quantity':toner_score,'number_rack': toner_rack,'number_shelf': toner_shelf}
        if update_quantity:
            self.stock[toner_id]['quantity'] = quantity
        else:
            self.stock[toner_id]['quantity'] += quantity
            self.stock[toner_id]['number_rack'] = number_rack
            self.stock[toner_id]['number_shelf'] = number_shelf
        Toner.objects.filter(id = toner_id).update(
                                                            score=self.stock[toner_id]['quantity'],
                                                            rack=self.stock[toner_id]['number_rack'],
                                                            shelf=self.stock[toner_id]['number_shelf']
                                                            )
        self.save()

    def add_fotoval(self, fotoval, quantity=1, number_rack=1, number_shelf=1, update_quantity=False):
        """
        Добавить фотовал на склад или обновить его количество.
        """
        fotoval_id = str(fotoval.id)
        fotoval_score = int(fotoval.score)
        fotoval_rack = int(fotoval.rack)
        fotoval_shelf = int(fotoval.shelf)

        if  fotoval_id not in self.stock:
            self.stock[fotoval_id] = {'quantity':fotoval_score,'number_rack': fotoval_rack,'number_shelf': fotoval_shelf}
        if update_quantity:
            self.stock[fotoval_id]['quantity'] = quantity
        else:
            self.stock[fotoval_id]['quantity'] += quantity
            self.stock[fotoval_id]['number_rack'] = number_rack
            self.stock[fotoval_id]['number_shelf'] = number_shelf
        Fotoval.objects.filter(id = fotoval_id).update(
                                                            score=self.stock[fotoval_id]['quantity'],
                                                            rack=self.stock[fotoval_id]['number_rack'],
                                                            shelf=self.stock[fotoval_id]['number_shelf']
                                                            )
        self.save()

    def add_accumulator(self, accumulator, quantity=1, number_rack=1, number_shelf=1, update_quantity=False):
        """
        Добавить аккумулятор на склад или обновить его количество.
        """
        accumulator_id = str(accumulator.id)
        accumulator_score = int(accumulator.score)
        accumulator_rack = int(accumulator.rack)
        accumulator_shelf = int(accumulator.shelf)

        if  accumulator_id not in self.stock:
            self.stock[accumulator_id] = {'quantity':accumulator_score,'number_rack': accumulator_rack,'number_shelf': accumulator_shelf}
        if update_quantity:
            self.stock[accumulator_id]['quantity'] = quantity
        else:
            self.stock[accumulator_id]['quantity'] += quantity
            self.stock[accumulator_id]['number_rack'] = number_rack
            self.stock[accumulator_id]['number_shelf'] = number_shelf
        Accumulator.objects.filter(id = accumulator_id).update(
                                                            score=self.stock[accumulator_id]['quantity'],
                                                            rack=self.stock[accumulator_id]['number_rack'],
                                                            shelf=self.stock[accumulator_id]['number_shelf']
                                                            )
        self.save()

    def add_storage(self, storage, quantity=1, number_rack=1, number_shelf=1, update_quantity=False):
        """
        Добавить накопитель на склад или обновить его количество.
        """
        storage_id = str(storage.id)
        storage_score = int(storage.score)
        storage_rack = int(storage.rack)
        storage_shelf = int(storage.shelf)

        if  storage_id not in self.stock:
            self.stock[storage_id] = {'quantity':storage_score,'number_rack': storage_rack,'number_shelf': storage_shelf}
        if update_quantity:
            self.stock[storage_id]['quantity'] = quantity
        else:
            self.stock[storage_id]['quantity'] += quantity
            self.stock[storage_id]['number_rack'] = number_rack
            self.stock[storage_id]['number_shelf'] = number_shelf
        Storage.objects.filter(id = storage_id).update(
                                                            score=self.stock[storage_id]['quantity'],
                                                            rack=self.stock[storage_id]['number_rack'],
                                                            shelf=self.stock[storage_id]['number_shelf']
                                                            )
        self.save()

    def save(self):
        # Обновление сессии 
        self.session[settings.STOCK_SESSION_ID] = self.stock
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove_cartrige(self, cartridge):
        """
        Удаление картриджа со склада
        """
        cartridge_id = str(cartridge.id)
        if cartridge_id in self.stock:
            del self.stock[cartridge_id]
            self.save()

    def remove_toner(self, toner):
        """
        Удаление тонера со склада
        """
        toner_id = str(toner.id)
        if toner_id in self.stock:
            del self.stock[toner_id]
            self.save()

    def remove_fotoval(self, fotoval): 
        """
        Удаление фотовала со склада
        """
        fotoval_id = str(fotoval.id)
        if fotoval_id in self.stock:
            del self.stock[fotoval_id]
            self.save()

    def remove_accumulator(self, accumulator): 
        """
        Удаление аккумуляторы со склада
        """
        accumulator_id = str(accumulator.id)
        if accumulator_id in self.stock:
            del self.stock[accumulator_id]
            self.save()

    def remove_storage(self, storage): 
        """
        Удаление накопителя со склада
        """
        storage_id = str(storage.id)
        if storage_id in self.stock:
            del self.stock[storage_id]
            self.save()

    def printer_install_cartridge(self, cartridge, quantity=1, update_quantity=False):
        """
        Уменьшает количество картриджей
        """
        cartridge_id = str(cartridge.id)
        cartridge_score = int(cartridge.score)

        if cartridge_id not in self.stock:
            self.stock[cartridge_id] = {'quantity': cartridge_score,}
        if update_quantity:
            self.stock[cartridge_id]['quantity'] = quantity
        else:
            self.stock[cartridge_id]['quantity'] -= quantity
        Cartridge.objects.filter(id = cartridge_id).update(score=self.stock[cartridge_id]['quantity'])
        self.save()


    def printer_install_toner(self, toner, quantity=1, update_quantity=False):
        """
        Уменьшает количество тонера
        """
        toner_id = str(toner.id)
        toner_score = int(toner.score)

        if toner_id not in self.stock:
            self.stock[toner_id] = {'quantity': toner_score,}
        if update_quantity:
            self.stock[toner_id]['quantity'] = quantity
        else:
            self.stock[toner_id]['quantity'] -= quantity
        Toner.objects.filter(id = toner_id).update(score=self.stock[toner_id]['quantity'])
        self.save()


    def printer_install_fotoval(self, fotoval, quantity=1, update_quantity=False):
        """
        Уменьшает количество фотовалов
        """
        fotoval_id = str(fotoval.id)
        fotoval_score = int(fotoval.score)

        if fotoval_id not in self.stock:
            self.stock[fotoval_id] = {'quantity': fotoval_score,}
        if update_quantity:
            self.stock[fotoval_id]['quantity'] = quantity
        else:
            self.stock[fotoval_id]['quantity'] -= quantity
        Fotoval.objects.filter(id = fotoval_id).update(score=self.stock[fotoval_id]['quantity'])
        self.save()


    def ups_install_accumulator(self, accumulator, quantity=1, update_quantity=False):
        """
        Уменьшает количество аккумуляторов
        """
        accumulator_id = str(accumulator.id)
        accumulator_score = int(accumulator.score)

        if accumulator_id not in self.stock:
            self.stock[accumulator_id] = {'quantity': accumulator_score,}
        if update_quantity:
            self.stock[accumulator_id]['quantity'] = quantity
        else:
            self.stock[accumulator_id]['quantity'] -= quantity
        Accumulator.objects.filter(id = accumulator_id).update(score=self.stock[accumulator_id]['quantity'])
        self.save()


    def install_storage(self, storage, quantity=1, update_quantity=False):
        """
        Уменьшает количество накопителей
        """
        storage_id = str(storage.id)
        storage_score = int(storage.score)

        if storage_id not in self.stock:
            self.stock[storage_id] = {'quantity': storage_score,}
        if update_quantity:
            self.stock[storage_id]['quantity'] = quantity
        else:
            self.stock[storage_id]['quantity'] -= quantity
        Storage.objects.filter(id = storage_id).update(score=self.stock[storage_id]['quantity'])
        self.save()

    def __iter__(self):
        """
        Перебор элементов на складе и получение расходников из базы данных.
        """
        stock_ids = self.stock.keys()
        # получение картриджей со склада 
        cartridges = Cartridge.objects.filter(id__in=stock_ids)
        for cartridge in cartridges:
            self.stock[str(cartridge.id)]['cartridge'] = cartridge
        # получение тонера со склада 
        toners = Toner.objects.filter(id__in=stock_ids)
        for toner in toners:
            self.stock[str(toner.id)]['toner'] = toner
        # получение фотовала со склада 
        fotovals = Fotoval.objects.filter(id__in=stock_ids)
        for fotoval in fotovals:
            self.stock[str(fotoval.id)]['fotoval'] = fotoval
        # получение аккумулятора со склада 
        accumulators = Accumulator.objects.filter(id__in=stock_ids)
        for accumulator in accumulators:
            self.stock[str(accumulator.id)]['accumulator'] = accumulator
        # получение накопителя со склада 
        storages = Storage.objects.filter(id__in=stock_ids)
        for storage in storages:
            self.stock[str(storage.id)]['storage'] = storage
        for item in self.stock.values():
            yield item

    def __len__(self):
        """
        Подсчет всех расходников на складе.
        """
        return sum(item['quantity'] for item in self.stock.values())