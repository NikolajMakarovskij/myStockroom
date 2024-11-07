from typing import Any

from django.conf import settings

from decommission.models import CategoryDec, CategoryDis
from device.models import Device


class Decom(object):
    """_Decom_
    Class with decommission and disposal methods

    Returns:
        Decom (Decom): _description_
    """

    # General methods
    def __init__(self, request):
        """_init_

        Returns:
            self (Decom): _decom class with django session_
        """
        self.session = request.session
        decom = self.session.get(settings.DECOM_SESSION_ID)
        if not decom:
            # save empty
            decom = self.session[settings.DECOM_SESSION_ID] = {}
        self.decom = decom

    def save(self):
        """_save_
        save modified session

        Returns:
            self (Decom): _decom class with django session_
        """
        # Update session
        self.session[settings.DECOM_SESSION_ID] = self.decom
        self.session.modified = True

    # Decommission
    def add_category_decom(device_id: str) -> Any | None: # type: ignore[misc]
        """_add_category_decom_
        Checks if the Device model has a category; checks if it is in the CategoryDec list.
        If the category exists, it binds it to the record; if it is missing, it is created and then assigned.
        
        Args:
            device_id (str): _uuid of device model_

        Returns:
            Any | None: _Adds a device category to a record in the Decommission model_
        """
        if not Device.objects.get(id=device_id).categories:
            device_category = None
        else:
            device_category = Device.objects.get(id=device_id).categories.name # type: ignore[attr-defined]
            if CategoryDec.objects.filter(name=device_category):
                device_category = CategoryDec.objects.get(name=device_category)
            else:
                device_category = CategoryDec.objects.create(
                    name=Device.objects.get(id=device_id).categories.name, # type: ignore[attr-defined]
                    slug=Device.objects.get(id=device_id).categories.slug, # type: ignore[attr-defined]
                )
        return device_category

    # Disposal
    def add_category_disp(device_id: str) -> Any | None: # type: ignore[misc]
        """_add_category_disp_
        Checks if the Device model has a category; checks if it is in the CategoryDis list.
        If the category exists, it binds it to the record; if it is missing, it is created and then assigned.
        
        Args:
            device_id (str): _uuid of the device model_

        Returns:
            Any | None: _Adds a device category to a record in the Disposal model_
        """
        if not Device.objects.get(id=device_id).categories:
            device_category = None
        else:
            device_category = Device.objects.get(id=device_id).categories.name # type: ignore[attr-defined]
            if CategoryDis.objects.filter(name=device_category):
                device_category = CategoryDis.objects.get(name=device_category)
            else:
                device_category = CategoryDis.objects.create(
                    name=Device.objects.get(id=device_id).categories.name, # type: ignore[attr-defined]
                    slug=Device.objects.get(id=device_id).categories.slug, # type: ignore[attr-defined]
                )
        return device_category
