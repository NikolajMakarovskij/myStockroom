from .forms import cartridgeForm, fotovalForm, tonerForm, accumulatorForm, storageForm
from .models import cartridge, fotoval, toner, accumulator, storage
from django.views import generic
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from catalog.utils import *
from catalog.models import references
from stockroom.forms import StockAddProductForm

#Расходники
class consumablesView(DataMixin, generic.ListView):
    template_name = 'consumables/consumables.html'
    model = references

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Расходники", searchlink='references',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Картриджы
class cartridgeListView(DataMixin, generic.ListView):
    model = cartridge
    template_name = 'consumables/cartridge_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Картриджы", searchlink='consumables:cartridge_list', add='consumables:new-cartridge')
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
    template_name = 'consumables/cartridge_detail.html'
    stock_product_form = StockAddProductForm()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Картридж",add='consumables:new-cartridge',update='consumables:cartridge-update',delete='consumables:cartridge-delete',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class cartridgeCreate(DataMixin, CreateView):
    model = cartridge
    form_class = cartridgeForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('consumables:cartridge_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить картридж",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class cartridgeUpdate(DataMixin, UpdateView):
    model = cartridge
    template_name = 'Forms/add.html'
    form_class = cartridgeForm
    success_url = reverse_lazy('consumables:cartridge_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать картридж",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class cartridgeDelete(DataMixin, DeleteView):
    model = cartridge
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('consumables:cartridge_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить картридж",selflink='consumables:cartridge_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Фотовалы
class fotovalListView(DataMixin, generic.ListView):
    model = fotoval
    template_name = 'consumables/fotoval_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Фотовалы", searchlink='consumables:fotoval_list', add='consumables:new-fotoval')
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
    template_name = 'consumables/fotoval_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Фотовал",add='consumables:new-fotoval',update='consumables:fotoval-update',delete='consumables:fotoval-delete',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class fotovalCreate(DataMixin, CreateView):
    model = fotoval
    form_class = fotovalForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('consumables:fotoval_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить фотовал",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class fotovalUpdate(DataMixin, UpdateView):
    model = fotoval
    template_name = 'Forms/add.html'
    form_class = fotovalForm
    success_url = reverse_lazy('consumables:fotoval_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать фотовал",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class fotovalDelete(DataMixin, DeleteView):
    model = fotoval
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('consumables:fotoval_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить фотовал",selflink='consumables:fotoval_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Тонер
class tonerListView(DataMixin, generic.ListView):
    model = toner
    template_name = 'consumables/toner_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Тонер", searchlink='consumables:toner_list', add='consumables:new-toner')
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
    template_name = 'consumables/toner_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Тонер",add='consumables:new-toner',update='consumables:toner-update',delete='consumables:toner-delete',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class tonerCreate(DataMixin, CreateView):
    model = toner
    form_class = tonerForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('consumables:toner_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить тонер",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class tonerUpdate(DataMixin, UpdateView):
    model = toner
    template_name = 'Forms/add.html'
    form_class = tonerForm
    success_url = reverse_lazy('consumables:toner_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать тонер",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class tonerDelete(DataMixin, DeleteView):
    model = toner
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('consumables:toner_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить тонер",selflink='consumables:toner_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#аккумуляторы
class accumulatorListView(DataMixin, generic.ListView):
    model = accumulator
    template_name = 'consumables/accumulator_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Аккумуляторы", searchlink='consumables:accumulator_list',add='consumables:new-accumulator')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = accumulator.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(power__icontains=query) | 
                Q(voltage__icontains=query) |  
                Q(current__icontains=query) | 
                Q(score__icontains=query) 
        )
        return object_list

class accumulatorDetailView(DataMixin, generic.DetailView):
    model = accumulator
    template_name = 'consumables/accumulator_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Аккумулятор",add='consumables:new-accumulator',update='consumables:accumulator-update',delete='consumables:accumulator-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class accumulatorCreate(DataMixin, CreateView):
    model = accumulator
    form_class = accumulatorForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('consumables:accumulator_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить аккумулятор",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class accumulatorUpdate(DataMixin, UpdateView):
    model = accumulator
    template_name = 'Forms/add.html'
    form_class = accumulatorForm
    success_url = reverse_lazy('consumables:accumulator_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать аккумулятор",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class accumulatorDelete(DataMixin, DeleteView):
    model = accumulator
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('consumables:accumulator_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить аккумулятор",selflink='consumables:accumulator_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Накопитель
class storageListView(DataMixin, generic.ListView):
    model = storage
    template_name = 'consumables/storage_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Список накопителей", searchlink='consumables:storage_list',add='consumables:new-storage',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = storage.objects.filter(
                Q(name__icontains=query) |
                Q(manufacturer__name__icontains=query) |
                Q(plug__icontains=query) |
                Q(typeMemory__icontains=query) |
                Q(volumeMemory__icontains=query) |
                Q(employee__name__icontains=query) |
                Q(plug__icontains=query) |
                Q(plug__icontains=query) |
                Q(modelStorage__icontains=query) 
        )
        return object_list

class storageDetailView(DataMixin, generic.DetailView):
    model = storage
    template_name = 'consumables/storage_detail.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Накопитель",add='consumables:new-storage',update='consumables:storage-update',delete='consumables:storage-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class storageCreate(DataMixin, CreateView):
    model = storage
    form_class = storageForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('consumables:storage_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить накопитель",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class storageUpdate(DataMixin, UpdateView):
    model = storage
    template_name = 'Forms/add.html'
    form_class = storageForm
    success_url = reverse_lazy('consumables:storage_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать накопитель",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class storageDelete(DataMixin, DeleteView):
    model = storage
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('consumables:storage_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить накопитель",selflink='consumables:storage_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context