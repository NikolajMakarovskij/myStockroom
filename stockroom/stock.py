from django.conf import settings
from consumables.models import Consumables 

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

    def add_consumable(self, consumable, quantity=1, number_rack=1, number_shelf=1, update_quantity=False):
        """
        Добавить картридж на склад или обновить его количество.
        """
        consumable_id = str(consumable.id)
        consumable_score = str(consumable.score)
        consumable_rack = str(consumable.rack)
        consumable_shelf = str(consumable.shelf)

        if consumable_id not in self.stock:
           self.stock[consumable_id] = {'quantity': consumable_score, 'number_rack': consumable_rack,'number_shelf': consumable_shelf }
        if update_quantity:
            self.stock[consumable_id]['quantity'] = quantity
        else:
            self.stock[consumable_id]['quantity'] += quantity
            self.stock[consumable_id]['number_rack'] = number_rack
            self.stock[consumable_id]['number_shelf'] = number_shelf
        Consumables.objects.filter(id = consumable_id).update(
                                                            score=self.stock[consumable_id]['quantity'],
                                                            rack=self.stock[consumable_id]['number_rack'],
                                                            shelf=self.stock[consumable_id]['number_shelf']
                                                            )
        self.save()

    def save(self):
        # Обновление сессии 
        self.session[settings.STOCK_SESSION_ID] = self.stock
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove_consumable(self, consumable):
        """
        Удаление картриджа со склада
        """
        consumable_id = str(consumable.id)
        if consumable_id in self.stock:
            del self.stock[consumable_id]
            self.save()

    def printer_install_consumable(self, consumable, quantity=1, update_quantity=False):
        """
        Уменьшает количество картриджей
        """
        consumable_id = str(consumable.id)
        consumable_score = int(consumable.score)

        if consumable_id not in self.stock:
            self.stock[consumable_id] = {'quantity': consumable_score,}
        if update_quantity:
            self.stock[consumable_id]['quantity'] = quantity
        else:
            self.stock[consumable_id]['quantity'] -= quantity
        Consumables.objects.filter(id = consumable_id).update(score=self.stock[consumable_id]['quantity'])
        self.save()

    def __iter__(self):
        """
        Перебор элементов на складе и получение расходников из базы данных.
        """
        stock_ids = self.stock.keys()
        # получение расходника со склада 
        consumables = Consumables.objects.filter(id__in=stock_ids)
        for consumable in consumables:
            self.stock[str(consumable.id)]['consumable'] = consumables

        for item in self.stock.values():
            yield item

    def __len__(self):
        """
        Подсчет всех расходников на складе.
        """
        return sum(item['quantity'] for item in self.stock.values())