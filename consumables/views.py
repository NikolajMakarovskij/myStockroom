from .forms import *
from .models import *
from django.views import generic
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from catalog.utils import *
from stockroom.forms import StockAddForm

#Расходники
class consumablesView(DataMixin, generic.ListView):
    template_name = 'consumables/consumables_list.html'
    model = Consumables
    menu_categories = Categories.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        menu_categories = Categories.objects.all()
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Расходники", searchlink='consumables:consumables_list',add='consumables:new-consumables', menu_categories=menu_categories)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = Consumables.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(categories__name__icontains=query) |
                Q(buhCode__icontains=query) |
                Q(score__icontains=query) |
                Q(serial__icontains=query) |
                Q(invent__icontains=query)    
        )
        return object_list

class consumablesCategoriesView(DataMixin, generic.ListView):
    template_name = 'consumables/consumables_list.html'
    model = Consumables.objects
    
    def get_context_data(self, *, object_list=None, **kwargs ):
        menu_categories = Categories.objects.all()
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Расходники", searchlink='consumables:consumables_list',add='consumables:new-consumables', menu_categories=menu_categories)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        object_list = Consumables.objects.filter(categories__slug=self.kwargs['category_slug'])
        return object_list        

        

class consumablesDetailView(DataMixin, FormMixin, generic.DetailView):
    model = Consumables
    template_name = 'consumables/consumables_detail.html'
    form_class = StockAddForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Расходники",add='consumables:new-consumables',update='consumables:consumables-update',delete='consumables:consumables-delete',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context 

class consumablesCreate(DataMixin,CreateView):
    model = Consumables
    form_class = consumablesForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('consumables:consumables_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить расходник",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class consumablesUpdate(DataMixin, UpdateView):
    model = Consumables
    template_name = 'Forms/add.html'
    form_class = consumablesForm
    success_url = reverse_lazy('consumables:consumables_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать расходник",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class consumablesDelete(DataMixin, DeleteView):
    model = Consumables
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('consumables:consumables_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить расходник",selflink='consumables:consumables_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context






