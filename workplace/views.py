from django.urls import reverse_lazy
from .forms import roomForm, workplaceForm
from .models import Room, Workplace
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from catalog.utils import DataMixin

#Рабочие места
class WorkplaceListView(DataMixin, generic.ListView):
    model = Workplace
    template_name = 'workplace/workplace_list.html'
  
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Рабочие места", searchlink='workplace:workplace_search',add='workplace:new-workplace')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = Workplace.objects.filter(
                Q(name__icontains=query) |
                Q(room__name__icontains=query) |
                Q(room__floor__icontains=query) |
                Q(room__building__icontains=query) 
        ).select_related('room')
        return object_list

class WorkplaceDetailView(DataMixin, generic.DetailView):
    model = Workplace
    template_name = 'workplace/workplace_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Рабочее место",add='workplace:new-workplace',update='workplace:workplace-update',delete='workplace:workplace-delete',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class WorkplaceCreate(DataMixin, CreateView):
    model = Workplace
    form_class = workplaceForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('workplace:workplace_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить рабочее место",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class WorkplaceUpdate(DataMixin, UpdateView):
    model = Workplace
    template_name = 'Forms/add.html'
    form_class = workplaceForm
    success_url = reverse_lazy('workplace:workplace_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать рабочее место",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class WorkplaceDelete(DataMixin, DeleteView):
    model = Workplace
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('workplace:workplace_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить рабочее место",selflink='workplace:workplace_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Кабинеты
class RoomListView(DataMixin, generic.ListView):
    model = Room
    template_name = 'workplace/room_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Кабинеты", searchlink='workplace:room_search',add='workplace:new-room',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = Room.objects.filter(
                Q(name__icontains=query) |
                Q(floor__icontains=query) |
                Q(building__icontains=query) 
        )
        return object_list

class RoomDetailView(DataMixin, generic.DetailView):
    model = Room
    template_name = 'workplace/room_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Кабинет",add='workplace:new-room',update='workplace:room-update',delete='workplace:room-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class RoomCreate(DataMixin, CreateView):
    model = Room
    form_class = roomForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('workplace:room_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить кабинет",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class RoomUpdate(DataMixin, UpdateView):
    model = Room
    template_name = 'Forms/add.html'
    form_class = roomForm
    success_url = reverse_lazy('workplace:room_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать кабинет",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class RoomDelete(DataMixin, DeleteView):
    model = Room
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('workplace:room_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить кабинет",selflink='workplace:room_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context
