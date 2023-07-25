from .stock import BaseStock


def stock(request):
    return {'stock': BaseStock(request)}
