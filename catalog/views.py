from django.shortcuts import render
from .models import *
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from .utils import *

#Главная
class indexView(generic.ListView):
    model = digitalSignature
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['menu'] = menu
        return context

#Сотрудники 
class EmployeeListView(DataMixin, generic.ListView):
    model = Employee
    template_name = 'employee_list.html' 
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Список сотрудников", searchlink='employee')
        context = dict(list(context.items()) + list(c_def.items()))
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = Employee.objects.filter(
                Q(name__icontains=query) | 
                Q(sername__icontains=query) | 
                Q(family__icontains=query) | 
                Q(departament__name__icontains=query) |
                Q(post__name__icontains=query) |  
                Q(Workplace__name__icontains=query) |
                Q(Workplace__Room__name__icontains=query) |
                Q(Workplace__Floor__name__icontains=query) |
                Q(Workplace__Building__name__icontains=query) 
        )
        return object_list

#Рабочие места
class WorkplaceListView(DataMixin, generic.ListView):
    model = Workplace
    template_name = 'workplace_list.html'
  
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Рабочие места", searchlink='workplace')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = Workplace.objects.filter(
                Q(name__icontains=query) |
                Q(Room__name__icontains=query) |
                Q(Floor__name__icontains=query) |
                Q(Building__name__icontains=query) 
        )
        return object_list

#Рабочие станции
class workstationListView(DataMixin, generic.ListView):
    model = workstation
    template_name = 'workstation_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Рабочие станции", searchlink='workstation',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = workstation.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__icontains=query) | 
                Q(Employee__name__icontains=query) |
                Q(Employee__sername__icontains=query) | 
                Q(Employee__family__icontains=query) |
                Q(Employee__post__name__icontains=query) |  
                Q(Employee__departament__name__icontains=query) | 
                Q(OS__name__icontains=query) |   
                Q(Workplace__name__icontains=query) |
                Q(Workplace__Room__name__icontains=query) |
                Q(Workplace__Floor__name__icontains=query) |
                Q(Workplace__Building__name__icontains=query) 
        )
        return object_list

class workstationDetailView(DataMixin, generic.DetailView):
    model = workstation

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Рабочая станция",)
        context = dict(list(context.items()) + list(c_def.items()))
        context['detailMenu'] = workstationMenu
        return context

#СОФТ
class softwareListView(DataMixin, generic.ListView):
    model = software
    template_name = 'software_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Список ПО", searchlink='software')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = software.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__icontains=query) | 
                Q(Employee__name__icontains=query) |
                Q(Employee__sername__icontains=query) | 
                Q(Employee__family__icontains=query) |
                Q(Employee__post__name__icontains=query) |  
                Q(Employee__departament__name__icontains=query) | 
                Q(workstation__name__icontains=query) |
                Q(workstation__OS__name__icontains=query) |   
                Q(workstation__Workplace__name__icontains=query) |
                Q(workstation__Workplace__Room__name__icontains=query) |
                Q(workstation__Workplace__Floor__name__icontains=query) |
                Q(workstation__Workplace__Building__name__icontains=query) 
        )
        return object_list

#Принтеры
class printerListView(DataMixin, generic.ListView):
    model = printer
    template_name = 'printer_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Принтеры", searchlink='printer')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = printer.objects.filter(
                Q(name__icontains=query) | 
                Q(manufactured__icontains=query) |
                Q(cartridge__name__icontains=query) |
                Q(paper__name__icontains=query) | 
                Q(Employee__name__icontains=query) |
                Q(Employee__sername__icontains=query) | 
                Q(Employee__family__icontains=query) |
                Q(Employee__post__name__icontains=query) |  
                Q(Employee__departament__name__icontains=query) | 
                Q(workstation__name__icontains=query) |
                Q(workstation__OS__name__icontains=query) |   
                Q(Workplace__name__icontains=query) |
                Q(Workplace__Room__name__icontains=query) |
                Q(Workplace__Floor__name__icontains=query) |
                Q(Workplace__Building__name__icontains=query) 
        )
        return object_list

def printer_list(request):
    return render(
        request,
        'printer_list.html',
        context={
            'printer_list.html':printer_list,
        }
    )

class printerDetailView(DataMixin, generic.DetailView):
    model = printer

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Принтер",)
        context = dict(list(context.items()) + list(c_def.items()))
        context['detailMenu'] = printerMenu
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
                Q(Employee__name__icontains=query) |
                Q(Employee__sername__icontains=query) | 
                Q(Employee__family__icontains=query) |
                Q(Employee__post__name__icontains=query) |  
                Q(Employee__departament__name__icontains=query) | 
                Q(workstation__name__icontains=query) |
                Q(workstation__OS__name__icontains=query) |   
                Q(Workplace__name__icontains=query) |
                Q(Workplace__Room__name__icontains=query) |
                Q(Workplace__Floor__name__icontains=query) |
                Q(Workplace__Building__name__icontains=query) 
        )
        return object_list





