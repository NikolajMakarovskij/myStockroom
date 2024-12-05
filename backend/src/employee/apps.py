from django.apps import AppConfig


class EmployeeConfig(AppConfig):
    """_EmployeeConfig_
    The application is designed to maintain a list of users of enterprise devices
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "employee"
    verbose_name = "Сотрудники"
