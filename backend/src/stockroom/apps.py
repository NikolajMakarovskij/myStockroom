from django.apps import AppConfig


class StockroomConfig(AppConfig):
    """_StockroomConfig_
    The application is designed to maintain a list of consumables, components in equipment and equipment stored in a warehouse
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "stockroom"
    verbose_name = "Склад"
