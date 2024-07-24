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


class DeviceRestView(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project)
        return Response(serializer.data)

    def update(self, request, pk=None):
        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        project = self.queryset.get(pk=pk)
        project.delete()
        return Response(status=204)


class DeviceListRestView(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceListSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = Device.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class DeviceCatRestView(viewsets.ModelViewSet):
    queryset = DeviceCat.objects.all()
    serializer_class = DeviceCatModelSerializer

    def list(self, request):
        queryset = DeviceCat.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project)
        return Response(serializer.data)

    def update(self, request, pk=None):
        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        project = self.queryset.get(pk=pk)
        project.delete()
        return Response(status=204)


class ExportDevice(View):
    def get(self, *args, **kwargs):
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
    def get_context_data(self, *, object_list=None, **kwargs):
        device_cat = cache.get("device_cat")
        if not device_cat:
            device_cat = DeviceCat.objects.all()
            cache.set("device_cat", device_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(menu_categories=device_cat)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get(self, queryset=None, *args, **kwargs):
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
