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
    """_DecommissionCatListRestView_ returns categories data in JSON format.

    Other parameters:
        queryset (CategoryDec):
        serializer_class (DecommissionCatSerializer):
    """

    queryset = CategoryDec.objects.all()
    serializer_class = DecommissionCatSerializer

    def list(self, request):
        """_list_ returns categories fields in JSON format.

        Args:
            request (_type_):

        Returns:
            data (JSON):
        """

        queryset = CategoryDec.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class DecommissionListRestView(viewsets.ModelViewSet[Decommission]):
    """_DecommissionListRestView_ returns decommission list with extended fields in JSON format.

    Other parameters:
        queryset (Decommission):
        serializer_class (DecommissionListSerializer):
    """

    queryset = Decommission.objects.all()
    serializer_class = DecommissionListSerializer

    def list(self, request):
        """_list_ returns decommission list with extended fields in JSON format.

        Args:
            request (_type_):

        Returns:
            data (JSON):
        """

        queryset = Decommission.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


# post methods
class AddToDecommissionDeviceView(APIView, DecomTasks):
    """_AddToDecommissionDeviceView_ adds a device to the decommission list.

    Other parameters:
        queryset (Decommission):
    """

    queryset = Decommission.objects.all()
    # @permission_required("stockroom.add_consumables_to_stock", raise_exception=True)

    def post(self, request, formant=None):
        """_post_ adds a device to the decommission list.

        Args:
            request (_type_):
            formant (_type_, optional):

        Other Parameters:
            serializer (DecommissionTasksSerializer):
            device_id (UUID):
            username (str):

        Returns:
            data (JSON):
            errors (JSON): _serializer.errors_
        """

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
    """_RemoveFromDecommissionDeviceView_ removes a device from the decommission list.

    Other parameters:
        queryset (Decommission):
    """

    queryset = Decommission.objects.all()
    # @permission_required("stockroom.remove_consumables_from_stock", raise_exception=True)

    def post(self, request, formant=None):
        """_post_ removes a device from the decommission list.

        Args:
            request (_type_):
            formant (_type_, optional):

        Other Parameters:
            serializer (DecommissionTasksSerializer):
            device_id (UUID):
            username (str):

        Returns:
            data (JSON):
            errors (JSON): _serializer.errors_
        """

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
    """_ExportDecomDevice_
    Returns an Excel file with all records of Decommission from the database
    """

    def get(self, *args, **kwargs):
        """extracts all records of Decommission from the database and converts them into an xlsx file

        Returns:
            response (HttpResponse): _returns xlsx file_

        Other parameters:
            resource (DecommissionResource): _dict of Decommission for export into an xlsx file_
        """

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
    """_ExportConsumableCategory_
    Returns an Excel file with filtered records by categories of Decommission from the database
    """

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_ The function is used to return a list of categories

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to decommission list_
        """

        cat_decom = cache.get("cat_decom")
        if not cat_decom:
            cat_decom = CategoryDec.objects.all()
            cache.set("cat_decom", cat_decom, 300)
        context = super().get_context_data(**kwargs)  # type: ignore[misc]
        c_def = self.get_user_context(menu_categories=cat_decom)  # type: ignore[attr-defined]
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get(self, queryset=None, *args, **kwargs):
        """extracts filtered records by categories of Decommission from the database and converts them into an xlsx file

        Returns:
            response (HttpResponse): _returns xlsx file_

        Other parameters:
            resource (DecommissionResource): _dict of Decommission for export into an xlsx file_
        """

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
    """_DisposalCatListRestView_ returns categories data in JSON format.

    Other parameters:
        queryset (CategoryDis):
        serializer_class (DisposalCatSerializer):
    """

    queryset = CategoryDis.objects.all()
    serializer_class = DisposalCatSerializer

    def list(self, request):
        """_list_ returns categories fields in JSON format.

        Args:
            request (_type_):

        Returns:
            data (JSON):
        """

        queryset = CategoryDis.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class DisposalListRestView(viewsets.ModelViewSet[Disposal]):
    """_DisposalListRestView_ returns disposal data in JSON format.

    Other parameters:
        queryset (Disposal):
        serializer_class (DisposalListSerializer):
    """

    queryset = Disposal.objects.all()
    serializer_class = DisposalListSerializer

    def list(self, request):
        """_list_ returns disposal fields in JSON format.

        Args:
            request (_type_):

        Returns:
            data (JSON):
        """

        queryset = Disposal.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


# post methods
class AddToDisposalDeviceView(APIView, DecomTasks):
    """_AddToDisposalDeviceView_ adds a device to the disposal list.

    Other parameters:
        queryset (Disposal):
    """

    queryset = Disposal.objects.all()
    # @permission_required("stockroom.add_consumables_to_stock", raise_exception=True)

    def post(self, request, formant=None):
        """_post_ adds a device to the disposal list.

        Args:
            request (_type_):
            formant (_type_, optional):

        Other Parameters:
            serializer (DecommissionTasksSerializer):
            device_id (UUID):
            username (str):

        Returns:
            data (JSON):
            errors (JSON): _serializer.errors_
        """

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
    """_RemoveFromDisposalDeviceView_ removes a device from the disposal list.

    Other parameters:
        queryset (Disposal):
    """

    queryset = Disposal.objects.all()
    # @permission_required("stockroom.remove_consumables_from_stock", raise_exception=True)

    def post(self, request, formant=None):
        """_post_ removes a device from the disposal list.

        Args:
            request (_type_):
            formant (_type_, optional):

        Other Parameters:
            serializer (DecommissionTasksSerializer):
            device_id (UUID):
            username (str):

        Returns:
            data (JSON):
            errors (JSON): _serializer.errors_
        """

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
    """_ExportDecomDevice_
    Returns an Excel file with all records of Disposal from the database
    """

    def get(self, *args, **kwargs):
        """extracts all records of Disposal from the database and converts them into an xlsx file

        Returns:
            response (HttpResponse): _returns xlsx file_

        Other parameters:
            resource (DisposalResource): _dict of Disposal for export into an xlsx file_
        """

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
    """_ExportConsumableCategory_
    Returns an Excel file with filtered records by categories of Disposal from the database
    """

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_ The function is used to return a list of categories

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to disposal list_
        """

        cat_disp = cache.get("cat_disp")
        if not cat_disp:
            cat_disp = CategoryDis.objects.all()
            cache.set("cat_disp", cat_disp, 300)
        context = super().get_context_data(**kwargs)  # type: ignore[misc]
        c_def = self.get_user_context(menu_categories=cat_disp)  # type: ignore[attr-defined]
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get(self, queryset=None, *args, **kwargs):
        """extracts filtered records by categories of Disposal from the database and converts them into an xlsx file

        Returns:
            response (HttpResponse): _returns xlsx file_

        Other parameters:
            resource (DisposalResource): _dict of Disposal for export into an xlsx file_
        """

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
