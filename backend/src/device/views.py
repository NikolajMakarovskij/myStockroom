from datetime import datetime

from django.core.cache import cache
from django.http import HttpResponse
from django.views import View
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from .models import Device, DeviceCat
from .resources import DeviceResource
from .serializers import (
    DeviceCatModelSerializer,
    DeviceListSerializer,
    DeviceSerializer,
)


class DeviceListRestView(viewsets.ReadOnlyModelViewSet[Device]):
    """_DeviceListRestView_ returns devices with extended fields data in JSON format.

    Other parameters:
        queryset (Device):
        serializer_class (DeviceListSerializer):
        permission_classes (permissions.AllowAny):
    """

    queryset = Device.objects.all()
    serializer_class = DeviceListSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        """_list_ returns devices list with extended fields in JSON format.

        Args:
            request (_type_):

        Returns:
            data (JSON):
        """

        queryset = Device.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class DeviceModelRestView(viewsets.ModelViewSet[Device]):
    """_DeviceModelRestView_ returns devices in JSON format.

    Other parameters:
        queryset (Device):
        serializer_class (DeviceSerializer):
    """

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def create(self, request):
        """_create_ adds devices to the database.

        Args:
            request (_type_):

        Returns:
            data (JSON):
            error (JSON):
        """

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        """_retrieve_ returns devices data in JSON format.

        Args:
            request (_type_):
            pk (UUID | None, optional):

        Returns:
            data (JSON):
        """

        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """_update_ updates devices in the database.

        Args:
            request (_type_):
            pk (UUID | None, optional):

        Returns:
            data (JSON):
            error (JSON):
        """

        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        """_destroy_ deletes devices from the database.

        Args:
            request (_type_):
            pk (UUID | None, optional):

        Returns:
            status (204):
        """

        project = self.queryset.get(pk=pk)
        project.delete()
        return Response(status=204)


class DeviceCatRestView(viewsets.ModelViewSet[DeviceCat]):
    """_DeviceCatRestView_ returns categories in JSON format.

    Other parameters:
        queryset (DeviceCat):
        serializer_class (DeviceCatModelSerializer):
    """

    queryset = DeviceCat.objects.all()
    serializer_class = DeviceCatModelSerializer

    def list(self, request):
        """_list_ returns categories in JSON format.

        Args:
            request (_type_):

        Returns:
            data (JSON):
        """

        queryset = DeviceCat.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """_create_ adds categories to the database.

        Args:
            request (_type_):

        Returns:
            data (JSON):
            error (JSON):
        """

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        """_retrieve_ returns categories in JSON format.

        Args:
            request (_type_):
            pk (UUID | None, optional):

        Returns:
            data (JSON):
            error (JSON):
        """

        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """_update_ updates categories in the database.

        Args:
            request (_type_):
            pk (UUID | None, optional):

        Returns:
            data (JSON):
            error (JSON):
        """

        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        """_destroy_ deletes categories from the database.

        Args:
            request (_type_):
            pk (UUID | None, optional):

        Returns:
            status (204):
        """

        project = self.queryset.get(pk=pk)
        project.delete()
        return Response(status=204)


class ExportDevice(View):
    """_ExportDevice_
    Returns an Excel file with all records of devices from the database
    """

    def get(self, *args, **kwargs):
        """extracts all records of devices from the database and converts them into an xlsx file

        Returns:
            response (HttpResponse): _returns xlsx file_

        Other parameters:
            resource (DeviceResource): _dict of devices for export into an xlsx file_
        """

        resource = DeviceResource()
        dataset = resource.export()
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f"Devices_{datetime.today().strftime('%Y_%m_%d')}", ext="xlsx"
            )
        )
        return response


class ExportDeviceCategory(View):
    """_ExportDeviceCategory_
    Returns an Excel file with all records of devices from the database
    """

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_ The function is used to return a list of categories

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to devices list_
        """

        device_cat = cache.get("device_cat")
        if not device_cat:
            device_cat = DeviceCat.objects.all()
            cache.set("device_cat", device_cat, 300)
        context = super().get_context_data(**kwargs)  # type: ignore[misc]
        c_def = self.get_user_context(menu_categories=device_cat)  # type: ignore[attr-defined]
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get(self, queryset=None, *args, **kwargs):
        """extracts filtered records by categories of devices from the database and converts them into an xlsx file

        Returns:
            response (HttpResponse): _returns xlsx file_

        Other parameters:
            resource (DeviceResource): _dict of devices for export into an xlsx file_
        """

        queryset = Device.objects.filter(categories__slug=self.kwargs["category_slug"])
        resource = DeviceResource()
        dataset = resource.export(queryset, *args, **kwargs)
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f"Devices_{datetime.today().strftime('%Y_%m_%d')}", ext="xlsx"
            )
        )
        return response
