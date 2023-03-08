from django.db.utils import IntegrityError
import pytest  
from myStockroom.wsgi import *
from ..models import Signature, Workstation, Consumables, Employee



@pytest.mark.django_db  
def test_signature_create():
    """Тестирует создание записи в базе данных для модели Signature"""
    Employee.objects.create(name="some_employee_1")
    Employee.objects.create(name="some_employee_2")
    Workstation.objects.create(name="Acer C27")
    Consumables.objects.create(name = "storage") 
    signature = Signature.objects.create(  
        name = "signature_name", 
        periodOpen = "2018-9-12",
        periodClose = "2022-3-31",
        employeeRegister = Employee.objects.get(name="some_employee_1"),
        employeeStorage = Employee.objects.get(name="some_employee_2"),
        workstation = Workstation.objects.get(name="Acer C27"),
        storage = Consumables.objects.get(name = "storage") 
    )  

    assert signature.name == "signature_name"
    assert signature.periodOpen == "2018-9-12"
    assert signature.periodClose == "2022-3-31"
    assert signature.employeeRegister.name == "some_employee_1"
    assert signature.employeeStorage.name == "some_employee_2"
    assert signature.workstation.name == "Acer C27"
    assert signature.storage.name == "storage"
