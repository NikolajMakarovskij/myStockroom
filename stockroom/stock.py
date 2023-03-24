import datetime
from django.conf import settings
from consumables.models import Consumables 
from .models import Stockroom, Categories, History


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

    def add_category(consumable_id):
        """Получение категории из расходников"""
        consumable_category = Consumables.objects.get(id = consumable_id).categories.name
        if Categories.objects.filter(name=consumable_category):
            consumable_category = Categories.objects.get(name=consumable_category)
        else:
            consumable_category = Categories.objects.create(
                name=Consumables.objects.get(id = consumable_id).categories.name,
                slug=Consumables.objects.get(id = consumable_id).categories.slug
                )
        return consumable_category

    def create_history(consumable_id, quantity, username, status_choise):
        history = History.objects.create(
            consumable=Consumables.objects.get(id = consumable_id).name, 
            consumableId=Consumables.objects.get(id = consumable_id).id, 
            score = quantity,
            dateInstall = datetime.date.today(),
            categories = Stock.add_category(consumable_id),
            user = username,
            status = status_choise
        )
        return history

    def get_printer(consumable_id):
        """Получение принтера"""
        printer = Consumables.objects.get(id=consumable_id).printer.all()
        return printer


    def add_consumable(self, consumable, quantity=1, number_rack=1, number_shelf=1, username=None):
        """
        Добавить расходник на склад или обновить его количество.
        """
        consumable_id = str(consumable.id)
        consumable_score = int(str(consumable.score))
        consumable_add = Consumables.objects.get(id = consumable_id)
        if Stockroom.objects.filter(consumables = consumable_id):
            consumable_score += quantity 
            Consumables.objects.filter(id = consumable_id).update(score = consumable_score)
            Stockroom.objects.filter(consumables = consumable_id).update(
                dateAddToStock = datetime.date.today(),
                #printer = Stock.get_printer(consumable_id)
            )
        else:
            Stockroom.objects.create(
                                    consumables = consumable_add,
                                    categories = Stock.add_category(consumable_id),
                                    dateAddToStock = datetime.date.today(),
                                    rack=int(number_rack),
                                    shelf=int(number_shelf),
                                    #printer = Stock.get_printer(consumable_id)
            )
            Consumables.objects.filter(id = consumable_id).update(score = int(quantity))
        Stock.create_history(consumable_id, quantity, username, status_choise='Приход')
        self.save()

    def save(self):
        # Обновление сессии 
        self.session[settings.STOCK_SESSION_ID] = self.stock
        self.session.modified = True

    def remove_consumable(self, consumable, quantity=0, username=None):
        """
        Удаление картриджа со склада
        """
        consumable_id = str(consumable.id)
        if Stockroom.objects.filter(consumables = consumable_id):
            Stockroom.objects.filter(consumables = consumable_id).delete()
            Stock.create_history(consumable_id, quantity, username, status_choise='Удаление')
        self.save()

    def device_add_consumable(self, consumable, quantity=1, username=None):
        """
        Установка расходника в устройство
        """
        consumable_id = str(consumable.id)
        consumable_score = int(str(consumable.score))
        consumable_score -= quantity 

        Consumables.objects.filter(id = consumable_id).update(score = consumable_score)
        Stockroom.objects.filter(consumables = consumable_id).update(dateInstall = datetime.date.today())
        Stock.create_history(consumable_id, quantity, username, status_choise='Расход')

        self.save()
