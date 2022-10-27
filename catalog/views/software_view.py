from django.urls import reverse_lazy
from ..forms import softwareForm, OSForm
from ..models.models import software, os
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from ..utils import DataMixin

class softwareListView(DataMixin, generic.ListView):
    model = software
    template_name = 'catalog/software/software_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Список ПО", searchlink='software', add='new-software')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = software.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(version__icontains=query) |
                Q(bitDepth__icontains=query) | 
                Q(workstation__name__icontains=query) |
                Q(workstation__os__name__icontains=query) |   
                Q(workstation__workplace__name__icontains=query) |
                Q(workstation__workplace__room__name__icontains=query) |
                Q(workstation__workplace__room__floor__icontains=query) |
                Q(workstation__workplace__room__building__icontains=query) 
        )
        return object_list

class softwareDetailView(DataMixin, generic.DetailView):
    model = software
    template_name = 'catalog/software/software_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Програмное обеспечение",add='new-software',update='software-update',delete='software-delete',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class softwareCreate(DataMixin, CreateView):
    model = software
    form_class = softwareForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('software')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить ПО",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class softwareUpdate(DataMixin, UpdateView):
    model = software
    template_name = 'Forms/add.html'
    form_class = softwareForm
    success_url = reverse_lazy('software')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать ПО",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class softwareDelete(DataMixin, DeleteView):
    model = software
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('software')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить ПО",selflink='software')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#ОС
class OSListView(DataMixin, generic.ListView):
    model = os
    template_name = 'catalog/software/OS_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Список ОС", searchlink='OS', add='new-OS')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = os.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) | 
                Q(version__icontains=query) |
                Q(bitDepth__icontains=query) 
        )
        return object_list

class OSDetailView(DataMixin, generic.DetailView):
    model = os
    template_name = 'catalog/software/OS_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Операционная система",add='new-OS',update='OS-update',delete='OS-delete',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context 

class OSCreate(DataMixin, CreateView):
    model = os
    form_class = OSForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('OS')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить ОС",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class OSUpdate(DataMixin, UpdateView):
    model = os
    template_name = 'Forms/add.html'
    form_class = OSForm
    success_url = reverse_lazy('OS')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать ОС",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class OSDelete(DataMixin, DeleteView):
    model = os
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('OS')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить ОС",selflink='OS')
        context = dict(list(context.items()) + list(c_def.items()))
        return context