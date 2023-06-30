from django.urls import reverse_lazy
from .forms import softwareForm, OSForm
from .models import *
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from catalog.utils import DataMixin, FormMessageMixin


class softwareListView(DataMixin, generic.ListView):
    model = Software
    template_name = 'software/software_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Список ПО", searchlink='software:software_search', add='software:new-software')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = Software.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(version__icontains=query) |
                Q(bitDepth__icontains=query)
        ).select_related('manufacturer')
        return object_list

class softwareDetailView(DataMixin, generic.DetailView):
    model = Software
    template_name = 'software/software_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Програмное обеспечение",add='software:new-software',update='software:software-update',delete='software:software-delete',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class softwareCreate(DataMixin, FormMessageMixin, CreateView):
    model = Software
    form_class = softwareForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('software:software_list')
    success_message = f"ПО %(name)s успешно создано"
    error_message = f"ПО %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить ПО",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class softwareUpdate(DataMixin, FormMessageMixin, UpdateView):
    model = Software
    template_name = 'Forms/add.html'
    form_class = softwareForm
    success_url = reverse_lazy('software:software_list')
    success_message = f"ПО %(name)s успешно обновлено"
    error_message = f"ПО %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать ПО",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class softwareDelete(DataMixin, FormMessageMixin, DeleteView):
    model = Software
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('software:software_list')
    success_message = f"ПО успешно удалено"
    error_message = f"ПО не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить ПО",selflink='software:software_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#ОС
class OSListView(DataMixin, generic.ListView):
    model = Os
    template_name = 'software/OS_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Список ОС", searchlink='software:OS_search', add='software:new-OS')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = Os.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) | 
                Q(version__icontains=query) |
                Q(bitDepth__icontains=query) 
        ).select_related('manufacturer')
        return object_list

class OSDetailView(DataMixin, generic.DetailView):
    model = Os
    template_name = 'software/OS_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Операционная система",add='software:new-OS',update='software:OS-update',delete='software:OS-delete',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context 

class OSCreate(DataMixin, FormMessageMixin, CreateView):
    model = Os
    form_class = OSForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('software:OS_list')
    success_message = f"ОС %(name)s успешно создана"
    error_message = f"ОС %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить ОС",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class OSUpdate(DataMixin, FormMessageMixin, UpdateView):
    model = Os
    template_name = 'Forms/add.html'
    form_class = OSForm
    success_url = reverse_lazy('software:OS_list')
    success_message = f"ОС %(name)s успешно обновлена"
    error_message = f"ОС %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать ОС",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class OSDelete(DataMixin, FormMessageMixin, DeleteView):
    model = Os
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('software:OS_list')
    success_message = f"ОС успешно удалена"
    error_message = f"ОС не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить ОС",selflink='software:OS_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context
