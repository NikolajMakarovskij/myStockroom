from django.apps import AppConfig


class SoftwareConfig(AppConfig):
    """_SignatureConfig_
    The application is designed to maintain a list of software on devices
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "software"
    verbose_name = "Программное обеспечение"
