from .forms import printerForm
from stockroom.forms import ConsumableInstallForm
from .models import Printer, Categories
from django.views import generic
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from catalog.utils import *
from django.core.cache import cache

#Принтеры
class printerListView(DataMixin, generic.ListView):
    model = Printer
    template_name = 'printer/printer_list.html'
    
    
    def get_context_data(self, *, object_list=None, **kwargs):
        print_cat = cache.get('print_cat')
        if not print_cat:
            print_cat = Categories.objects.all()
            cache.aset('print_cat', print_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Принтеры", searchlink='printer:printer_search', add='printer:new-printer', menu_categories=print_cat)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = Printer.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(cartridge__name__icontains=query) |
                Q(fotoval__name__icontains=query) |
                Q(fotodrumm__name__icontains=query) |
                Q(toner__name__icontains=query) |
                Q(score__icontains=query) |   
                Q(workplace__name__icontains=query) |
                Q(workplace__room__name__icontains=query) |
                Q(workplace__room__floor__icontains=query) |
                Q(workplace__room__building__icontains=query) 
        ).select_related('manufacturer','categories', 'cartridge', 'fotoval', 'fotodrumm', 'toner', 'workplace', 'workplace__room')
        return object_list

class printerCategoryListView(DataMixin, generic.ListView):
    model = Printer.objects
    template_name = 'printer/printer_list.html'
    
    
    def get_context_data(self, *, object_list=None, **kwargs):
        print_cat = cache.get('print_cat')
        if not print_cat:
            print_cat = Categories.objects.all()
            cache.aset('print_cat', print_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Принтеры", searchlink='printer:printer_search', add='printer:new-printer', menu_categories=print_cat)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        object_list = Printer.objects.filter(categories__slug=self.kwargs['category_slug']).select_related('manufacturer', 'categories', 'cartridge', 'fotoval', 'fotodrumm', 'toner', 'workplace', 'workplace__room')
        return object_list 

class printerDetailView(DataMixin, FormMixin, generic.DetailView):
    model = Printer
    template_name = 'printer/printer_detail.html'
    form_class = ConsumableInstallForm
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Принтер",add='printer:new-printer',update='printer:printer-update',delete='printer:printer-delete',)
        context = dict(list(context.items()) + list(c_def.items()))
        context['detailMenu'] = printerMenu
        return context

class printerCreate(DataMixin, CreateView):
    model = Printer
    form_class = printerForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('printer:printer_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить принтер",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class printerUpdate(DataMixin, UpdateView):
    model = Printer
    template_name = 'Forms/add.html'
    form_class = printerForm
    success_url = reverse_lazy('printer:printer_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать принтер",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class printerDelete(DataMixin, DeleteView):
    model = Printer
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('printer:printer_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить принтер",selflink='printer:printer_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


