from django.conf import settings
from consumables.models import Cartridge

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

    def add(self, cartridge, quantity=1, update_quantity=False):
        """
        Добавить продукт на склад или обновить его количество.
        """
        cartridge_id = str(cartridge.id)
        cartridge_score = int(cartridge.score)
        if cartridge_id not in self.stock:
            self.stock[cartridge_id] = {'quantity': cartridge_score }
        if update_quantity:
            self.stock[cartridge_id]['quantity'] = quantity
        else:
            self.stock[cartridge_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.STOCK_SESSION_ID] = self.stock
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, cartridge):
        """
        Удаление расходника со склада
        """
        cartridge_id = str(cartridge.id)
        if cartridge_id in self.stock:
            del self.stock[cartridge_id]
            self.save()

    def __iter__(self):
        """
        Перебор элементов на складе и получение расходников из базы данных.
        """
        cartridge_ids = self.stock.keys()
        # получение объектов на склад и добавление их в корзину
        cartridges = Cartridge.objects.filter(id__in=cartridge_ids)
        for cartridge in cartridges:
            self.stock[str(cartridge.id)]['cartridge'] = cartridge
        for item in self.stock.values():
            yield item

    def __len__(self):
        """
        Подсчет всех расходников на складе.
        """
        return sum(item['quantity'] for item in self.stock.values())