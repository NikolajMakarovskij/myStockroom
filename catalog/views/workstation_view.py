from ..forms import *
from ..models.ups_model import *
from ..models.workstation_model import *
from django.views import generic
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ..utils import *

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
                Q(cpu__name__icontains=query) | 
                Q(gpu__name__icontains=query) | 
                Q(ram__name__icontains=query) | 
                Q(ssd__name__icontains=query) | 
                Q(hdd__name__icontains=query) | 
                Q(os__name__icontains=query) | 
                Q(dcpower__name__icontains=query) | 
                Q(keyBoard__name__icontains=query) | 
                Q(mouse__name__icontains=query) | 
                Q(ups__name__icontains=query) | 
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

#Процессор
class cpuListView(DataMixin, generic.ListView):
    model = cpu
    template_name = 'catalog/workstation/cpu_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="CPU", searchlink='cpu',add='new-cpu')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = cpu.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(serial__icontains=query) | 
                Q(invent__icontains=query) | 
                Q(socket__icontains=query) | 
                Q(frequency__icontains=query) | 
                Q(l1__icontains=query) | 
                Q(l2__icontains=query) | 
                Q(l3__icontains=query) | 
                Q(core__icontains=query) | 
                Q(thread__icontains=query) | 
                Q(memory__icontains=query) | 
                Q(memoryCapacity__icontains=query) | 
                Q(channelsCapacity__icontains=query) | 
                Q(tdp__icontains=query) | 
                Q(supply__icontains=query) | 
                Q(score__icontains=query) 
        )
        return object_list

class cpuDetailView(DataMixin, generic.DetailView):
    model = cpu
    template_name = 'catalog/workstation/cpu_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="CPU",add='new-cpu',update='cpu-update',delete='cpu-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class cpuCreate(DataMixin, CreateView):
    model = cpu
    form_class = cpuForm
    template_name = 'Forms/add.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить CPU",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class cpuUpdate(DataMixin, UpdateView):
    model = cpu
    template_name = 'Forms/add.html'
    form_class = cpuForm
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать CPU",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class cpuDelete(DataMixin, DeleteView):
    model = cpu
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('cpu')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить CPU",selflink='cpu')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Видеокарта
class gpuListView(DataMixin, generic.ListView):
    model = gpu
    template_name = 'catalog/workstation/gpu_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="GPU", searchlink='gpu',add='new-gpu')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = gpu.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(type__icontains=query) | 
                Q(serial__icontains=query) | 
                Q(invent__icontains=query) | 
                Q(gram__icontains=query) | 
                Q(gramType__icontains=query) | 
                Q(pcie__icontains=query) | 
                Q(supply__icontains=query) | 
                Q(score__icontains=query) 
        )
        return object_list

class gpuDetailView(DataMixin, generic.DetailView):
    model = gpu
    template_name = 'catalog/workstation/gpu_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="GPU",add='new-gpu',update='gpu-update',delete='gpu-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class gpuCreate(DataMixin, CreateView):
    model = gpu
    form_class = gpuForm
    template_name = 'Forms/add.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить GPU",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class gpuUpdate(DataMixin, UpdateView):
    model = gpu
    template_name = 'Forms/add.html'
    form_class = gpuForm
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать GPU",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class gpuDelete(DataMixin, DeleteView):
    model = gpu
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('gpu')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить GPU",selflink='gpu')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Оперативная память
class ramListView(DataMixin, generic.ListView):
    model = ram
    template_name = 'catalog/workstation/ram_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="RAM", searchlink='ram',add='new-ram')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = ram.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(type__icontains=query) | 
                Q(serial__icontains=query) | 
                Q(invent__icontains=query) | 
                Q(ramCapacity__icontains=query) | 
                Q(rang__icontains=query) |  
                Q(score__icontains=query) 
        )
        return object_list

class ramDetailView(DataMixin, generic.DetailView):
    model = ram
    template_name = 'catalog/workstation/ram_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="RAM",add='new-ram',update='ram-update',delete='ram-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class ramCreate(DataMixin, CreateView):
    model = ram
    form_class = ramForm
    template_name = 'Forms/add.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить RAM",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class ramUpdate(DataMixin, UpdateView):
    model = ram
    template_name = 'Forms/add.html'
    form_class = ramForm
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать RAM",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class ramDelete(DataMixin, DeleteView):
    model = ram
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('ram')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить RAM",selflink='ram')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#SSD
class ssdListView(DataMixin, generic.ListView):
    model = ssd
    template_name = 'catalog/workstation/ssd_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="ssd", searchlink='ssd',add='new-ssd')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = ssd.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(type__icontains=query) | 
                Q(serial__icontains=query) | 
                Q(invent__icontains=query) | 
                Q(capacity__icontains=query) | 
                Q(plug__icontains=query) |  
                Q(speedRead__icontains=query) | 
                Q(speadWrite__icontains=query) | 
                Q(resourse__icontains=query) | 
                Q(score__icontains=query) 
        )
        return object_list

