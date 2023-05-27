from .forms import *
from .models import *
from django.views import generic
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from catalog.utils import *
from django.core.cache import cache



#Рабочие станции
class workstationListView(DataMixin, generic.ListView):
    model = Workstation
    template_name = 'workstation/workstation_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        work_cat = cache.get('work_cat')
        if not work_cat:
            work_cat = Workstation_cat.objects.all()
            cache.set('work_cat', work_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Рабочие станции", searchlink='workstation:workstation_search',add='workstation:new-workstation',menu_categories=work_cat)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = Workstation.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(serial__icontains=query) | 
                Q(invent__icontains=query) | 
                Q(motherboard__icontains=query) | 
                Q(monitor__name__icontains=query) | 
                Q(cpu__icontains=query) | 
                Q(gpu__icontains=query) | 
                Q(ram__name__icontains=query) | 
                Q(ssd__name__icontains=query) | 
                Q(hdd__name__icontains=query) | 
                Q(os__name__icontains=query) | 
                Q(dcpower__icontains=query) | 
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
        ).select_related('workplace','workplace__room', 'employee', 'os').only('employee__name', 'employee__sername', 'employee__family', 'name', 'serial', 
                  'serialImg', 'invent', 'inventImg', 'os__name', 'workplace__name', 'workplace__room__name', 'workplace__room__floor', 'workplace__room__building') 
        return object_list

