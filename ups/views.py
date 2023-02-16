from .forms import cassetteForm, upsForm
from stockroom.forms import ConsumableInstallForm
from .models import Cassette, Ups
from django.views import generic
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from catalog.utils import *

#Блок питания
class upsListView(DataMixin, generic.ListView):
    model = Ups
    template_name = 'ups/ups_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="ИБП", searchlink='ups:ups',add='ups:new-ups')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = Ups.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(serial__icontains=query) | 
                Q(invent__icontains=query) | 
                Q(power__icontains=query) | 
                Q(voltage__icontains=query) |  
                Q(current__icontains=query) | 
                Q(accumulator__name__icontains=query) |
                Q(cassette__name__icontains=query) | 
                Q(score__icontains=query) 
        )
        return object_list

class upsDetailView(DataMixin, FormMixin, generic.DetailView):
    model = Ups
    template_name = 'ups/ups_detail.html'
    form_class = ConsumableInstallForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="ИБП",add='ups:new-ups',update='ups:ups-update',delete='ups:ups-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class upsCreate(DataMixin, CreateView):
    model = Ups
    form_class = upsForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('ups:ups')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить ИБП",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class upsUpdate(DataMixin, UpdateView):
    model = Ups
    template_name = 'Forms/add.html'
    form_class = upsForm
    success_url = reverse_lazy('ups:ups')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать ИБП",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class upsDelete(DataMixin, DeleteView):
    model = Ups
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('ups:ups')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить ИБП",selflink='ups:ups')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#кассеты
class cassetteListView(DataMixin, generic.ListView):
    model = Cassette
    template_name = 'ups/cassette_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Кассеты", searchlink='ups:cassette',add='ups:new-cassette')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = Cassette.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(serial__icontains=query) | 
                Q(invent__icontains=query) | 
                Q(power__icontains=query) | 
                Q(voltage__icontains=query) |  
                Q(current__icontains=query) | 
                Q(accumulator__name__icontains=query) | 
                Q(score__icontains=query) 
        )
        return object_list

class cassetteDetailView(DataMixin, FormMixin, generic.DetailView):
    model = Cassette
    template_name = 'ups/cassette_detail.html'
    form_class = ConsumableInstallForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Кассета",add='ups:new-cassette',update='ups:cassette-update',delete='ups:cassette-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class cassetteCreate(DataMixin, CreateView):
    model = Cassette
    form_class = cassetteForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('ups:cassette')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить кассету",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class cassetteUpdate(DataMixin, UpdateView):
    model = Cassette
    template_name = 'Forms/add.html'
    form_class = cassetteForm
    success_url = reverse_lazy('ups:cassette')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать кассету",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class cassetteDelete(DataMixin, DeleteView):
    model = Cassette
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('ups:cassette')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить кассету",selflink='ups:cassette')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