class ssdDetailView(DataMixin, generic.DetailView):
    model = ssd
    template_name = 'catalog/workstation/ssd_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="SSD",add='new-ssd',update='ssd-update',delete='ssd-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class ssdCreate(DataMixin, CreateView):
    model = ssd
    form_class = ssdForm
    template_name = 'Forms/add.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить SSD",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class ssdUpdate(DataMixin, UpdateView):
    model = ssd
    template_name = 'Forms/add.html'
    form_class = ssdForm
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать SSD",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class ssdDelete(DataMixin, DeleteView):
    model = ssd
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('ssd')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить SSD",selflink='ssd')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#HDD
class hddListView(DataMixin, generic.ListView):
    model = hdd
    template_name = 'catalog/workstation/hdd_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="hdd", searchlink='hdd',add='new-hdd')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = hdd.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(serial__icontains=query) | 
                Q(invent__icontains=query) | 
                Q(capacity__icontains=query) | 
                Q(plug__icontains=query) |  
                Q(speedRead__icontains=query) | 
                Q(speadWrite__icontains=query) | 
                Q(rpm__icontains=query) | 
                Q(score__icontains=query) 
        )
        return object_list

class hddDetailView(DataMixin, generic.DetailView):
    model = hdd
    template_name = 'catalog/workstation/hdd_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="HDD",add='new-hdd',update='hdd-update',delete='hdd-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class hddCreate(DataMixin, CreateView):
    model = hdd
    form_class = hddForm
    template_name = 'Forms/add.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить HHD",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class hddUpdate(DataMixin, UpdateView):
    model = hdd
    template_name = 'Forms/add.html'
    form_class = hddForm
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать HDD",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class hddDelete(DataMixin, DeleteView):
    model = hdd
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('hdd')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить HDD",selflink='hdd')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Блок питания
class dcpowerListView(DataMixin, generic.ListView):
    model = dcpower
    template_name = 'catalog/workstation/dcpower_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Блоки питания", searchlink='dcpower',add='new-dcpower')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = dcpower.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(serial__icontains=query) | 
                Q(invent__icontains=query) | 
                Q(power__icontains=query) | 
                Q(motherboard__icontains=query) |  
                Q(cpu__icontains=query) | 
                Q(gpu__icontains=query) | 
                Q(sata__icontains=query) | 
                Q(molex__icontains=query) | 
                Q(score__icontains=query) 
        )
        return object_list

class dcpowerDetailView(DataMixin, generic.DetailView):
    model = dcpower
    template_name = 'catalog/workstation/dcpower_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Блок питания",add='new-dcpower',update='dcpower-update',delete='dcpower-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class dcpowerCreate(DataMixin, CreateView):
    model = dcpower
    form_class = dcpowerForm
    template_name = 'Forms/add.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить блок питания",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class dcpowerUpdate(DataMixin, UpdateView):
    model = dcpower
    template_name = 'Forms/add.html'
    form_class = dcpowerForm
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать блок питания",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class dcpowerDelete(DataMixin, DeleteView):
    model = dcpower
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('dcpower')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить блок питания",selflink='dcpower')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Клавиатура
class keyBoardListView(DataMixin, generic.ListView):
    model = keyBoard
    template_name = 'catalog/workstation/keyBoard_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Клавиатуры", searchlink='keyBoard',add='new-keyBoard')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = keyBoard.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(serial__icontains=query) | 
                Q(invent__icontains=query) | 
                Q(score__icontains=query) 
        )
        return object_list

class keyBoardDetailView(DataMixin, generic.DetailView):
    model = keyBoard
    template_name = 'catalog/workstation/keyBoard_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Клавиатура",add='new-keyBoard',update='keyBoard-update',delete='keyBoard-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class keyBoardCreate(DataMixin, CreateView):
    model = keyBoard
    form_class = keyBoardForm
    template_name = 'Forms/add.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить клавиатуру",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class keyBoardUpdate(DataMixin, UpdateView):
    model = keyBoard
    template_name = 'Forms/add.html'
    form_class = keyBoardForm
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать клавиатуру",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class keyBoardDelete(DataMixin, DeleteView):
    model = keyBoard
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('keyBoard')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить клавиатуру",selflink='keyBoard')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Мышь
class mouseListView(DataMixin, generic.ListView):
    model = mouse
    template_name = 'catalog/workstation/mouse_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Мыши", searchlink='mouse',add='new-mouse')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = mouse.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(serial__icontains=query) | 
                Q(invent__icontains=query) |  
                Q(score__icontains=query) 
        )
        return object_list

class mouseDetailView(DataMixin, generic.DetailView):
    model = mouse
    template_name = 'catalog/workstation/mouse_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Мышь",add='new-mouse',update='mouse-update',delete='mouse-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class mouseCreate(DataMixin, CreateView):
    model = mouse
    form_class = mouseForm
    template_name = 'Forms/add.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить мышь",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class mouseUpdate(DataMixin, UpdateView):
    model = mouse
    template_name = 'Forms/add.html'
    form_class = mouseForm
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать мышь",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class mouseDelete(DataMixin, DeleteView):
    model = mouse
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('mouse')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить мышь",selflink='mouse')
        context = dict(list(context.items()) + list(c_def.items()))
        return context