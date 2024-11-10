from stockroom.stock.base_stock import BaseStock


def stock(request):  # TODO Figure out what it was added for and delete it
    """_Context processor for the Base_stock module_

    DO NOT DELETE IT. IT DOESN'T WORK WITHOUT IT!

    Args:
        request (request): _description_

    Returns:
        stock (BaseStock): _description_
    """
    return {"stock": BaseStock(request)}
