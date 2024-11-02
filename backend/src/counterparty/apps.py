from django.apps import AppConfig


class CounterpartyConfig(AppConfig):
    """_CounterpartyConfig_ The application is designed to maintain a list of contractors and manufacturers
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "counterparty"
    verbose_name = "Контрагенты"
