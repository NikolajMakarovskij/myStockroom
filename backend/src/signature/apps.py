from django.apps import AppConfig


class SignatureConfig(AppConfig):
    """_SignatureConfig_
    The application is designed to maintain a list of EDS from users
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "signature"
    verbose_name = "ЭЦП"
