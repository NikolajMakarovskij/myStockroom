import datetime
from django.conf import settings
from consumables.models import Consumables 
from .models import Stockroom,Categories

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
            #category = Categories.objects.create(
            #                                    name =  Consumables.objects.filter(id = consumable_id).get(categories.name),
            #                                    slug =  Consumables.objects.filter(id = consumable_id).get(categories.slug)
            #)
            Stockroom.objects.create(
                                    consumables = consumable_add,
            #                        categories = category,
                                    dateAddToStock = datetime.date.today(),
                                    #dateInstall = datetime.date.today()
            )
            Consumables.objects.filter(id = consumable_id).update(
                                                            score=int(quantity),
                                                            rack=int(number_rack),
                                                            shelf=int(number_shelf)
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
        if Stockroom.objects.filter(consumables = consumable_id):
            Stockroom.objects.filter(consumables = consumable_id).delete()
            self.save()

    def device_add_consumable(self, consumable, quantity=1, update_quantity=False):
        """
        Уменьшает количество картриджей
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