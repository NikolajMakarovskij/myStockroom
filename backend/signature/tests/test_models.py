import datetime
import pytest
from django.urls import reverse

from ..models import Signature, Device, Consumables, Employee


@pytest.mark.django_db
def test_signature_create():
    """Тестирует создание записи в базе данных для модели Signature"""
    Employee.objects.create(name="some_employee_1")
    Employee.objects.create(name="some_employee_2")
    Device.objects.create(name="Acer C27")
    Consumables.objects.create(name="storage")
    Signature.objects.create(
        name="signature_name",
        periodOpen=datetime.date.today(),
        periodClose=datetime.date.today(),
        employeeRegister=Employee.objects.get(name="some_employee_1"),
        employeeStorage=Employee.objects.get(name="some_employee_2"),
        workstation=Device.objects.get(name="Acer C27"),
        storage=Consumables.objects.get(name="storage")
    )
    signature = Signature.objects.get(name="signature_name")
    assert Signature.objects.count() == 1
    assert signature.name == "signature_name"
    assert signature.periodOpen == datetime.date.today()
    assert signature.periodClose == datetime.date.today()
    assert signature.employeeRegister.name == "some_employee_1"
    assert signature.employeeStorage.name == "some_employee_2"
    assert signature.workstation.name == "Acer C27"
    assert signature.storage.name == "storage"
    assert signature.__str__() == "signature_name"
    assert signature.get_absolute_url() == reverse('signature:signature-detail', kwargs={'pk': signature.pk})
