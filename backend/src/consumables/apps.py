from django.apps import AppConfig


class ConsumablesConfig(AppConfig):
    """_ConsumablesConfig_
    The application is designed to maintain a list of used consumables and components in the equipment of the enterprise
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "consumables"
    verbose_name = "Расходники"
