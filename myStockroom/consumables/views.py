from .forms import *
from .models import Consumables, Categories
from django.views import generic
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from catalog.utils import *
from stockroom.forms import StockAddForm
from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import *


#Расходники главная
class consumableIndexView(generic.TemplateView):
    """
    Главная
    """
    template_name = 'consumables/consumables_index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Расходники и комплектующие'
        context['menu'] = menu
        return context

#Расходники
class consumablesView(DataMixin, generic.ListView):
    template_name = 'consumables/consumables_list.html'
    model = Consumables

    def get_context_data(self, *, object_list=None, **kwargs):
        cons_cat = cache.get('cons_cat')
        if not cons_cat:
            cons_cat = Categories.objects.all()
            cache.set('cons_cat', cons_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Расходники", searchlink='consumables:consumables_search',add='consumables:new-consumables', menu_categories=cons_cat)
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
        ).select_related('categories', 'manufacturer')
        return object_list

class consumablesCategoriesView(DataMixin, generic.ListView):
    template_name = 'consumables/consumables_list.html'
    model = Consumables.objects
    
    def get_context_data(self, *, object_list=None, **kwargs ):
        cons_cat = cache.get('cons_cat')
        if not cons_cat:
            cons_cat = Categories.objects.all()
            cache.set('cons_cat', cons_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Расходники", searchlink='consumables:consumables_search',add='consumables:new-consumables', menu_categories=cons_cat)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        object_list = Consumables.objects.filter(categories__slug=self.kwargs['category_slug']).select_related('categories', 'manufacturer')
        return object_list        

        
class ConsumablesRestView(DataMixin, FormMessageMixin, viewsets.ModelViewSet):
    queryset = Consumables.objects.all()
    serializer_class = ConsumablesModelSerializer
    success_message = f"%(categories)s %(name)s успешно создано"
    error_message = f"%(categories)s %(name)s не удалось создать"

    def get_serializer_context(self):
        context = super().get_serializer_context()
        return context

class CategoriesRestView(DataMixin, FormMessageMixin, viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesModelSerializer
    success_message = f"Категория %(name)s успешно создана"
    error_message = f"Категория %(name)s не удалось создать" 

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        context.update({"menu": menu})
        return context

class consumablesDetailView(DataMixin, FormMixin, generic.DetailView):
    model = Consumables
    template_name = 'consumables/consumables_detail.html'
    form_class = StockAddForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Расходник",add='consumables:new-consumables',update='consumables:consumables-update',delete='consumables:consumables-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context 

class consumablesCreate(DataMixin, FormMessageMixin, CreateView):
    model = Consumables
    form_class = consumablesForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('consumables:consumables_list')
    success_message = f"Расходник %(name)s успешно создан"
    error_message = f"Расходник %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить расходник",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class consumablesUpdate(DataMixin, FormMessageMixin, UpdateView):
    model = Consumables
    template_name = 'Forms/add.html'
    form_class = consumablesForm
    success_url = reverse_lazy('consumables:consumables_list')
    success_message = f"Расходник %(name)s успешно обновлен"
    error_message = f"Расходник %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать расходник")
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class consumablesDelete(DataMixin, FormMessageMixin, DeleteView):
    model = Consumables
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('consumables:consumables_list')
    success_message = f"Расходник успешно удален"
    error_message = f"Расходник не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить расходник",selflink='consumables:consumables_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


#Комплектующие
class accessoriesView(DataMixin, generic.ListView):
    template_name = 'consumables/accessories_list.html'
    model = Accessories

    def get_context_data(self, *, object_list=None, **kwargs):
        acc_cat = cache.get('acc_cat')
        if not acc_cat:
            acc_cat = Acc_cat.objects.all()
            cache.set('acc_cat', acc_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Комплектующие", searchlink='consumables:accessories_search',add='consumables:new-accessories', menu_categories=acc_cat)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = Accessories.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(categories__name__icontains=query) |
                Q(buhCode__icontains=query) |
                Q(score__icontains=query) |
                Q(serial__icontains=query) |
                Q(invent__icontains=query)    
        ).select_related('categories', 'manufacturer')
        return object_list

class accessoriesCategoriesView(DataMixin, generic.ListView):
    template_name = 'consumables/accessories_list.html'
    model = Accessories.objects
    
    def get_context_data(self, *, object_list=None, **kwargs ):
        acc_cat = cache.get('acc_cat')
        if not acc_cat:
            acc_cat = Acc_cat.objects.all()
            cache.set('acc_cat', acc_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Комплектующие", searchlink='consumables:accessories_search',add='consumables:new-accessories', menu_categories=acc_cat)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        object_list = Accessories.objects.filter(categories__slug=self.kwargs['category_slug']).select_related('categories', 'manufacturer')
        return object_list        

class AccessoriesRestView(DataMixin, FormMessageMixin, viewsets.ModelViewSet):
    queryset = Accessories.objects.all()
    serializer_class = AccessoriesModelSerializer
    success_message = f"%(categories)s %(name)s успешно создано"
    error_message = f"%(categories)s %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Комплектующие")
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class Acc_catRestView(DataMixin, FormMessageMixin, viewsets.ModelViewSet):
    queryset = Acc_cat.objects.all()
    serializer_class = Acc_catModelSerializer
    success_message = f"Категория %(name)s успешно создана"
    error_message = f"Категория %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Категории")
        context = dict(list(context.items()) + list(c_def.items()))
        return context        

class accessoriesDetailView(DataMixin, FormMixin, generic.DetailView):
    model = Accessories
    template_name = 'consumables/accessories_detail.html'
    form_class = StockAddForm 

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Комплектующее",add='consumables:new-accessories',update='consumables:accessories-update',delete='consumables:accessories-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context 

class accessoriesCreate(DataMixin, FormMessageMixin, CreateView):
    model = Accessories
    form_class = accessoriesForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('consumables:accessories_list')
    success_message = f"Комплектующее %(name)s успешно создано"
    error_message = f"Комплектующее %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить комплектующее",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class accessoriesUpdate(DataMixin, FormMessageMixin, UpdateView):
    model = Accessories
    template_name = 'Forms/add.html'
    form_class = accessoriesForm
    success_url = reverse_lazy('consumables:accessories_list')
    success_message = f"Комплектующее %(name)s успешно обновлен"
    error_message = f"Комплектующее %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать комплектующее")
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class accessoriesDelete(DataMixin, FormMessageMixin, DeleteView):
    model = Accessories
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('consumables:accessories_list')
    success_message = f"Комплектующее успешно удален"
    error_message = f"Комплектующее не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить комплектующее",selflink='consumables:accessories_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context



