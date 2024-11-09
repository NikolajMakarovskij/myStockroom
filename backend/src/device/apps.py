from django.apps import AppConfig


class DeviceConfig(AppConfig):
    """_Device_
    The application is designed to maintain a list of intended equipment
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "device"
    verbose_name = "Устройства"