class workstationCategoryListView(DataMixin, generic.ListView):
    model = Workstation.objects
    template_name = 'workstation/workstation_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        work_cat = cache.get('work_cat')
        if not work_cat:
            work_cat = Workstation_cat.objects.all()
            cache.set('work_cat', work_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Рабочие станции", searchlink='workstation:workstation_search',add='workstation:new-workstation',menu_categories=work_cat)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        object_list = Workstation.objects.filter(categories__slug=self.kwargs['category_slug']).select_related('categories', 'manufacturer', 'workplace','workplace__room', 'software', 'employee', 'os')
        return object_list

class workstationDetailView(DataMixin, generic.DetailView):
    model = Workstation
    template_name = 'workstation/workstation_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        work_menu = cache.get('work_menu')
        if not work_menu:
            work_menu = workstationMenu
            cache.set('work_menu', work_menu, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Рабочая станция",add='workstation:new-workstation',update='workstation:workstation-update',delete='workstation:workstation-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        context['detailMenu'] = work_menu
        return context

class workstationCreate(DataMixin, FormMessageMixin, CreateView):
    model = Workstation
    form_class = workstationForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('workstation:workstation_list')
    success_message = 'Рабочая станция %(name)s успешно создана'
    error_message = 'Рабочую станцию %(name)s не удалось создать'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить рабочую станцию",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class workstationUpdate(DataMixin, FormMessageMixin, UpdateView):
    model = Workstation
    template_name = 'Forms/add.html'
    form_class = workstationForm
    success_url = reverse_lazy('workstation:workstation_list')
    success_message = 'Рабочая станция %(name)s успешно обновлена'
    error_message = 'Рабочую станцию %(name)s не удалось обновить'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать рабочую станцию",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class workstationDelete(DataMixin, FormMessageMixin, DeleteView):
    model = Workstation
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('workstation:workstation_list')
    success_message = 'Рабочая станция успешно удалена'
    error_message = 'Рабочую станцию не удалось удалить'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить рабочую станцию",selflink='workstation:workstation_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Монитор
class monitorListView(DataMixin, generic.ListView):
    model = Monitor
    template_name = 'workstation/monitor_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Мониторы", searchlink='workstation:monitor_search',add='workstation:new-monitor')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = Monitor.objects.filter(
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
    model = Monitor
    template_name = 'workstation/monitor_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Монитор",add='workstation:new-monitor',update='workstation:monitor-update',delete='workstation:monitor-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class monitorCreate(DataMixin, FormMessageMixin, CreateView):
    model = Monitor
    form_class = monitorForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('workstation:monitor_list')
    success_message = 'Монитор %(name)s успешно создан'
    error_message = 'Монитор %(name)s не удалось создать'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить монитор",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class monitorUpdate(DataMixin, FormMessageMixin, UpdateView):
    model = Monitor
    template_name = 'Forms/add.html'
    form_class = monitorForm
    success_url = reverse_lazy('workstation:monitor_list')
    success_message = 'Монитор %(name)s успешно обновлен'
    error_message = 'Монитор %(name)s не удалось обновить'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать монитор",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class monitorDelete(DataMixin, FormMessageMixin, DeleteView):
    model = Monitor
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('workstation:monitor')
    success_message = 'Монитор успешно удален'
    error_message = 'Монитор не удалось удалить'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить монитор",selflink='workstation:monitor_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Клавиатура
class keyBoardListView(DataMixin, generic.ListView):
    model = KeyBoard
    template_name = 'workstation/keyBoard_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Клавиатуры", searchlink='workstation:keyBoard_search',add='workstation:new-keyBoard')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = KeyBoard.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(serial__icontains=query) | 
                Q(invent__icontains=query) | 
                Q(score__icontains=query) 
        )
        return object_list

class keyBoardDetailView(DataMixin, generic.DetailView):
    model = KeyBoard
    template_name = 'workstation/keyBoard_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Клавиатура",add='workstation:new-keyBoard',update='workstation:keyBoard-update',delete='workstation:keyBoard-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class keyBoardCreate(DataMixin, FormMessageMixin, CreateView):
    model = KeyBoard
    form_class = keyBoardForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('workstation:keyBoard_list')
    success_message = 'Клавиатура %(name)s успешно создана'
    error_message = 'Клавиатуру %(name)s не удалось создать'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить клавиатуру",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class keyBoardUpdate(DataMixin, FormMessageMixin, UpdateView):
    model = KeyBoard
    template_name = 'Forms/add.html'
    form_class = keyBoardForm
    success_url = reverse_lazy('workstation:keyBoard_list')
    success_message = 'Клавиатура %(name)s успешно обновлена'
    error_message = 'Клавиатуру %(name)s не удалось обновить'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать клавиатуру",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class keyBoardDelete(DataMixin, FormMessageMixin, DeleteView):
    model = KeyBoard
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('workstation:keyBoard_list')
    success_message = 'Расходник успешно удален'
    error_message = 'Расходник не удалось удалить'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить клавиатуру",selflink='workstation:keyBoard_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Мышь
class mouseListView(DataMixin, generic.ListView):
    model = Mouse
    template_name = 'workstation/mouse_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Мыши", searchlink='workstation:mouse_search',add='workstation:new-mouse')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = Mouse.objects.filter(
                Q(name__icontains=query) | 
                Q(manufacturer__name__icontains=query) |
                Q(serial__icontains=query) | 
                Q(invent__icontains=query) |  
                Q(score__icontains=query) 
        )
        return object_list

class mouseDetailView(DataMixin, generic.DetailView):
    model = Mouse
    template_name = 'workstation/mouse_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Мышь",add='workstation:new-mouse',update='workstation:mouse-update',delete='workstation:mouse-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class mouseCreate(DataMixin, FormMessageMixin, CreateView):
    model = Mouse
    form_class = mouseForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('workstation:mouse_list')
    success_message = 'Мышь %(name)s успешно создана'
    error_message = 'Мышь %(name)s не удалось создать'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить мышь",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class mouseUpdate(DataMixin, FormMessageMixin, UpdateView):
    model = Mouse
    template_name = 'Forms/add.html'
    form_class = mouseForm
    success_url = reverse_lazy('workstation:mouse_list')
    success_message = 'Мышь %(name)s успешно обновлена'
    error_message = 'Мышь %(name)s не удалось обновить'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать мышь",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class mouseDelete(DataMixin, FormMessageMixin, DeleteView):
    model = Mouse
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('workstation:mouse_list')
    success_message = 'Мышь успешно удалена'
    error_message = 'Мышь не удалось удалить'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить мышь",selflink='workstation:mouse_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context