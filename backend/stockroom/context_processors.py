from .stock import Stock


def stock(request):
    return {'stock': Stock(request)}
