import datetime
from django.conf import settings
from device.models import Device
from stockroom.stock import Stock
from stockroom.models import StockDev
from decommission.models import Decommission, CategoryDec, HistoryDec, Disposal, CategoryDis, HistoryDis
from django.contrib import messages


class Decom(object):
    """Class with decommission and disposal methods"""

    # General methods
    def __init__(self, request):
        """
        Initializes the decom
        """
        self.session = request.session
        decom = self.session.get(settings.DECOM_SESSION_ID)
        if not decom:
            # save empty
            decom = self.session[settings.DECOM_SESSION_ID] = {}
        self.decom = decom

    def save(self):
        # Update session
        self.session[settings.DECOM_SESSION_ID] = self.decom
        self.session.modified = True

    def add_category_decom(device_id: str) -> dict:
        """Get category"""
        if not Device.objects.get(id=device_id).categories:
            device_category = None
        else:
            device_category = Device.objects.get(id=device_id).categories.name
            if CategoryDec.objects.filter(name=device_category):
                device_category = CategoryDec.objects.get(name=device_category)
            else:
                device_category = CategoryDec.objects.create(
                    name=Device.objects.get(id=device_id).categories.name,
                    slug=Device.objects.get(id=device_id).categories.slug
                )
        return device_category

    # Decommission
    def create_history_decom(device_id: str, username: int) -> None:
        """Creating an entry in the decommission history"""
        if not (Decom.add_category_decom(device_id)):
            history = HistoryDec.objects.create(
                devices=Device.objects.get(id=device_id).name,
                devicesId=Device.objects.get(id=device_id).id,
                date=datetime.date.today(),
                user=username
            )
        else:
            history = HistoryDec.objects.create(
                devices=Device.objects.filter(id=device_id).get().name,
                devicesId=Device.objects.filter(id=device_id).get().id,
                date=datetime.date.today(),
                categories=Decom.add_category_decom(device_id),
                user=username
            )
        return history

    def add_device_decom(self, device: dict, username: str, status_choice: str) -> None:
        """
        Add a device to a decommission
        """
        quantity = int(0)
        device_id = str(device.id)
        device_add = Device.objects.get(id=device_id)
        if not Decommission.objects.filter(devices=device_id):
            if Decom.add_category_decom(device_id) is None:
                Decommission.objects.create(
                    devices=device_add,
                    date=datetime.date.today(),
                )
            else:
                Decommission.objects.create(
                    devices=device_add,
                    categories=Decom.add_category_decom(device_id),
                    date=datetime.date.today(),
                )
            Decom.create_history_decom(device_id, username)
            Stock.create_history_dev(device_id, quantity, username, status_choice)
            StockDev.objects.filter(devices=device_id).delete()
        else:
            pass
        self.save()

    def remove_decom(self, device: dict, username: str, status_choice: str) -> None:
        """
        Delete from Decommission
        """
        quantity = int(0)
        device_id = str(device.id)
        if Decommission.objects.filter(devices=device_id):
            Decommission.objects.filter(devices=device_id).delete()
            Decom.create_history_decom(device_id, username)
            Stock.create_history_dev(device_id, quantity, username, status_choice)
        self.save()

    # Disposal
    def add_category_disp(device_id: str) -> dict:
        """Get category"""
        if not Device.objects.get(id=device_id).categories:
            device_category = None
        else:
            device_category = Device.objects.get(id=device_id).categories.name
            if CategoryDis.objects.filter(name=device_category):
                device_category = CategoryDis.objects.get(name=device_category)
            else:
                device_category = CategoryDis.objects.create(
                    name=Device.objects.get(id=device_id).categories.name,
                    slug=Device.objects.get(id=device_id).categories.slug
                )
        return device_category

    def create_history_disp(device_id: str, username: str) -> None:
        """Creating an entry in the disposal history"""
        if not (Decom.add_category_disp(device_id)):
            history = HistoryDis.objects.create(
                devices=Device.objects.get(id=device_id).name,
                devicesId=Device.objects.get(id=device_id).id,
                date=datetime.date.today(),
                user=username
            )
        else:
            history = HistoryDis.objects.create(
                devices=Device.objects.filter(id=device_id).get().name,
                devicesId=Device.objects.filter(id=device_id).get().id,
                date=datetime.date.today(),
                categories=Decom.add_category_disp(device_id),
                user=username
            )
        return history

    def add_device_disp(self, device: dict, username: str, status_choice: str) -> None:
        """
        Add a device to a disposal
        """
        username = username
        status_choice = status_choice
        quantity = int(0)
        device_id = str(device.id)
        device_add = Device.objects.get(id=device_id)
        if not Disposal.objects.filter(devices=device_id):
            if Decom.add_category_disp(device_id) is None:
                Disposal.objects.create(
                    devices=device_add,
                    date=datetime.date.today(),
                )
            else:
                Disposal.objects.create(
                    devices=device_add,
                    categories=Decom.add_category_disp(device_id),
                    date=datetime.date.today(),
                )
            Decom.create_history_disp(device_id, username)
            Stock.create_history_dev(device_id, quantity, username, status_choice)
            Decommission.objects.filter(devices=device_id).delete()
        else:
            pass
        self.save()

    def remove_disp(self, device: dict, username: str, status_choice: str) -> None:
        """
        Delete from Decommission
        """
        quantity = int(0)
        status_choice = status_choice
        device_id = str(device.id)
        if Disposal.objects.filter(devices=device_id):
            Disposal.objects.filter(devices=device_id).delete()
            Decom.create_history_disp(device_id, username)
            Stock.create_history_dev(device_id, quantity, username, status_choice)
        self.save()
