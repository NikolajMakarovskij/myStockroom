from .forms import cartridgeForm, fotovalForm, tonerForm, accumulatorForm, storageForm
from .models import Cartridge, Fotoval, Toner, Accumulator, Storage
from django.views import generic
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from catalog.utils import *
from catalog.models import References
from stockroom.forms import StockAddForm, StockAddForm

#Расходники
class consumablesView(DataMixin, generic.ListView):
    template_name = 'consumables/consumables.html'
    model = References

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Расходники", searchlink='references',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Картриджы
class cartridgeListView(DataMixin, generic.ListView):
    model = Cartridge
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
        object_list = Cartridge.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(buhCode__icontains=query) |
                Q(score__icontains=query) |
                Q(rack__icontains=query) |
                Q(shelf__icontains=query)    
        )
        return object_list

class cartridgeDetailView(DataMixin, FormMixin, generic.DetailView):
    model = Cartridge
    template_name = 'consumables/cartridge_detail.html'
    form_class = StockAddForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Картридж",add='consumables:new-cartridge',update='consumables:cartridge-update',delete='consumables:cartridge-delete',)# addtostock='consumables:add-to-stock')
        context = dict(list(context.items()) + list(c_def.items()))
        return context 

class cartridgeCreate(DataMixin,CreateView):
    model = Cartridge
    form_class = cartridgeForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('consumables:cartridge_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить картридж",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class cartridgeUpdate(DataMixin, UpdateView):
    model = Cartridge
    template_name = 'Forms/add.html'
    form_class = cartridgeForm
    success_url = reverse_lazy('consumables:cartridge_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать картридж",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class cartridgeDelete(DataMixin, DeleteView):
    model = Cartridge
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('consumables:cartridge_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить картридж",selflink='consumables:cartridge_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Фотовалы
class fotovalListView(DataMixin, generic.ListView):
    model = Fotoval
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
        object_list = Fotoval.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(mileage__icontains=query) |
                Q(buhCode__icontains=query) |
                Q(score__icontains=query) |
                Q(rack__icontains=query) |
                Q(shelf__icontains=query)  
        )
        return object_list

class fotovalDetailView(DataMixin, FormMixin, generic.DetailView):
    model = Fotoval
    template_name = 'consumables/fotoval_detail.html'
    form_class = StockAddForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Фотовал",add='consumables:new-fotoval',update='consumables:fotoval-update',delete='consumables:fotoval-delete',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class fotovalCreate(DataMixin, CreateView):
    model = Fotoval
    form_class = fotovalForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('consumables:fotoval_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить фотовал",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class fotovalUpdate(DataMixin, UpdateView):
    model = Fotoval
    template_name = 'Forms/add.html'
    form_class = fotovalForm
    success_url = reverse_lazy('consumables:fotoval_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать фотовал",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class fotovalDelete(DataMixin, DeleteView):
    model = Fotoval
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('consumables:fotoval_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить фотовал",selflink='consumables:fotoval_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Тонер
class tonerListView(DataMixin, generic.ListView):
    model = Toner
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
        object_list = Toner.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(buhCode__icontains=query) |
                Q(score__icontains=query) |
                Q(rack__icontains=query) |
                Q(shelf__icontains=query)    
        )
        return object_list

class tonerDetailView(DataMixin,FormMixin, generic.DetailView):
    model = Toner
    template_name = 'consumables/toner_detail.html'
    form_class = StockAddForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Тонер",add='consumables:new-toner',update='consumables:toner-update',delete='consumables:toner-delete',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class tonerCreate(DataMixin, CreateView):
    model = Toner
    form_class = tonerForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('consumables:toner_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить тонер",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class tonerUpdate(DataMixin, UpdateView):
    model = Toner
    template_name = 'Forms/add.html'
    form_class = tonerForm
    success_url = reverse_lazy('consumables:toner_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать тонер",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class tonerDelete(DataMixin, DeleteView):
    model = Toner
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('consumables:toner_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить тонер",selflink='consumables:toner_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#аккумуляторы
class accumulatorListView(DataMixin, generic.ListView):
    model = Accumulator
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
        object_list = Accumulator.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(power__icontains=query) | 
                Q(voltage__icontains=query) |  
                Q(current__icontains=query) | 
                Q(score__icontains=query) |
                Q(rack__icontains=query) |
                Q(shelf__icontains=query) 
        )
        return object_list

class accumulatorDetailView(DataMixin, FormMixin, generic.DetailView):
    model = Accumulator
    template_name = 'consumables/accumulator_detail.html'
    form_class = StockAddForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Аккумулятор",add='consumables:new-accumulator',update='consumables:accumulator-update',delete='consumables:accumulator-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class accumulatorCreate(DataMixin, CreateView):
    model = Accumulator
    form_class = accumulatorForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('consumables:accumulator_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить аккумулятор",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class accumulatorUpdate(DataMixin, UpdateView):
    model = Accumulator
    template_name = 'Forms/add.html'
    form_class = accumulatorForm
    success_url = reverse_lazy('consumables:accumulator_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать аккумулятор",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class accumulatorDelete(DataMixin, DeleteView):
    model = Accumulator
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('consumables:accumulator_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить аккумулятор",selflink='consumables:accumulator_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Накопитель
class storageListView(DataMixin, generic.ListView):
    model = Storage
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
        object_list = Storage.objects.filter(
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

class storageDetailView(DataMixin, FormMixin, generic.DetailView):
    model = Storage
    template_name = 'consumables/storage_detail.html'
    form_class = StockAddForm
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Накопитель",add='consumables:new-storage',update='consumables:storage-update',delete='consumables:storage-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class storageCreate(DataMixin, CreateView):
    model = Storage
    form_class = storageForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('consumables:storage_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить накопитель",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class storageUpdate(DataMixin, UpdateView):
    model = Storage
    template_name = 'Forms/add.html'
    form_class = storageForm
    success_url = reverse_lazy('consumables:storage_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать накопитель",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class storageDelete(DataMixin, DeleteView):
    model = Storage
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('consumables:storage_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить накопитель",selflink='consumables:storage_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context