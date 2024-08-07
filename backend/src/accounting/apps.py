from django.apps import AppConfig


class AccountingConfig(AppConfig):
    """_AccountingConfig_:
    The app is designed to account for consumables and components listed on the company's balance sheet

    Args:
        AppConfig (AppConfig): _description_
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounting"
    verbose_name = "Баланс"
