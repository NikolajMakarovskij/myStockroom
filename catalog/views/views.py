from ..forms import *
from ..models.models import *
from django.views import generic
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ..utils import *
from .employee_view import *
from .software_view import *
from .workstation_view import *
from .printer_view import *
from .signature_view import *
from .ups_view import *


#Главная
class indexView(generic.ListView):
    model = signature
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['menu'] = menu
        return context

#Справочники
class referencesView(DataMixin, generic.ListView):
    model = references
    template_name = 'references.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Справочники", searchlink='references',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Склад
class warehouseView(DataMixin, generic.ListView):
    model = references
    template_name = 'references.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Справочники", searchlink='references',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Расходники
class consumablesView(DataMixin, generic.ListView):
    model = references
    template_name = 'references.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Справочники", searchlink='references',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Производитель
class manufacturerListView(DataMixin, generic.ListView):
    model = manufacturer
    template_name = 'catalog/manufacturer_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Список производителей", searchlink='manufacturer',add='new-manufacturer',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = manufacturer.objects.filter(
                Q(name__icontains=query) |
                Q(country__icontains=query) |
                Q(production__icontains=query) 
        )
        return object_list

class manufacturerDetailView(DataMixin, generic.DetailView):
    model = manufacturer
    template_name = 'catalog/manufacturer_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Производитель",add='new-manufacturer',update='manufacturer-update',delete='manufacturer-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class manufacturerCreate(DataMixin, CreateView):
    model = manufacturer
    form_class = manufacturerForm
    template_name = 'Forms/add.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить производителя",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class manufacturerUpdate(DataMixin, UpdateView):
    model = manufacturer
    template_name = 'Forms/add.html'
    form_class = manufacturerForm
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать производителя",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class manufacturerDelete(DataMixin, DeleteView):
    model = manufacturer
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('manufacturer')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить производителя",selflink='manufacturer')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Накопитель
class storageListView(DataMixin, generic.ListView):
    model = storage
    template_name = 'catalog/storage_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Список накопителей", searchlink='storage',add='new-storage',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = storage.objects.filter(
                Q(name__icontains=query) |
                Q(manufacturer__name__icontains=query) |
                Q(plug__icontains=query) |
                Q(typeMemory__icontains=query) |
                Q(volumeMemory__icontains=query) |
                Q(employee__name__icontains=query) |
                Q(plug__icontains=query) |
                Q(plug__icontains=query) |
                Q(modelStorage__icontains=query) 
        )
        return object_list

class storageDetailView(DataMixin, generic.DetailView):
    model = storage
    template_name = 'catalog/storage_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Накопитель",add='new-storage',update='storage-update',delete='storage-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class storageCreate(DataMixin, CreateView):
    model = storage
    form_class = storageForm
    template_name = 'Forms/add.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить накопитель",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class storageUpdate(DataMixin, UpdateView):
    model = storage
    template_name = 'Forms/add.html'
    form_class = storageForm
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать накопитель",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class storageDelete(DataMixin, DeleteView):
    model = storage
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('storage')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить накопитель",selflink='storage')
        context = dict(list(context.items()) + list(c_def.items()))
        return context








