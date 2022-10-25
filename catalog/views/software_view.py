from django.urls import reverse_lazy
from ..forms import softwareForm
from ..models.models import software, OS
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
                Q(workstation__name__icontains=query) |
                Q(workstation__OS__name__icontains=query) |   
                Q(workstation__Workplace__name__icontains=query) |
                Q(workstation__Workplace__Room__name__icontains=query) |
                Q(workstation__Workplace__Room__Floor__icontains=query) |
                Q(workstation__Workplace__Room__Building__icontains=query) 
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