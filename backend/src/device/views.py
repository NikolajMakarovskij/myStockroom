from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.db.models import Q
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View, generic
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from rest_framework import viewsets

from core.utils import DataMixin, FormMessageMixin
from stockroom.forms import (
    AddHistoryDeviceForm,
    ConsumableInstallForm,
    MoveDeviceForm,
    StockAddForm,
)

from .forms import DeviceForm
from .models import Device, DeviceCat
from .resources import DeviceResource
from .serializers import DeviceCatModelSerializer, DeviceModelSerializer


# Devices
class DeviceListView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    """_DeviceListView_
    List of device instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        paginate_by (int, optional): _add pagination_
        model (Device): _base model for list_
    """

    permission_required = ("device.view_device",)
    paginate_by = DataMixin.paginate
    model = Device
    template_name = "device/device_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, link for search, link to create device, categories for filtering queryset_
        """
        device_cat = cache.get("device_cat")
        if not device_cat:
            device_cat = DeviceCat.objects.all()
            cache.set("device_cat", device_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Устройства",
            searchlink="device:device_search",
            add="device:new-device",
            menu_categories=device_cat,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_queryset_

        Returns:
            object_list (Device): _description_
        """
        query = self.request.GET.get("q")
        if not query:
            query = ""
        object_list = (
            Device.objects.filter(
                Q(name__icontains=query)
                | Q(description__icontains=query)
                | Q(invent__icontains=query)
                | Q(serial__icontains=query)
                | Q(manufacturer__name__icontains=query)
                | Q(consumable__name__icontains=query)
                | Q(hostname__icontains=query)
                | Q(ip_address__icontains=query)
                | Q(quantity__icontains=query)
                | Q(workplace__name__icontains=query)
                | Q(workplace__room__name__icontains=query)
                | Q(workplace__room__floor__icontains=query)
                | Q(workplace__room__building__icontains=query)
            )
            .select_related("workplace", "workplace__room")
            .prefetch_related("workplace__employee")
            .distinct()
        )
        return object_list


class DeviceCategoryListView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    """_DeviceCategoryListView_
    List of device instances filtered by categories

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        paginate_by (int, optional): _add pagination_
        model (Device): _base model for list_
    """

    model = Device
    paginate_by = DataMixin.paginate
    template_name = "device/device_list.html"
    permission_required = ("device.view_device",)

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, link for search, link to create device, categories for filtering queryset_
        """
        device_cat = cache.get("device_cat")
        if not device_cat:
            device_cat = DeviceCat.objects.all()
            cache.set("device_cat", device_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Устройства",
            searchlink="device:device_search",
            add="device:new-device",
            menu_categories=device_cat,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_queryset_

        Returns:
            object_list (Device): _description_
        """
        query = self.request.GET.get("q")
        if not query:
            query = ""
        object_list = (
            Device.objects.filter(categories__slug=self.kwargs["category_slug"])
            .filter(
                Q(name__icontains=query)
                | Q(description__icontains=query)
                | Q(invent__icontains=query)
                | Q(serial__icontains=query)
                | Q(manufacturer__name__icontains=query)
                | Q(consumable__name__icontains=query)
                | Q(hostname__icontains=query)
                | Q(ip_address__icontains=query)
                | Q(quantity__icontains=query)
                | Q(workplace__name__icontains=query)
                | Q(workplace__room__name__icontains=query)
                | Q(workplace__room__floor__icontains=query)
                | Q(workplace__room__building__icontains=query)
            )
            .select_related("workplace", "workplace__room")
            .prefetch_related("workplace__employee")
            .distinct()
        )
        return object_list


class DeviceRestView(DataMixin, FormMessageMixin, viewsets.ModelViewSet):
    """_DeviceRestView_ returns device

    Other parameters:
        queryset (Device):
        serializer_class (DeviceModelSerializer):
        success_message (str):
        error_message (str):
    """

    queryset = Device.objects.all()
    serializer_class = DeviceModelSerializer
    success_message = "%(categories)s %(name)s успешно создано"
    error_message = "%(categories)s %(name)s не удалось создать"


class DeviceCatRestView(DataMixin, FormMessageMixin, viewsets.ModelViewSet):
    """_DeviceCatRestView_ returns device

    Other parameters:
        queryset (DeviceCat):
        serializer_class (DeviceCatModelSerializer):
        success_message (str):
        error_message (str):
    """

    queryset = DeviceCat.objects.all()
    serializer_class = DeviceCatModelSerializer
    success_message = "Категория %(name)s успешно создано"
    error_message = "Категория %(name)s не удалось создать"


