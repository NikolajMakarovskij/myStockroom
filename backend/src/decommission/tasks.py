import datetime
from uuid import UUID

from celery import shared_task

from decommission.models import Decommission, Disposal
from device.models import Device
from stockroom.models.devices import StockDev
from stockroom.stock.stock import DevStock

from .decom import Decom


class DecomTasks(Decom):
    """_DecomTasks_
    This class inherits the methods from the Decommission class and is used to define the tasks that will be used in the Celery tasks.
    """

    # Decommission
    @shared_task()
    def add_device_decom(device_id: UUID, username: str, status_choice: str) -> None:  # type: ignore[misc]
        """_add_device_decom_
        Adds a device to a record in the decommission model and deletes it from the stockroom model

        Args:
            device_id (UUID): _uuid of the Device model_
            username (str): _the username received from the session_
            status_choice (str): _the status of the completed operation_
        """

        quantity = int(0)
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
            DevStock.create_history_device(
                device_id, quantity, username, status_choice, note=""
            )
            StockDev.objects.filter(stock_model=device_id).delete()
        else:
            pass

    @shared_task()
    def remove_decom(device_id: UUID, username: str, status_choice: str) -> None:  # type: ignore[misc]
        """_remove_decom_
        Delete from the Decommission model

        Args:
            device_id (UUID): _uuid of the Device model_
            username (str): _the username received from the session_
            status_choice (str): _the status of the completed operation_
        """

        quantity = int(0)
        if Decommission.objects.filter(stock_model=device_id):
            Decommission.objects.filter(stock_model=device_id).delete()
            DevStock.create_history_device(
                device_id, quantity, username, status_choice, note=""
            )

    # Disposal
    @shared_task()
    def add_device_disp(device_id: UUID, username: str, status_choice: str) -> None:  # type: ignore[misc]
        """_add_device_disp_
        Adds a decommission to a record in the disposal model and deletes it from the decommission model

        Args:
            device_id (UUID): _uuid of the Device model_
            username (str): _the username received from the session_
            status_choice (str): _the status of the completed operation_
        """

        username = username
        status_choice = status_choice
        quantity = int(0)
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
            DevStock.create_history_device(
                device_id, quantity, username, status_choice, note=""
            )
            Decommission.objects.filter(stock_model=device_id).delete()
        else:
            pass

    @shared_task()
    def remove_disp(device_id: UUID, username: str, status_choice: str) -> None:  # type: ignore[misc]
        """_remove_disp_
        Delete from the Disposal model

        Args:
            device_id (UUID): _uuid of the Device model_
            username (str): _the username received from the session_
            status_choice (str): _the status of the completed operation_
        """

        quantity = int(0)
        status_choice = status_choice
        if Disposal.objects.filter(stock_model=device_id):
            Disposal.objects.filter(stock_model=device_id).delete()
            DevStock.create_history_device(
                device_id, quantity, username, status_choice, note=""
            )
