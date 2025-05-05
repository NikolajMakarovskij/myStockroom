from datetime import datetime

from django.core.cache import cache
from django.http import HttpResponse
from django.views import View
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CategoryDec, CategoryDis, Decommission, Disposal
from .resources import DecommissionResource, DisposalResource
from .serializers import (
    DecommissionCatSerializer,
    DecommissionListSerializer,
    DecommissionTasksSerializer,
    DisposalCatSerializer,
    DisposalListSerializer,
)
from .tasks import DecomTasks


# Decommission
class DecommissionCatListRestView(viewsets.ModelViewSet[CategoryDec]):
    queryset = CategoryDec.objects.all()
    serializer_class = DecommissionCatSerializer

    def list(self, request):
        queryset = CategoryDec.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class DecommissionListRestView(viewsets.ModelViewSet[Decommission]):
    queryset = Decommission.objects.all()
    serializer_class = DecommissionListSerializer

    def list(self, request):
        queryset = Decommission.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


# post methods
class AddToDecommissionDeviceView(APIView, DecomTasks):
    queryset = Decommission.objects.all()
    # @permission_required("stockroom.add_consumables_to_stock", raise_exception=True)

    def post(self, request, formant=None):
        serializer = DecommissionTasksSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        device_id = serializer.validated_data["device_id"]
        username = serializer.validated_data["username"]

        try:
            self.add_device_decom(
                device_id=device_id, username=username, status_choice="Списание"
            )
            return Response(
                {
                    "device_id": device_id,
                    "username": username,
                },
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )


class RemoveFromDecommissionDeviceView(APIView, DecomTasks):
    queryset = Decommission.objects.all()
    # @permission_required("stockroom.remove_consumables_from_stock", raise_exception=True)

    def post(self, request, formant=None):
        serializer = DecommissionTasksSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        device_id = serializer.validated_data["device_id"]
        username = serializer.validated_data["username"]

        try:
            self.remove_decom(
                device_id=device_id, username=username, status_choice="Удаление"
            )
            return Response(
                {
                    "device_id": device_id,
                    "username": username,
                },
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ExportDecomDevice(View):
    def get(self, *args, **kwargs):
        resource = DecommissionResource()
        dataset = resource.export()
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f"Devices_in_decommission_{datetime.today().strftime('%Y_%m_%d')}",
                ext="xlsx",
            )
        )
        return response


class ExportDecomDeviceCategory(View):
    def get_context_data(self, *, object_list=None, **kwargs):
        cat_decom = cache.get("cat_decom")
        if not cat_decom:
            cat_decom = CategoryDec.objects.all()
            cache.set("cat_decom", cat_decom, 300)
        context = super().get_context_data(**kwargs)  # type: ignore[misc]
        c_def = self.get_user_context(menu_categories=cat_decom)  # type: ignore[attr-defined]
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get(self, queryset=None, *args, **kwargs):
        queryset = Decommission.objects.filter(
            categories__slug=self.kwargs["category_slug"]
        )
        resource = DecommissionResource()
        dataset = resource.export(queryset, *args, **kwargs)
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f"Devices_in_decommission_{datetime.today().strftime('%Y_%m_%d')}",
                ext="xlsx",
            )
        )
        return response


# Disposal
class DisposalCatListRestView(viewsets.ModelViewSet[CategoryDis]):
    queryset = CategoryDis.objects.all()
    serializer_class = DisposalCatSerializer

    def list(self, request):
        queryset = CategoryDis.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class DisposalListRestView(viewsets.ModelViewSet[Disposal]):
    queryset = Disposal.objects.all()
    serializer_class = DisposalListSerializer

    def list(self, request):
        queryset = Disposal.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


# post methods
class AddToDisposalDeviceView(APIView, DecomTasks):
    queryset = Disposal.objects.all()
    # @permission_required("stockroom.add_consumables_to_stock", raise_exception=True)

    def post(self, request, formant=None):
        serializer = DecommissionTasksSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        device_id = serializer.validated_data["device_id"]
        username = serializer.validated_data["username"]

        try:
            self.add_device_disp(
                device_id=device_id, username=username, status_choice="Утилизация"
            )
            return Response(
                {
                    "device_id": device_id,
                    "username": username,
                },
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )


class RemoveFromDisposalDeviceView(APIView, DecomTasks):
    queryset = Disposal.objects.all()
    # @permission_required("stockroom.remove_consumables_from_stock", raise_exception=True)

    def post(self, request, formant=None):
        serializer = DecommissionTasksSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        device_id = serializer.validated_data["device_id"]
        username = serializer.validated_data["username"]

        try:
            self.remove_disp(
                device_id=device_id, username=username, status_choice="Удаление"
            )
            return Response(
                {
                    "device_id": device_id,
                    "username": username,
                },
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ExportDispDevice(View):
    def get(self, *args, **kwargs):
        resource = DisposalResource()
        dataset = resource.export()
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f"Devices_in_disposal_{datetime.today().strftime('%Y_%m_%d')}",
                ext="xlsx",
            )
        )
        return response


class ExportDispDeviceCategory(View):
    def get_context_data(self, *, object_list=None, **kwargs):
        cat_disp = cache.get("cat_disp")
        if not cat_disp:
            cat_disp = CategoryDis.objects.all()
            cache.set("cat_disp", cat_disp, 300)
        context = super().get_context_data(**kwargs)  # type: ignore[misc]
        c_def = self.get_user_context(menu_categories=cat_disp)  # type: ignore[attr-defined]
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get(self, queryset=None, *args, **kwargs):
        queryset = Disposal.objects.filter(
            categories__slug=self.kwargs["category_slug"]
        )
        resource = DisposalResource()
        dataset = resource.export(queryset, *args, **kwargs)
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f"Devices_in_disposal_{datetime.today().strftime('%Y_%m_%d')}",
                ext="xlsx",
            )
        )
        return response
