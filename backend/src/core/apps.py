from django.apps import AppConfig


class CoreConfig(AppConfig):
    """_CoreConfig_  
    The app is the core of the Warehouse. Designed for common configurations for all apps and home page
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
    verbose_name = "core"
