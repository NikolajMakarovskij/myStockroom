from .decom import Decom
import datetime
from celery import shared_task
from decommission.models import Decommission, Disposal
from device.models import Device
from stockroom.models.devices import StockDev
from stockroom.stock.stock import DevStock


class DecomTasks(Decom):
    # Decommission
    @shared_task()
    def add_device_decom(device_id: dict, username: str, status_choice: str) -> None:
        """
        Add a device to a decommission
        """
        quantity = int(0)
        device_id = str(device_id)
        device_add = Device.objects.get(id=device_id)
        if not Decommission.objects.filter(stock_model=device_id):
            if Decom.add_category_decom(device_id) is None:
                Decommission.objects.create(
                    stock_model=device_add,
                    date=datetime.date.today(),
                )
            else:
                Decommission.objects.create(
                    stock_model=device_add,
                    categories=Decom.add_category_decom(device_id),
                    date=datetime.date.today(),
                )
            DevStock.create_history_device(DevStock, device_id, quantity, username, status_choice, note=None)
            StockDev.objects.filter(stock_model=device_id).delete()
        else:
            pass

    @shared_task()
    def remove_decom(device_id: str, username: str, status_choice: str) -> None:
        """
        Delete from Decommission
        """
        quantity = int(0)
        device_id = str(device_id)
        if Decommission.objects.filter(stock_model=device_id):
            Decommission.objects.filter(stock_model=device_id).delete()
            DevStock.create_history_device(DevStock, device_id, quantity, username, status_choice, note=None)

    # Disposal
    @shared_task()
    def add_device_disp(device_id: str, username: str, status_choice: str) -> None:
        """
        Add a device to a disposal
        """
        username = username
        status_choice = status_choice
        quantity = int(0)
        device_id = str(device_id)
        device_add = Device.objects.get(id=device_id)
        if not Disposal.objects.filter(stock_model=device_id):
            if Decom.add_category_disp(device_id) is None:
                Disposal.objects.create(
                    stock_model=device_add,
                    date=datetime.date.today(),
                )
            else:
                Disposal.objects.create(
                    stock_model=device_add,
                    categories=Decom.add_category_disp(device_id),
                    date=datetime.date.today(),
                )
            DevStock.create_history_device(DevStock, device_id, quantity, username, status_choice, note=None)
            Decommission.objects.filter(stock_model=device_id).delete()
        else:
            pass

    @shared_task()
    def remove_disp(device_id: str, username: str, status_choice: str) -> None:
        """
        Delete from Decommission
        """
        quantity = int(0)
        status_choice = status_choice
        device_id = str(device_id)
        if Disposal.objects.filter(stock_model=device_id):
            Disposal.objects.filter(stock_model=device_id).delete()
            DevStock.create_history_device(DevStock, device_id, quantity, username, status_choice, note=None)
