from django.core.cache import cache
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets
from core.utils import DataMixin, FormMessageMixin, deviceMenu
from stockroom.forms import ConsumableInstallForm, StockAddForm, MoveDeviceForm
from .forms import DeviceForm
from .models import Device, DeviceCat
from .serializers import DeviceModelSerializer, DeviceCatModelSerializer


# Устройства
class DeviceListView(LoginRequiredMixin, DataMixin, generic.ListView):
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
            Q(quantity__icontains=query) |
            Q(workplace__name__icontains=query) |
            Q(workplace__room__name__icontains=query) |
            Q(workplace__room__floor__icontains=query) |
            Q(workplace__room__building__icontains=query)
        ).select_related('workplace', 'workplace__room').prefetch_related('workplace__employee')
        return object_list


class DeviceCategoryListView(LoginRequiredMixin, DataMixin, generic.ListView):
    model = Device.objects
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
        object_list = Device.objects.filter(categories__slug=self.kwargs['category_slug']).select_related(
            'workplace', 'workplace__room').prefetch_related('workplace__employee')
        return object_list


class DeviceRestView(DataMixin, FormMessageMixin, viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceModelSerializer
    success_message = f"%(categories)s %(name)s успешно создано"
    error_message = f"%(categories)s %(name)s не удалось создать"


class DeviceCatRestView(DataMixin, FormMessageMixin, viewsets.ModelViewSet):
    queryset = DeviceCat.objects.all()
    serializer_class = DeviceCatModelSerializer
    success_message = f"Категория %(name)s успешно создано"
    error_message = f"Категория %(name)s не удалось создать"


class DeviceDetailView(LoginRequiredMixin, DataMixin, generic.DetailView):
    model = Device
    template_name = 'device/device_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        consumable_form = ConsumableInstallForm(self.request.GET or None)
        stock_form = StockAddForm(self.request.GET or None)
        move_form = MoveDeviceForm(self.request.GET or None)
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
        context['detailMenu'] = deviceMenu
        context['get_device_id'] = self.request.session['get_device_id']
        context['stock_form'] = stock_form
        context['consumable_form'] = consumable_form
        context['move_form'] = move_form
        return context


class DeviceCreate(LoginRequiredMixin, DataMixin, FormMessageMixin, CreateView):
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


class DeviceUpdate(LoginRequiredMixin, DataMixin, FormMessageMixin, UpdateView):
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


class DeviceDelete(LoginRequiredMixin, DataMixin, DeleteView):
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
class ConsumableInstallFormView(FormView):
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


class StockAddFormView(FormView):
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


class MoveFormView(FormView):
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
