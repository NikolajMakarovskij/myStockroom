from django.conf import settings
from consumables.models import cartridge, accumulator, fotoval, toner


class Stock(object):

    def __init__(self, request):
        """
        Инициализируем склад
        """
        self.session = request.session
        stock = self.session.get(settings.STOCK_SESSION_ID)
        if not stock:
            # save an empty cart in the session
            stock = self.session[settings.STOCK_SESSION_ID] = {}
        self.stock = stock

    def add(self, cartridge, quantity=1, update_quantity=False):
        """
        Добавить продукт на склад или обновить его количество.
        """
        cartridge_id = str(cartridge.id)
        if cartridge_id not in self.stock:
            self.stock[cartridge_id] = {'quantity': 0 }
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
        # получение объектов product и добавление их в корзину
        cartridges = cartridge.objects.filter(id__in=cartridge_ids)
        for cartridge in cartridges:
            self.stock[str(cartridge.id)]['cartridge'] = cartridge

    def __len__(self):
        """
        Подсчет всех расходников на складе.
        """
        return sum(item['quantity'] for item in self.stock.values())