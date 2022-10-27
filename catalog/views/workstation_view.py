from catalog.models.workstation_model import monitor
from ..forms import *
from ..models.models import *
from django.views import generic
from django.db.models import Q
from ..utils import *
from .workplace_view import *
from .employee_view import *
from .software_view import *

#Рабочие станции
class workstationListView(DataMixin, generic.ListView):
    model = workstation
    template_name = 'catalog/workstation/workstation_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Рабочие станции", searchlink='workstation',add='new-workstation')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = workstation.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(modelComputer__icontains=query) | 
                Q(serial__icontains=query) | 
                Q(invent__icontains=query) | 
                Q(motherboard__name__icontains=query) | 
                Q(monitor__name__icontains=query) | 
                Q(cpu__icontains=query) | 
                Q(gpu__icontains=query) | 
                Q(ram__icontains=query) | 
                Q(ssd__icontains=query) | 
                Q(hdd__icontains=query) | 
                Q(os__name__icontains=query) | 
                Q(dcpower__icontains=query) | 
                Q(keyBoard__icontains=query) | 
                Q(mouse__icontains=query) | 
                Q(ups__icontains=query) | 
                Q(employee__name__icontains=query) |
                Q(employee__sername__icontains=query) | 
                Q(employee__family__icontains=query) |
                Q(employee__post__name__icontains=query) |  
                Q(employee__post__departament__name__icontains=query) | 
                Q(os__name__icontains=query) |   
                Q(workplace__name__icontains=query) |
                Q(workplace__room__name__icontains=query) |
                Q(workplace__room__floor__icontains=query) |
                Q(workplace__room__building__icontains=query) 
        )
        return object_list

class workstationDetailView(DataMixin, generic.DetailView):
    model = workstation
    template_name = 'catalog/workstation/workstation_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Рабочая станция",add='new-workstation',update='workstation-update',delete='workstation-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class workstationCreate(DataMixin, CreateView):
    model = workstation
    form_class = workstationForm
    template_name = 'Forms/add.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить рабочую станцию",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class workstationUpdate(DataMixin, UpdateView):
    model = workstation
    template_name = 'Forms/add.html'
    form_class = workstationForm
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать рабочую станцию",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class workstationDelete(DataMixin, DeleteView):
    model = workstation
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('workstation')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить рабочую станцию",selflink='workstation')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Монитор
class monitorListView(DataMixin, generic.ListView):
    model = monitor
    template_name = 'catalog/workstation/monitor_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Мониторы", searchlink='monitor',add='new-monitor')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = monitor.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(serial__icontains=query) | 
                Q(invent__icontains=query) | 
                Q(resolution__icontains=query) | 
                Q(frequency__icontains=query) | 
                Q(typeDisplay__icontains=query) | 
                Q(dpi__icontains=query) | 
                Q(usbPort__icontains=query) | 
                Q(hdmi__icontains=query) | 
                Q(vga__icontains=query) | 
                Q(dvi__icontains=query) | 
                Q(displayPort__icontains=query) 
        )
        return object_list

class monitorDetailView(DataMixin, generic.DetailView):
    model = monitor
    template_name = 'catalog/workstation/monitor_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Монитор",add='new-monitor',update='monitor-update',delete='monitor-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class monitorCreate(DataMixin, CreateView):
    model = monitor
    form_class = monitorForm
    template_name = 'Forms/add.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить монитор",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class monitorUpdate(DataMixin, UpdateView):
    model = monitor
    template_name = 'Forms/add.html'
    form_class = monitorForm
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать монитор",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class monitorDelete(DataMixin, DeleteView):
    model = monitor
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('monitor')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить монитор",selflink='monitor')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Материнская плата
class motherboardListView(DataMixin, generic.ListView):
    model = motherboard
    template_name = 'catalog/workstation/motherboard_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Материнские платы", searchlink='motherboard',add='new-motherboard')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = motherboard.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(serial__icontains=query) | 
                Q(invent__icontains=query) | 
                Q(cpuSoket__icontains=query) | 
                Q(ramSlot__icontains=query) | 
                Q(usb_2__icontains=query) | 
                Q(usb_3__icontains=query) | 
                Q(usb_3_1__icontains=query) | 
                Q(usb_3_2__icontains=query) | 
                Q(usb_4_0__icontains=query) | 
                Q(comPort__icontains=query) | 
                Q(pcie_x1__icontains=query) |
                Q(pcie_x16__icontains=query) |
                Q(pci__icontains=query) |
                Q(sata__icontains=query) |
                Q(m2__icontains=query) |
                Q(vga__icontains=query) |
                Q(hdmi__icontains=query) |
                Q(dvi__icontains=query) |
                Q(dispayPort__icontains=query) |
                Q(powerSupply__icontains=query) |
                Q(powerSupplyCPU__icontains=query) 
        )
        return object_list

class motherboardDetailView(DataMixin, generic.DetailView):
    model = motherboard
    template_name = 'catalog/workstation/motherboard_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Материнская плата",add='new-motherboard',update='motherboard-update',delete='motherboard-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class motherboardCreate(DataMixin, CreateView):
    model = motherboard
    form_class = motherboardForm
    template_name = 'Forms/add.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить маткринскую плату",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class motherboardUpdate(DataMixin, UpdateView):
    model = motherboard
    template_name = 'Forms/add.html'
    form_class = motherboardForm
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать маткринскую плату",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class motherboardDelete(DataMixin, DeleteView):
    model = motherboard
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('motherboard')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить маткринскую плату",selflink='motherboard')
        context = dict(list(context.items()) + list(c_def.items()))
        return context