from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from core.utils import DataMixin, FormMessageMixin
from stockroom.forms import ConsumableInstallForm, StockAddForm, MoveDeviceForm, AddHistoryDeviceForm
from .forms import DeviceForm
from .models import Device, DeviceCat
from .serializers import DeviceSerializer, DeviceCatModelSerializer, DeviceListSerializer

from django.http import HttpResponse
from .resources import DeviceResource
from datetime import datetime


# Devices
class DeviceListView(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView):
    permission_required = ('device.view_device',)
    model = Device
    template_name = 'device/device_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        device_cat = cache.get('device_cat')
        if not device_cat:
            device_cat = DeviceCat.objects.all()
            cache.set('device_cat', device_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Устройства", searchlink='device:device_search', add='device:new-device',
                                      menu_categories=device_cat)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            query = ''
        object_list = Device.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(invent__icontains=query) |
            Q(serial__icontains=query) |
            Q(manufacturer__name__icontains=query) |
            Q(consumable__name__icontains=query) |
            Q(hostname__icontains=query) |
            Q(ip_address__icontains=query) |
            Q(quantity__icontains=query) |
            Q(workplace__name__icontains=query) |
            Q(workplace__room__name__icontains=query) |
            Q(workplace__room__floor__icontains=query) |
            Q(workplace__room__building__icontains=query)
        ).select_related('workplace', 'workplace__room').prefetch_related('workplace__employee').distinct()
        return object_list


class DeviceCategoryListView(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView):
    model = Device.objects
    template_name = 'device/device_list.html'
    permission_required = ('device.view_device',)

    def get_context_data(self, *, object_list=None, **kwargs):
        device_cat = cache.get('device_cat')
        if not device_cat:
            device_cat = DeviceCat.objects.all()
            cache.set('device_cat', device_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Устройства",
                                      searchlink="device:device_search",
                                      add='device:new-device', menu_categories=device_cat)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            query = ''
        object_list = Device.objects.filter(
            categories__slug=self.kwargs['category_slug']
        ).filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(invent__icontains=query) |
            Q(serial__icontains=query) |
            Q(manufacturer__name__icontains=query) |
            Q(consumable__name__icontains=query) |
            Q(hostname__icontains=query) |
            Q(ip_address__icontains=query) |
            Q(quantity__icontains=query) |
            Q(workplace__name__icontains=query) |
            Q(workplace__room__name__icontains=query) |
            Q(workplace__room__floor__icontains=query) |
            Q(workplace__room__building__icontains=query)
        ).select_related('workplace', 'workplace__room').prefetch_related('workplace__employee').distinct()
        return object_list