class DeviceDetailView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.DetailView
):
    """_DeviceDetailView_
    Detail of device instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Consumables): _base model for list_
    """

    model = Device
    template_name = "device/device_detail.html"
    permission_required = ("device.view_device",)

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, links to create, update and delete device instance_

        Other parameters:
            consumable_form (ConsumableInstallForm): _form for install consumable_
            stock_form (StockAddForm): _form for add stock_
            move_form (MoveDeviceForm): _form for move device_
            history_form (AddHistoryDeviceForm): _form for add history device_
        """
        consumable_form = ConsumableInstallForm(self.request.GET or None)
        stock_form = StockAddForm(self.request.GET or None)
        move_form = MoveDeviceForm(self.request.GET or None)
        history_form = AddHistoryDeviceForm(self.request.GET or None)
        self.request.session["get_device_id"] = str(
            Device.objects.filter(pk=self.kwargs["pk"]).get().id
        )
        device_cat = cache.get("device_cat")
        if not device_cat:
            device_cat = DeviceCat.objects.all()
            cache.set("device_cat", device_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Устройство",
            add="device:new-device",
            update="device:device-update",
            delete="device:device-delete",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        context["get_device_id"] = self.request.session["get_device_id"]
        context["stock_form"] = stock_form
        context["consumable_form"] = consumable_form
        context["move_form"] = move_form
        context["history_form"] = history_form
        return context


class DeviceCreate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, CreateView
):
    """_DeviceCreate_
    Create of device instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Device): _base model for list_
        form_class (DeviceForm): _form class to view_
        success_message (str):
        error_message (str):
    """

    permission_required = ("device.add_device",)
    model = Device
    form_class = DeviceForm
    template_name = "Forms/add.html"
    success_message = "%(categories)s %(name)s успешно создано"
    error_message = "%(categories)s %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Добавить устройство",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class DeviceUpdate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, UpdateView
):
    """_DeviceUpdate_
    Update of device instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Device): _base model for list_
        form_class (DeviceForm): _form class to view_
        success_message (str):
        error_message (str):
    """

    permission_required = ("device.change_device",)
    model = Device
    template_name = "Forms/add.html"
    form_class = DeviceForm
    success_message = "%(categories)s %(name)s успешно обновлено"
    error_message = "%(categories)s %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class DeviceDelete(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, DeleteView):  # type: ignore[misc]
    """_DeviceDelete_
    Delete of device instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Device): _base model for list_
        success_url (str): _switches to url in case of successful deletion_
        success_message (str):
        error_message (str):
    """

    permission_required = ("device.delete_device",)
    model = Device
    template_name = "Forms/delete.html"
    success_url = reverse_lazy("device:device_list")
    success_message = "%(categories)s успешно удален"
    error_message = "%(categories)s не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to device list_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить", selflink="device:device_list")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


# form views
class ConsumableInstallFormView(PermissionRequiredMixin, FormView):
    """_ConsumableInstallFormView_
    A form for installing consumables and accessories in the device

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        form_class (ConsumableInstallForm): _form class to view_
        success_url (str): _switches to url in case of successful deletion_
    """

    permission_required = ("device.can_install_consumable",)
    form_class = ConsumableInstallForm
    template_name = "device/device_detail.html"
    success_url = reverse_lazy("device:device_list")

    def post(self, request, *args, **kwargs):
        """_post_

        Args:
            request (request): _description_

        Returns:
            self (self): _return post response_
        """
        consumable_form = self.form_class(request.POST)
        if consumable_form.is_valid():
            consumable_form.save()
            return self.render_to_response(self.get_context_data(success=True))
        else:
            return self.render_to_response(
                self.get_context_data(
                    consumable_form=consumable_form,
                )
            )


class StockAddFormView(PermissionRequiredMixin, FormView):
    """_StockAddFormView_
    A form for adding devices in the stock

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        form_class (StockAddForm): _form class to view_
        success_url (str): _switches to url in case of successful deletion_
    """

    permission_required = ("device.can_add_stock",)
    form_class = StockAddForm
    template_name = "device/device_detail.html"
    success_url = reverse_lazy("device:device_list")

    def post(self, request, *args, **kwargs):
        """_post_

        Args:
            request (request): _description_

        Returns:
            self (self): _return post response_
        """
        stock_form = self.form_class(request.POST)
        consumable_form = ConsumableInstallForm()
        if stock_form.is_valid():
            stock_form.save()
            return self.render_to_response(self.get_context_data(success=True))
        else:
            return self.render_to_response(
                self.get_context_data(
                    stock_form=stock_form, consumable_form=consumable_form
                )
            )


class MoveFormView(PermissionRequiredMixin, FormView):
    """_MoveFormView_
    A form for changing workplaces in the device

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        form_class (MoveDeviceForm): _form class to view_
        success_url (str): _switches to url in case of successful deletion_
    """

    permission_required = ("device.can_install_accessories",)
    form_class = MoveDeviceForm
    template_name = "device/device_detail.html"
    success_url = reverse_lazy("device:device_list")

    def post(self, request, *args, **kwargs):
        """_post_

        Args:
            request (request): _description_

        Returns:
            self (self): _return post response_
        """
        move_form = self.form_class(request.POST)
        consumable_form = ConsumableInstallForm()
        stock_form = StockAddForm()

        if move_form.is_valid():
            move_form.save()
            return self.render_to_response(self.get_context_data(success=True))
        else:
            return self.render_to_response(
                self.get_context_data(
                    stock_form=stock_form,
                    consumable_form=consumable_form,
                    move_form=move_form,
                )
            )


class AddHistoryFormView(PermissionRequiredMixin, FormView):
    """_AddHistoryFormView_
    Adds an action record to the device history

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        form_class (AddHistoryDeviceForm): _form class to view_
        success_url (str): _switches to url in case of successful deletion_
    """

    permission_required = ("device.can_add_history",)
    form_class = AddHistoryDeviceForm
    template_name = "device/device_detail.html"
    success_url = reverse_lazy("device:device_list")

    def post(self, request, *args, **kwargs):
        """_post_

        Args:
            request (request): _description_

        Returns:
            self (self): _return post response_
        """

        history_form = self.form_class(request.POST)
        move_form = MoveDeviceForm
        consumable_form = ConsumableInstallForm()
        stock_form = StockAddForm()

        if history_form.is_valid():
            history_form.save()
            return self.render_to_response(self.get_context_data(success=True))
        else:
            return self.render_to_response(
                self.get_context_data(
                    stock_form=stock_form,
                    consumable_form=consumable_form,
                    move_form=move_form,
                    history_form=history_form,
                )
            )


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
                filename=f'Devices_{datetime.today().strftime("%Y_%m_%d")}', ext="xlsx"
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
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(menu_categories=device_cat)
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
                filename=f'Devices_{datetime.today().strftime("%Y_%m_%d")}', ext="xlsx"
            )
        )
        return response
