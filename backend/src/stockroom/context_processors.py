from stockroom.stock.base_stock import BaseStock


def stock(request):
    return {"stock": BaseStock(request)}
