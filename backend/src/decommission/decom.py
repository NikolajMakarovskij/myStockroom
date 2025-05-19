from typing import Any
from uuid import UUID

from device.models import Device

from .models import CategoryDec, CategoryDis


class Decom(object):
    """_Decom_
    Class with decommission and disposal methods

    Returns:
        Decom (Decom): _description_
    """

    # Decommission
    def add_category_decom(device_id: UUID) -> Any | None:  # type: ignore[misc]
        """_add_category_decom_
        Checks if the Device model has a category; checks if it is in the CategoryDec list.
        If the category exists, it binds it to the record; if it is missing, it is created and then assigned.

        Args:
            device_id (UUID): _uuid of device model_

        Returns:
            Any | None: _Adds a device category to a record in the Decommission model_
        """

        if not Device.objects.get(id=device_id).categories:
            device_category = None
        else:
            device_category = Device.objects.get(id=device_id).categories.name  # type: ignore[union-attr]
            if CategoryDec.objects.filter(name=device_category):
                device_category = CategoryDec.objects.get(name=device_category)
            else:
                device_category = CategoryDec.objects.create(
                    name=Device.objects.get(id=device_id).categories.name,  # type: ignore[union-attr]
                    slug=Device.objects.get(id=device_id).categories.slug,  # type: ignore[union-attr]
                )
        return device_category

    # Disposal
    def add_category_disp(device_id: UUID) -> Any | None:  # type: ignore[misc]
        """_add_category_disp_
        Checks if the Device model has a category; checks if it is in the CategoryDis list.
        If the category exists, it binds it to the record; if it is missing, it is created and then assigned.

        Args:
            device_id (UUID): _uuid of the device model_

        Returns:
            Any | None: _Adds a device category to a record in the Disposal model_
        """

        if not Device.objects.get(id=device_id).categories:
            device_category = None
        else:
            device_category = Device.objects.get(id=device_id).categories.name  # type: ignore[union-attr]
            if CategoryDis.objects.filter(name=device_category):
                device_category = CategoryDis.objects.get(name=device_category)
            else:
                device_category = CategoryDis.objects.create(
                    name=Device.objects.get(id=device_id).categories.name,  # type: ignore[union-attr]
                    slug=Device.objects.get(id=device_id).categories.slug,  # type: ignore[union-attr]
                )
        return device_category