class DeviceRestView(DataMixin, FormMessageMixin, viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    success_message = f"%(categories)s %(name)s успешно создано"
    error_message = f"%(categories)s %(name)s не удалось создать"


class DeviceListRestView(DataMixin, viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceListSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = Device.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class DeviceCatRestView(DataMixin, FormMessageMixin, viewsets.ModelViewSet):
    queryset = DeviceCat.objects.all()
    serializer_class = DeviceCatModelSerializer
    success_message = f"Категория %(name)s успешно создано"
    error_message = f"Категория %(name)s не удалось создать"


class DeviceDetailView(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.DetailView):
    model = Device
    template_name = 'device/device_detail.html'
    permission_required = ('device.view_device',)

    def get_context_data(self, *, object_list=None, **kwargs):
        consumable_form = ConsumableInstallForm(self.request.GET or None)
        stock_form = StockAddForm(self.request.GET or None)
        move_form = MoveDeviceForm(self.request.GET or None)
        history_form = AddHistoryDeviceForm(self.request.GET or None)
        self.request.session['get_device_id'] = str(Device.objects.filter(pk=self.kwargs['pk']).get().id)
        device_cat = cache.get('device_cat')
        if not device_cat:
            device_cat = DeviceCat.objects.all()
            cache.set('device_cat', device_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Устройство", add='device:new-device', update='device:device-update', delete='device:device-delete',
        )
        context = dict(list(context.items()) + list(c_def.items()))
        context['get_device_id'] = self.request.session['get_device_id']
        context['stock_form'] = stock_form
        context['consumable_form'] = consumable_form
        context['move_form'] = move_form
        context['history_form'] = history_form
        return context


class DeviceCreate(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, CreateView):
    permission_required = ('device.add_device',)
    model = Device
    form_class = DeviceForm
    template_name = 'Forms/add.html'
    success_message = f"%(categories)s %(name)s успешно создано"
    error_message = f"%(categories)s %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить устройство", )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class DeviceUpdate(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, UpdateView):
    permission_required = ('device.change_device',)
    model = Device
    template_name = 'Forms/add.html'
    form_class = DeviceForm
    success_message = f"%(categories)s %(name)s успешно обновлено"
    error_message = f"%(categories)s %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class DeviceDelete(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, DeleteView):
    permission_required = ('device.delete_device',)
    model = Device
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('device:device_list')
    success_message = f"%(categories)s успешно удален"
    error_message = f"%(categories)s не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить", selflink='device:device_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


# form views
class ConsumableInstallFormView(PermissionRequiredMixin, FormView):
    permission_required = ('device.can_install_consumable',)
    form_class = ConsumableInstallForm
    template_name = 'device/device_detail.html'
    success_url = reverse_lazy('device:device_list')

    def post(self, request, *args, **kwargs):
        consumable_form = self.form_class(request.POST)
        if consumable_form.is_valid():
            consumable_form.save()
            return self.render_to_response(
                self.get_context_data(
                    success=True
                )
            )
        else:
            return self.render_to_response(
                self.get_context_data(
                    consumable_form=consumable_form,
                )
            )


class StockAddFormView(PermissionRequiredMixin, FormView):
    permission_required = ('device.can_add_stock',)
    form_class = StockAddForm
    template_name = 'device/device_detail.html'
    success_url = reverse_lazy('device:device_list')

    def post(self, request, *args, **kwargs):
        stock_form = self.form_class(request.POST)
        consumable_form = ConsumableInstallForm()
        if stock_form.is_valid():
            stock_form.save()
            return self.render_to_response(
                self.get_context_data(
                    success=True
                )
            )
        else:
            return self.render_to_response(
                self.get_context_data(
                    stock_form=stock_form,
                    consumable_form=consumable_form
                )
            )


class MoveFormView(PermissionRequiredMixin, FormView):
    permission_required = ('device.can_install_accessories',)
    form_class = MoveDeviceForm
    template_name = 'device/device_detail.html'
    success_url = reverse_lazy('device:device_list')

    def post(self, request, *args, **kwargs):
        move_form = self.form_class(request.POST)
        consumable_form = ConsumableInstallForm()
        stock_form = StockAddForm()

        if move_form.is_valid():
            move_form.save()
            return self.render_to_response(
                self.get_context_data(
                    success=True
                )
            )
        else:
            return self.render_to_response(
                self.get_context_data(
                    stock_form=stock_form,
                    consumable_form=consumable_form,
                    move_form=move_form
                )
            )


class AddHistoryFormView(PermissionRequiredMixin, FormView):
    permission_required = ('device.can_add_history',)
    form_class = AddHistoryDeviceForm
    template_name = 'device/device_detail.html'
    success_url = reverse_lazy('device:device_list')

    def post(self, request, *args, **kwargs):
        history_form = self.form_class(request.POST)
        move_form = MoveDeviceForm
        consumable_form = ConsumableInstallForm()
        stock_form = StockAddForm()

        if history_form.is_valid():
            history_form.save()
            return self.render_to_response(
                self.get_context_data(
                    success=True
                )
            )
        else:
            return self.render_to_response(
                self.get_context_data(
                    stock_form=stock_form,
                    consumable_form=consumable_form,
                    move_form=move_form,
                    history_form=history_form
                )
            )


class ExportDevice(View):

    def get(self, *args, **kwargs):
        resource = DeviceResource()
        dataset = resource.export()
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response['Content-Disposition'] = 'attachment; filename={filename}.{ext}'.format(
            filename=F'Devices_{datetime.today().strftime("%Y_%m_%d")}',
            ext='xlsx'
        )
        return response


class ExportDeviceCategory(View):
    def get_context_data(self, *, object_list=None, **kwargs):
        device_cat = cache.get('device_cat')
        if not device_cat:
            device_cat = DeviceCat.objects.all()
            cache.set('device_cat', device_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(menu_categories=device_cat)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get(self, queryset=None, *args, **kwargs):
        queryset = Device.objects.filter(categories__slug=self.kwargs['category_slug'])
        resource = DeviceResource()
        dataset = resource.export(queryset, *args, **kwargs)
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response['Content-Disposition'] = 'attachment; filename={filename}.{ext}'.format(
            filename=F'Devices_{datetime.today().strftime("%Y_%m_%d")}',
            ext='xlsx'
        )
        return response