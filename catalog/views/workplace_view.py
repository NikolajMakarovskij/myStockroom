from django.urls import reverse_lazy
from ..forms import roomForm, workplaceForm
from ..models.models import Workplace, Room
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from ..utils import DataMixin

#Рабочие места
class WorkplaceListView(DataMixin, generic.ListView):
    model = Workplace
    template_name = 'catalog/workplace/workplace_list.html'
  
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Рабочие места", searchlink='workplace',add='new-workplace')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = Workplace.objects.filter(
                Q(name__icontains=query) |
                Q(Room__name__icontains=query) |
                Q(Room__Floor__icontains=query) |
                Q(Room__Building__icontains=query) 
        )
        return object_list

class WorkplaceDetailView(DataMixin, generic.DetailView):
    model = Workplace
    template_name = 'catalog/workplace/workplace_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Рабочее место",add='new-workplace',update='workplace-update',delete='workplace-delete',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class WorkplaceCreate(DataMixin, CreateView):
    model = Workplace
    form_class = workplaceForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('workplace')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить рабочее место",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class WorkplaceUpdate(DataMixin, UpdateView):
    model = Workplace
    template_name = 'Forms/add.html'
    form_class = workplaceForm
    success_url = reverse_lazy('workplace')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать рабочее место",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class WorkplaceDelete(DataMixin, DeleteView):
    model = Workplace
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('workplace')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить рабочее место",selflink='workplace')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Кабинеты
class RoomListView(DataMixin, generic.ListView):
    model = Room
    template_name = 'catalog/workplace/room_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Рабочие места", searchlink='room',add='new-room',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = Room.objects.filter(
                Q(name__icontains=query) |
                Q(Floor__icontains=query) |
                Q(Building__icontains=query) 
        )
        return object_list

class RoomDetailView(DataMixin, generic.DetailView):
    model = Room
    template_name = 'catalog/workplace/room_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Кабинет",add='new-room',update='room-update',delete='room-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class RoomCreate(DataMixin, CreateView):
    model = Room
    form_class = roomForm
    template_name = 'Forms/add.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить кабинет",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class RoomUpdate(DataMixin, UpdateView):
    model = Room
    template_name = 'Forms/add.html'
    form_class = roomForm
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать кабинет",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class RoomDelete(DataMixin, DeleteView):
    model = Room
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('room')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить кабинет",selflink='room')
        context = dict(list(context.items()) + list(c_def.items()))
        return context