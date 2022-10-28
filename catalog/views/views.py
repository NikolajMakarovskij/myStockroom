from ..forms import *
from ..models.models import *
from django.views import generic
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ..utils import *
from .workplace_view import *
from .employee_view import *
from .software_view import *
from .workstation_view import *
from .printer_view import *
from .signature import *

#Главная
class indexView(generic.ListView):
    model = digitalSignature
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['menu'] = menu
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




class digitalSignatureListView(DataMixin, generic.ListView):
    model = digitalSignature
    template_name = 'digital_signature_list.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="ЭЦП", searchlink='digital-signature')
        context = dict(list(context.items()) + list(c_def.items()))
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = digitalSignature.objects.filter(
                Q(name__icontains=query) | 
                Q(validityPeriod__icontains=query) | 
                Q(employee__name__icontains=query) |
                Q(employee__sername__icontains=query) | 
                Q(employee__family__icontains=query) |
                Q(employee__post__name__icontains=query) |  
                Q(employee__post__departament__name__icontains=query) | 
                Q(workstation__name__icontains=query) |
                Q(workstation__os__name__icontains=query) |   
                Q(workplace__name__icontains=query) |
                Q(workplace__room__name__icontains=query) |
                Q(workplace__room__floor__icontains=query) |
                Q(workplace__room__building__icontains=query) 
        )
        return object_list





