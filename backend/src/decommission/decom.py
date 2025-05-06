from typing import Any
from uuid import UUID

from device.models import Device

from .models import CategoryDec, CategoryDis


class Decom(object):
    """Class with decommission and disposal methods"""

    # Decommission
    def add_category_decom(device_id: UUID) -> Any | None:  # type: ignore[misc]
        """Get category"""
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
        """Get category"""
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
