from ..forms import signatureForm
from ..models.models import *
from django.views import generic
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ..utils import *
from .views import *

class signatureListView(DataMixin, generic.ListView):
    model = signature
    template_name = 'catalog/signature/signature_list.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="ЭЦП", searchlink='signature')
        context = dict(list(context.items()) + list(c_def.items()))
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = signature.objects.filter(
                Q(name__icontains=query)|  
                Q(periodOpen__icontains=query)|
                Q(periodClose__icontains=query)|
                Q(employeeRegister__name__icontains=query)|
                Q(employeeStorage__name__icontains=query)|
                Q(storage__name__icontains=query)|
                Q(workstation__name__icontains=query)|
                Q(workstation__workplace__name__icontains=query)|
                Q(workstation__workplace__room__name__icontains=query)|
                Q(workstation__workplace__room__floor__icontains=query)|
                Q(workstation__workplace__room__building__icontains=query)
        )
        return object_list

class signatureDetailView(DataMixin, generic.DetailView):
    model = signature
    template_name = 'catalog/signature/signature_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="ЭЦП",add='new-signature',update='signature-update',delete='signature-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class signatureCreate(DataMixin, CreateView):
    model = signature
    form_class = signatureForm
    template_name = 'Forms/add.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить ЭЦП",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class signatureUpdate(DataMixin, UpdateView):
    model = signature
    template_name = 'Forms/add.html'
    form_class = signatureForm
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать ЭЦП",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class signatureDelete(DataMixin, DeleteView):
    model = signature
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('signature')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить ЭЦП",selflink='signature')
        context = dict(list(context.items()) + list(c_def.items()))
        return context
