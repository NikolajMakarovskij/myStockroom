from django.apps import AppConfig


class DecommissionConfig(AppConfig):
    """_Decommission_
    The application is designed to maintain a list of decommissioning and disposal devices
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "decommission"
    verbose_name = "Списание"
