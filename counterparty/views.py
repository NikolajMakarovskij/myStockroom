from .forms import manufacturerForm
from .models import Manufacturer
from catalog.models import References
from django.views import generic
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from catalog.utils import *

#Контрагенты
class CounterpartyView(DataMixin, generic.ListView):
    template_name = 'counterparty/counterparty.html'
    model = References

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Расходники", searchlink='references_search',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Производитель
class manufacturerListView(DataMixin, generic.ListView):
    model = Manufacturer
    template_name = 'counterparty/manufacturer_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Список производителей", searchlink='counterparty:manufacturer_search',add='counterparty:new-manufacturer',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = Manufacturer.objects.filter(
                Q(name__icontains=query) |
                Q(country__icontains=query) |
                Q(production__icontains=query) 
        )
        return object_list

class manufacturerDetailView(DataMixin, generic.DetailView):
    model = Manufacturer
    template_name = 'counterparty/manufacturer_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Производитель",add='counterparty:new-manufacturer',update='counterparty:manufacturer-update',delete='counterparty:manufacturer-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class manufacturerCreate(DataMixin, CreateView):
    model = Manufacturer
    form_class = manufacturerForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('counterparty:manufacturer_list')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить производителя",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class manufacturerUpdate(DataMixin, UpdateView):
    model = Manufacturer
    template_name = 'Forms/add.html'
    form_class = manufacturerForm
    success_url = reverse_lazy('counterparty:manufacturer_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать производителя",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class manufacturerDelete(DataMixin, DeleteView):
    model = Manufacturer
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('counterparty:manufacturer_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить производителя",selflink='counterparty:manufacturer_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context
