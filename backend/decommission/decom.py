from django.conf import settings
from device.models import Device
from decommission.models import CategoryDec, CategoryDis


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

