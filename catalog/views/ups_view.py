from ..forms import *
from ..models.ups_model import *
from django.views import generic
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ..utils import *

#Блок питания
class upsListView(DataMixin, generic.ListView):
    model = ups
    template_name = 'catalog/ups/ups_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="ИБП", searchlink='ups',add='new-ups')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = ups.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(serial__icontains=query) | 
                Q(invent__icontains=query) | 
                Q(power__icontains=query) | 
                Q(voltage__icontains=query) |  
                Q(current__icontains=query) | 
                Q(accumulator1__name__icontains=query) |
                Q(accumulator2__name__icontains=query) |
                Q(accumulator3__name__icontains=query) |
                Q(accumulator4__name__icontains=query) | 
                Q(cassette1__name__icontains=query) | 
                Q(cassette2__name__icontains=query) |
                Q(cassette3__name__icontains=query) |
                Q(cassette4__name__icontains=query) |
                Q(score__icontains=query) 
        )
        return object_list

class upsDetailView(DataMixin, generic.DetailView):
    model = ups
    template_name = 'catalog/ups/ups_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="ИБП",add='new-ups',update='ups-update',delete='ups-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class upsCreate(DataMixin, CreateView):
    model = ups
    form_class = upsForm
    template_name = 'Forms/add.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить ИБП",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class upsUpdate(DataMixin, UpdateView):
    model = ups
    template_name = 'Forms/add.html'
    form_class = upsForm
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать ИБП",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class upsDelete(DataMixin, DeleteView):
    model = ups
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('ups')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить ИБП",selflink='ups')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#кассеты
class cassetteListView(DataMixin, generic.ListView):
    model = cassette
    template_name = 'catalog/ups/cassette_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Кассеты", searchlink='cassette',add='new-cassette')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = cassette.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(serial__icontains=query) | 
                Q(invent__icontains=query) | 
                Q(power__icontains=query) | 
                Q(voltage__icontains=query) |  
                Q(current__icontains=query) | 
                Q(accumulator1__name__icontains=query) | 
                Q(accumulator2__name__icontains=query) | 
                Q(accumulator3__name__icontains=query) | 
                Q(accumulator4__name__icontains=query) | 
                Q(accumulator5__name__icontains=query) | 
                Q(accumulator6__name__icontains=query) | 
                Q(accumulator7__name__icontains=query) | 
                Q(accumulator8__name__icontains=query) | 
                Q(accumulator9__name__icontains=query) | 
                Q(accumulator10__name__icontains=query) | 
                Q(score__icontains=query) 
        )
        return object_list

class cassetteDetailView(DataMixin, generic.DetailView):
    model = cassette
    template_name = 'catalog/ups/cassette_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Кассета",add='new-cassette',update='cassette-update',delete='cassette-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class cassetteCreate(DataMixin, CreateView):
    model = cassette
    form_class = cassetteForm
    template_name = 'Forms/add.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить кассету",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class cassetteUpdate(DataMixin, UpdateView):
    model = cassette
    template_name = 'Forms/add.html'
    form_class = cassetteForm
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать кассету",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class cassetteDelete(DataMixin, DeleteView):
    model = cassette
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('cassette')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить кассету",selflink='cassette')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#аккумуляторы
class accumulatorListView(DataMixin, generic.ListView):
    model = accumulator
    template_name = 'catalog/ups/accumulator_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Аккумуляторы", searchlink='accumulator',add='new-accumulator')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = accumulator.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(serial__icontains=query) | 
                Q(invent__icontains=query) | 
                Q(power__icontains=query) | 
                Q(voltage__icontains=query) |  
                Q(current__icontains=query) | 
                Q(score__icontains=query) 
        )
        return object_list

class accumulatorDetailView(DataMixin, generic.DetailView):
    model = accumulator
    template_name = 'catalog/ups/accumulator_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Аккумулятор",add='new-accumulator',update='accumulator-update',delete='accumulator-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class accumulatorCreate(DataMixin, CreateView):
    model = accumulator
    form_class = accumulatorForm
    template_name = 'Forms/add.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить аккумулятор",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class accumulatorUpdate(DataMixin, UpdateView):
    model = accumulator
    template_name = 'Forms/add.html'
    form_class = accumulatorForm
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать аккумулятор",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class accumulatorDelete(DataMixin, DeleteView):
    model = accumulator
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('accumulator')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить аккумулятор",selflink='accumulator')
        context = dict(list(context.items()) + list(c_def.items()))
        return context