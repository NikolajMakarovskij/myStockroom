from typing import Any

from django.conf import settings

from decommission.models import CategoryDec, CategoryDis
from device.models import Device


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

    # Decommission
    def add_category_decom(device_id: str) -> Any | None: # type: ignore[misc]
        """Get category"""
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
        """Get category"""
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
