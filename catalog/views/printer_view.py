from ..forms import printerForm, cartridgeForm, fotovalForm, tonerForm
from ..models.printer_model import *
from django.views import generic
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ..utils import *

#Принтеры
class printerListView(DataMixin, generic.ListView):
    model = printer
    template_name = 'catalog/printer/printer_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Принтеры", searchlink='printer', add='new-printer')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = printer.objects.filter(
                Q(name__icontains=query) | 
                Q(modelPrinter__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(cartridge__name__icontains=query) |
                Q(fotoval__name__icontains=query) |
                Q(fotoval__mileage__icontains=query) |
                Q(toner__name__icontains=query) |
                Q(score__icontains=query) |   
                Q(workplace__name__icontains=query) |
                Q(workplace__room__name__icontains=query) |
                Q(workplace__room__floor__icontains=query) |
                Q(workplace__room__building__icontains=query) 
        )
        return object_list

class printerDetailView(DataMixin, generic.DetailView):
    model = printer
    template_name = 'catalog/printer/printer_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Принтер",add='new-printer',update='printer-update',delete='printer-delete',)
        context = dict(list(context.items()) + list(c_def.items()))
        context['detailMenu'] = printerMenu
        return context

class printerCreate(DataMixin, CreateView):
    model = printer
    form_class = printerForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('printer')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить принтер",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class printerUpdate(DataMixin, UpdateView):
    model = printer
    template_name = 'Forms/add.html'
    form_class = printerForm
    success_url = reverse_lazy('printer')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать принтер",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class printerDelete(DataMixin, DeleteView):
    model = printer
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('printer')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить принтер",selflink='printer')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Картриджы
class cartridgeListView(DataMixin, generic.ListView):
    model = cartridge
    template_name = 'catalog/printer/cartridge_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Картриджы", searchlink='cartridge', add='new-cartridge')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = cartridge.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(buhCode__icontains=query) |
                Q(score__icontains=query)    
        )
        return object_list

class cartridgeDetailView(DataMixin, generic.DetailView):
    model = cartridge
    template_name = 'catalog/printer/cartridge_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Картридж",add='new-cartridge',update='cartridge-update',delete='cartridge-delete',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class cartridgeCreate(DataMixin, CreateView):
    model = cartridge
    form_class = cartridgeForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('cartridge')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить картридж",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class cartridgeUpdate(DataMixin, UpdateView):
    model = cartridge
    template_name = 'Forms/add.html'
    form_class = cartridgeForm
    success_url = reverse_lazy('cartridge')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать картридж",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class cartridgeDelete(DataMixin, DeleteView):
    model = cartridge
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('cartridge')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить картридж",selflink='cartridge')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Фотовалы
class fotovalListView(DataMixin, generic.ListView):
    model = fotoval
    template_name = 'catalog/printer/fotoval_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Фотовалы", searchlink='fotoval', add='new-fotoval')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = fotoval.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(mileage__icontains=query) |
                Q(buhCode__icontains=query) |
                Q(score__icontains=query)    
        )
        return object_list

class fotovalDetailView(DataMixin, generic.DetailView):
    model = fotoval
    template_name = 'catalog/printer/fotoval_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Фотовал",add='new-fotoval',update='fotoval-update',delete='fotoval-delete',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class fotovalCreate(DataMixin, CreateView):
    model = fotoval
    form_class = fotovalForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('fotoval')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить фотовал",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class fotovalUpdate(DataMixin, UpdateView):
    model = fotoval
    template_name = 'Forms/add.html'
    form_class = fotovalForm
    success_url = reverse_lazy('fotoval')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать фотовал",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class fotovalDelete(DataMixin, DeleteView):
    model = fotoval
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('fotoval')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить фотовал",selflink='fotoval')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Тонер
class tonerListView(DataMixin, generic.ListView):
    model = toner
    template_name = 'catalog/printer/toner_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Тонер", searchlink='toner', add='new-toner')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = toner.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(buhCode__icontains=query) |
                Q(score__icontains=query)    
        )
        return object_list

class tonerDetailView(DataMixin, generic.DetailView):
    model = toner
    template_name = 'catalog/printer/toner_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Тонер",add='new-toner',update='toner-update',delete='toner-delete',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class tonerCreate(DataMixin, CreateView):
    model = toner
    form_class = tonerForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('toner')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить тонер",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class tonerUpdate(DataMixin, UpdateView):
    model = toner
    template_name = 'Forms/add.html'
    form_class = tonerForm
    success_url = reverse_lazy('toner')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать тонер",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class tonerDelete(DataMixin, DeleteView):
    model = toner
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('toner')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить тонер",selflink='toner')
        context = dict(list(context.items()) + list(c_def.items()))
        return context