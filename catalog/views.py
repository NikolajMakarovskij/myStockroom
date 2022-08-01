from unicodedata import name
from django.shortcuts import render
from .models import *
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib import messages

n = [digitalSignature.validateP]
m = [digitalSignature.validateP]

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    if n == m:
            messages.add_message(request, messages.INFO,  'Проверка' )

    return render(
        request,
        'index.html',
        context={
            'title': 'Главная страница',
            'menu': menu,

        }, 
    )

menu = [
    {'title':  "Главная страница", 'url_name': 'index'},
    {'title':  "Раб. места", 'url_name': 'workplace'},
    {'title':  "Сотрудники", 'url_name': 'employee'},
    {'title':  "Софт", 'url_name': 'software'},
    {'title':  "Раб. станции", 'url_name': 'workstation'},
    {'title':  "Принтеры", 'url_name': 'printer'},
    {'title':  "ЭЦП", 'url_name': 'digital-signature'},
    ]

class EmployeeListView(generic.ListView):
    model = Employee
    paginate_by =  10
    

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Сотрудники'
        context['menu'] = menu
        return context

def employee_list(request): 
    return render(
        request,
        'employee_list.html',
        context={

        }
    )

class WorkplaceListView(generic.ListView):
    model = Workplace
    paginate_by =  10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Рабочие места'
        context['menu'] = menu
        return context

def workplace_list(request): 
    return render(
        request,
        'workplace_list.html',
        context={
            
        }
    )

class workstationListView(generic.ListView):
    model = workstation
    paginate_by =  10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Рабочие станции'
        context['menu'] = menu
        return context

def workstation_list(request): 
    return render(
        request,
        'workstation_list.html',
        context={
            'workstation_list.html':workstation_list,
        }
    )

workstationMenu = [
    {'title':  "Информация о системе", 'anchor': '#systemInfo'},
    {'title':  "Информация об ОС", 'anchor': '#OSInfo'},
    {'title':  "Информация о сотруднике", 'anchor': '#infoEmployee'},
    {'title':  "Монитор", 'anchor': '#monitor'},
    {'title':  "Материнская плата", 'anchor': '#motherboard'},
    ]

class workstationDetailView(generic.DetailView):
    model = workstation

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Рабочая станция №'
        context['menu'] = menu
        context['workstationMenu'] = workstationMenu
        return context

def workstation_detail_view(request,pk):
    try:
        workstation_id=workstation.objects.get(pk=pk)
    except workstation.DoesNotExist:
        raise Http404("Не удалось найти детальную информацию")

    return render(
        request,
        'catalog/workstation_detail.html',
        context={
            'workstation': workstation_id,
            }

    )

class softwareListView(generic.ListView):
    model = software
    paginate_by =  10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Програмное обеспечение'
        context['menu'] = menu
        return context

def software_list(request):
    return render(
        request,
        'software_list.html',
        context={
            'software_list.html':software_list,
        }
    )

class printerListView(generic.ListView):
    model = printer
    paginate_by =  10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Принтеры'
        context['menu'] = menu
        return context

def printer_list(request):
    return render(
        request,
        'printer_list.html',
        context={
            'printer_list.html':printer_list,
        }
    )

printerMenu = [
    {'title':  "Информация о принтере", 'anchor': '#printerInfo'},
    {'title':  "Информация о картридже", 'anchor': '#cartridgeInfo'},
    {'title':  "Информация о бумаге", 'anchor': '#paperInfo'},
    {'title':  "Местоположение", 'anchor': '#workplaceInfo'},
    ]

class printerDetailView(generic.DetailView):
    model = printer

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Принтер №'
        context['menu'] = menu
        context['printerMenu'] = printerMenu
        return context

def printer_detail_view(request,pk):
    try:
        printer_id=printer.objects.get(pk=pk)
    except printer.DoesNotExist:
        raise Http404("Не удалось найти детальную информацию")

    return render(
        request,
        'catalog/printer_detail.html',
        context={

            }
    )

class digitalSignatureListView(generic.ListView):
    model = digitalSignature
    paginate_by =  10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Цифровые подписи'
        context['menu'] = menu
        context['index.html']:digital_signature_list
        return context

def digital_signature_list(request):
    return render(
        request,
        'digital_signature_list.html',
        context={
            'digital_signature_list.html':digital_signature_list,
            'index.html':digital_signature_list,
        }
    )



