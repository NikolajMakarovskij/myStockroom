from .forms import *
from catalog.models.ups_model import *
from .models import *
from django.views import generic
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from catalog.utils import *



#Рабочие станции
class workstationListView(DataMixin, generic.ListView):
    model = workstation
    template_name = 'workstation/workstation_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Рабочие станции", searchlink='workstation:workstation',add='workstation:new-workstation')
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
                Q(software__name__icontains=query)|  
                Q(workplace__name__icontains=query) |
                Q(workplace__room__name__icontains=query) |
                Q(workplace__room__floor__icontains=query) |
                Q(workplace__room__building__icontains=query) 
        )
        return object_list

class workstationDetailView(DataMixin, generic.DetailView):
    model = workstation
    template_name = 'workstation/workstation_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Рабочая станция",add='workstation:new-workstation',update='workstation:workstation-update',delete='workstation:workstation-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class workstationCreate(DataMixin, CreateView):
    model = workstation
    form_class = workstationForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('workstation:workstation')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить рабочую станцию",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class workstationUpdate(DataMixin, UpdateView):
    model = workstation
    template_name = 'Forms/add.html'
    form_class = workstationForm
    success_url = reverse_lazy('workstation:workstation')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать рабочую станцию",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class workstationDelete(DataMixin, DeleteView):
    model = workstation
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('workstation:workstation')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить рабочую станцию",selflink='workstation:workstation')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Монитор
class monitorListView(DataMixin, generic.ListView):
    model = monitor
    template_name = 'workstation/monitor_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Мониторы", searchlink='workstation:monitor',add='workstation:new-monitor')
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
    template_name = 'workstation/monitor_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Монитор",add='workstation:new-monitor',update='workstation:monitor-update',delete='workstation:monitor-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class monitorCreate(DataMixin, CreateView):
    model = monitor
    form_class = monitorForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('workstation:monitor')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить монитор",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class monitorUpdate(DataMixin, UpdateView):
    model = monitor
    template_name = 'Forms/add.html'
    form_class = monitorForm
    success_url = reverse_lazy('workstation:monitor')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать монитор",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class monitorDelete(DataMixin, DeleteView):
    model = monitor
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('workstation:monitor')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить монитор",selflink='workstation:monitor')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Материнская плата
class motherboardListView(DataMixin, generic.ListView):
    model = motherboard
    template_name = 'workstation/motherboard_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Материнские платы", searchlink='workstation:motherboard',add='workstation:new-motherboard')
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
    template_name = 'workstation/motherboard_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Материнская плата",add='workstation:new-motherboard',update='workstation:motherboard-update',delete='workstation:motherboard-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class motherboardCreate(DataMixin, CreateView):
    model = motherboard
    form_class = motherboardForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('workstation:motherboard')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить маткринскую плату",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class motherboardUpdate(DataMixin, UpdateView):
    model = motherboard
    template_name = 'Forms/add.html'
    form_class = motherboardForm
    success_url = reverse_lazy('workstation:motherboard')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать маткринскую плату",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class motherboardDelete(DataMixin, DeleteView):
    model = motherboard
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('workstation:motherboard')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить маткринскую плату",selflink='workstation:motherboard')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Процессор
class cpuListView(DataMixin, generic.ListView):
    model = cpu
    template_name = 'workstation/cpu_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="CPU", searchlink='workstation:cpu',add='workstation:new-cpu')
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
    template_name = 'workstation/cpu_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="CPU",add='workstation:new-cpu',update='workstation:cpu-update',delete='workstation:cpu-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class cpuCreate(DataMixin, CreateView):
    model = cpu
    form_class = cpuForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('workstation:cpu')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить CPU",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class cpuUpdate(DataMixin, UpdateView):
    model = cpu
    template_name = 'Forms/add.html'
    form_class = cpuForm
    success_url = reverse_lazy('workstation:cpu')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать CPU",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class cpuDelete(DataMixin, DeleteView):
    model = cpu
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('workstation:cpu')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить CPU",selflink='workstation:cpu')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Видеокарта
class gpuListView(DataMixin, generic.ListView):
    model = gpu
    template_name = 'workstation/gpu_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="GPU", searchlink='workstation:gpu',add='workstation:new-gpu')
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
    template_name = 'workstation/gpu_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="GPU",add='workstation:new-gpu',update='workstation:gpu-update',delete='workstation:gpu-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class gpuCreate(DataMixin, CreateView):
    model = gpu
    form_class = gpuForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('workstation:gpu')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить GPU",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class gpuUpdate(DataMixin, UpdateView):
    model = gpu
    template_name = 'Forms/add.html'
    form_class = gpuForm
    success_url = reverse_lazy('workstation:gpu')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать GPU",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class gpuDelete(DataMixin, DeleteView):
    model = gpu
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('workstation:gpu')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить GPU",selflink='workstation:gpu')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Оперативная память
class ramListView(DataMixin, generic.ListView):
    model = ram
    template_name = 'workstation/ram_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="RAM", searchlink='workstation:ram',add='workstation:new-ram')
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
    template_name = 'workstation/ram_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="RAM",add='workstation:new-ram',update='workstation:ram-update',delete='workstation:ram-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class ramCreate(DataMixin, CreateView):
    model = ram
    form_class = ramForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('workstation:ram')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить RAM",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class ramUpdate(DataMixin, UpdateView):
    model = ram
    template_name = 'Forms/add.html'
    form_class = ramForm
    success_url = reverse_lazy('workstation:ram')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать RAM",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class ramDelete(DataMixin, DeleteView):
    model = ram
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('workstation:ram')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить RAM",selflink='workstation:ram')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#SSD
class ssdListView(DataMixin, generic.ListView):
    model = ssd
    template_name = 'workstation/ssd_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="ssd", searchlink='workstation:ssd',add='workstation:new-ssd')
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
    template_name = 'workstation/ssd_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="SSD",add='workstation:new-ssd',update='workstation:ssd-update',delete='workstation:ssd-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class ssdCreate(DataMixin, CreateView):
    model = ssd
    form_class = ssdForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('workstation:ssd')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить SSD",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class ssdUpdate(DataMixin, UpdateView):
    model = ssd
    template_name = 'Forms/add.html'
    form_class = ssdForm
    success_url = reverse_lazy('workstation:ssd')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать SSD",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class ssdDelete(DataMixin, DeleteView):
    model = ssd
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('workstation:ssd')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить SSD",selflink='workstation:ssd')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#HDD
class hddListView(DataMixin, generic.ListView):
    model = hdd
    template_name = 'workstation/hdd_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="hdd", searchlink='workstation:hdd',add='workstation:new-hdd')
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
    template_name = 'workstation/hdd_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="HDD",add='workstation:new-hdd',update='workstation:hdd-update',delete='workstation:hdd-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class hddCreate(DataMixin, CreateView):
    model = hdd
    form_class = hddForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('workstation:hdd')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить HHD",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class hddUpdate(DataMixin, UpdateView):
    model = hdd
    template_name = 'Forms/add.html'
    form_class = hddForm
    success_url = reverse_lazy('workstation:hdd')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать HDD",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class hddDelete(DataMixin, DeleteView):
    model = hdd
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('workstation:hdd')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить HDD",selflink='workstation:hdd')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Блок питания
class dcpowerListView(DataMixin, generic.ListView):
    model = dcpower
    template_name = 'workstation/dcpower_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Блоки питания", searchlink='workstation:dcpower',add='workstation:new-dcpower')
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
    template_name = 'workstation/dcpower_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Блок питания",add='workstation:new-dcpower',update='workstation:dcpower-update',delete='workstation:dcpower-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class dcpowerCreate(DataMixin, CreateView):
    model = dcpower
    form_class = dcpowerForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('workstation:dcpower')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить блок питания",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class dcpowerUpdate(DataMixin, UpdateView):
    model = dcpower
    template_name = 'Forms/add.html'
    form_class = dcpowerForm
    success_url = reverse_lazy('workstation:dcpower')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать блок питания",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class dcpowerDelete(DataMixin, DeleteView):
    model = dcpower
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('workstation:dcpower')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить блок питания",selflink='workstation:dcpower')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Клавиатура
class keyBoardListView(DataMixin, generic.ListView):
    model = keyBoard
    template_name = 'workstation/keyBoard_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Клавиатуры", searchlink='workstation:keyBoard',add='workstation:new-keyBoard')
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
    template_name = 'workstation/keyBoard_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Клавиатура",add='workstation:new-keyBoard',update='workstation:keyBoard-update',delete='workstation:keyBoard-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class keyBoardCreate(DataMixin, CreateView):
    model = keyBoard
    form_class = keyBoardForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('workstation:keyBoard')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить клавиатуру",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class keyBoardUpdate(DataMixin, UpdateView):
    model = keyBoard
    template_name = 'Forms/add.html'
    form_class = keyBoardForm
    success_url = reverse_lazy('workstation:keyBoard')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать клавиатуру",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class keyBoardDelete(DataMixin, DeleteView):
    model = keyBoard
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('workstation:keyBoard')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить клавиатуру",selflink='workstation:keyBoard')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Мышь
class mouseListView(DataMixin, generic.ListView):
    model = mouse
    template_name = 'workstation/mouse_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Мыши", searchlink='workstation:mouse',add='workstation:new-mouse')
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
    template_name = 'workstation/mouse_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Мышь",add='new-mouse',update='workstation:mouse-update',delete='workstation:mouse-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class mouseCreate(DataMixin, CreateView):
    model = mouse
    form_class = mouseForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('workstation:mouse')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить мышь",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class mouseUpdate(DataMixin, UpdateView):
    model = mouse
    template_name = 'Forms/add.html'
    form_class = mouseForm
    success_url = reverse_lazy('workstation:mouse')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать мышь",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class mouseDelete(DataMixin, DeleteView):
    model = mouse
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('workstation:mouse')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить мышь",selflink='workstation:mouse')
        context = dict(list(context.items()) + list(c_def.items()))
        return context