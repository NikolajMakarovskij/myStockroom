from .forms import deviceForm
from stockroom.forms import ConsumableInstallForm
from .models import Device, Device_cat
from django.views import generic
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from catalog.utils import *
from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import *

#Устройства
class deviceListView(DataMixin, generic.ListView):
    model = Device
    template_name = 'device/device_list.html'
    
    
    def get_context_data(self, *, object_list=None, **kwargs):
        device_cat = cache.get('device_cat')
        if not device_cat:
            device_cat = Device_cat.objects.all()
            cache.set('device_cat', device_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Устройства", searchlink='device:device_search', add='device:new-device', menu_categories=device_cat)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = Device.objects.filter(
                Q(name__icontains=query) | 
                Q(description__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(consumable__name__icontains=query) |
                Q(score__icontains=query) |   
                Q(workplace__name__icontains=query) |
                Q(workplace__room__name__icontains=query) |
                Q(workplace__room__floor__icontains=query) |
                Q(workplace__room__building__icontains=query) 
        ).select_related('manufacturer','categories', 'consumable', 'workplace', 'workplace__room')
        return object_list

class deviceCategoryListView(DataMixin, generic.ListView):
    model = Device.objects
    template_name = 'device/device_list.html'
    
    
    def get_context_data(self, *, object_list=None, **kwargs):
        device_cat = cache.get('device_cat')
        if not device_cat:
            device_cat = Device_cat.objects.all()
            cache.set('device_cat', device_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Устройства", searchlink='device:device_search', add='device:new-device', menu_categories=device_cat)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        object_list = Device.objects.filter(categories__slug=self.kwargs['category_slug']).select_related('manufacturer', 'categories', 'consumable', 'workplace', 'workplace__room')
        return object_list 

class DeviceRestView(DataMixin, FormMessageMixin, viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceModelSerializer
    success_message = '%(categories)s %(name)s успешно создано'
    error_message = '%(categories)s %(name)s не удалось создать'

    @action(methods=['get'], detail=False)
    def get_devices(self, request):
        devices = Device.objects.all()
        return Response({'devices': [c.name for c in devices]})
    
    @action(methods=['get'], detail=True)
    def get_device(self, request, pk=None):
        device = Device.objects.get(pk=pk).device
        return Response({
            'device': device.name, 
            'categories':device.categories,
            'manufacturer':device.manufacturer, 
            'serial':device.serial,
            'serialImg':device.serialImg,
            'invent':device.invent,
            'inventImg':device.inventImg,
            'description':device.description,
            'workplace':device.workplace,
            'consumable':device.consumable,
            'score':device.score,
            'note':device.note
            })

    @action(methods=['get'], detail=False)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Устройство")
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class Device_catRestView(DataMixin, FormMessageMixin, viewsets.ModelViewSet):
    queryset = Device_cat.objects.all()
    serializer_class = Device_catModelSerializer
    success_message = 'Категория %(name)s успешно создано'
    error_message = 'Категория %(name)s не удалось создать'

    @action(methods=['get'], detail=False)
    def get_device_cats(self, request):
        device_cats = Device_cat.objects.all()
        return Response({'device_cats': [c.name for c in device_cats]})
    
    @action(methods=['get'], detail=True)
    def get_device_cat(self, request, pk=None):
        device_cat = Device_cat.objects.get(pk=pk).device_cat
        return Response({'device_cat': device_cat.name, 'slug':device_cat.slug})

    @action(methods=['get'], detail=False)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Категории")
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class deviceDetailView(DataMixin, FormMixin, generic.DetailView):
    model = Device
    template_name = 'device/device_detail.html'
    form_class = ConsumableInstallForm
    
    def get_context_data(self, *, object_list=None, **kwargs):
        device_cat = cache.get('device_cat')
        if not device_cat:
            device_cat = Device_cat.objects.all()
            cache.set('device_cat', device_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Устройство "+Device.objects.get().categories.name+' '+Device.objects.get().name,add='device:new-device',update='device:device-update',delete='device:device-delete',)
        context = dict(list(context.items()) + list(c_def.items()))
        context['detailMenu'] = deviceMenu
        return context

class deviceCreate(DataMixin, FormMessageMixin, CreateView):
    model = Device
    form_class = deviceForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('device:device_list')
    success_message = '%(categories)s %(name)s успешно создано'
    error_message = '%(categories)s %(name)s не удалось создать'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить устройство",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class deviceUpdate(DataMixin, FormMessageMixin, UpdateView):
    model = Device
    template_name = 'Forms/add.html'
    form_class = deviceForm
    success_url = reverse_lazy('device:device_list')
    success_message = '%(categories)s %(name)s успешно обновлено'
    error_message = '%(categories)s %(name)s не удалось обновить'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать "+Device.objects.get().categories.name+' '+Device.objects.get().name,)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class deviceDelete(DataMixin, DeleteView):
    model = Device
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('device:device_list')
    success_message = '%(categories)s успешно удален'
    error_message = '%(categories)s не удалось удалить'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить "+Device.objects.get().categories.name+' '+Device.objects.get().name,selflink='device:device_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


