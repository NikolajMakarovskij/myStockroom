import datetime
from django.conf import settings
from consumables.models import Consumables 
from .models import Stockroom, Categories

class Stock(object):

    def __init__(self, request):
        """
        Инициализирует склад
        """
        self.session = request.session
        stock = self.session.get(settings.STOCK_SESSION_ID)
        if not stock:
            # Сохранение пустого склада
            stock = self.session[settings.STOCK_SESSION_ID] = {}
        self.stock = stock

    def add_consumable(self, consumable, quantity=1, number_rack=1, number_shelf=1, update_quantity=False):
        """
        Добавить расходник на склад или обновить его количество.
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
                                    rack=int(number_rack),
                                    shelf=int(number_shelf)
            )
            Consumables.objects.filter(id = consumable_id).update(
                                                            score=int(quantity),
                                                            )
        self.save()

    def save(self):
        # Обновление сессии 
        self.session[settings.STOCK_SESSION_ID] = self.stock
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
        self.save()
