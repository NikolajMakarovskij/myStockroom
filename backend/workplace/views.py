from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework import viewsets, permissions

from core.utils import DataMixin, FormMessageMixin, menu
from .forms import RoomForm, WorkplaceForm
from .models import Room, Workplace
from .serializers import WorkplaceModelSerializer, RoomModelSerializer


class IndexView(LoginRequiredMixin, PermissionRequiredMixin, generic.TemplateView):
    permission_required = 'workplace.view_workplace'
    """
    Главная
    """
    template_name = 'workplace/workplace_index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Рабочие места, Помещения'
        context['menu'] = menu
        return context


# Рабочие места
class WorkplaceListView(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView):
    permission_required = 'workplace.view_workplace'
    model = Workplace
    template_name = 'workplace/workplace_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Рабочие места", searchlink='workplace:workplace_search',
                                      add='workplace:new-workplace', )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            query = ''
        object_list = Workplace.objects.filter(
            Q(name__icontains=query) |
            Q(room__name__icontains=query) |
            Q(room__floor__icontains=query) |
            Q(room__building__icontains=query)
        ).select_related('room')
        return object_list


class WorkplaceRestView(DataMixin, viewsets.ModelViewSet):
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceModelSerializer
    permission_classes = [permissions.IsAuthenticated]


class WorkplaceDetailView(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.DetailView):
    permission_required = 'workplace.view_workplace'
    model = Workplace
    template_name = 'workplace/workplace_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Рабочее место", add='workplace:new-workplace',
                                      update='workplace:workplace-update', delete='workplace:workplace-delete', )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class WorkplaceCreate(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, CreateView):
    permission_required = 'workplace.add_workplace'
    model = Workplace
    form_class = WorkplaceForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('workplace:workplace_list')
    success_message = f"Рабочее место %(name)s успешно создано"
    error_message = f"Рабочее место %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить рабочее место", )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class WorkplaceUpdate(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, UpdateView):
    permission_required = 'workplace.change_workplace'
    model = Workplace
    template_name = 'Forms/add.html'
    form_class = WorkplaceForm
    success_url = reverse_lazy('workplace:workplace_list')
    success_message = f"Рабочее место %(name)s успешно обновлено"
    error_message = f"Рабочее место %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать рабочее место", )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class WorkplaceDelete(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, DeleteView):
    permission_required = 'workplace.delete_workplace'
    model = Workplace
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('workplace:workplace_list')
    success_message = f"Рабочее место успешно удалено"
    error_message = f"Рабочее место не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить рабочее место", selflink='workplace:workplace_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


# Кабинеты
class RoomListView(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView):
    permission_required = 'workplace.view_room'
    model = Room
    template_name = 'workplace/room_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Кабинеты", searchlink='workplace:room_search', add='workplace:new-room',
                                      )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            query = ''
        object_list = Room.objects.filter(
            Q(name__icontains=query) |
            Q(floor__icontains=query) |
            Q(building__icontains=query)
        )
        return object_list


class RoomRestView(DataMixin, viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomModelSerializer
    permission_classes = [permissions.IsAuthenticated]


class RoomDetailView(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.DetailView):
    permission_required = 'workplace.view_room'
    model = Room
    template_name = 'workplace/room_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Кабинет", add='workplace:new-room', update='workplace:room-update',
                                      delete='workplace:room-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class RoomCreate(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, CreateView):
    permission_required = 'workplace.add_room'
    model = Room
    form_class = RoomForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('workplace:room_list')
    success_message = f"Кабинет %(name)s успешно создан"
    error_message = f"Кабинет %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить кабинет", )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class RoomUpdate(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, UpdateView):
    permission_required = 'workplace.change_room'
    model = Room
    template_name = 'Forms/add.html'
    form_class = RoomForm
    success_url = reverse_lazy('workplace:room_list')
    success_message = f"Кабинет %(name)s успешно обновлен"
    error_message = f"Кабинет %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать кабинет", )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class RoomDelete(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, DeleteView):
    permission_required = 'workplace.delete_room'
    model = Room
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('workplace:room_list')
    success_message = f"Кабинет успешно удален"
    error_message = f"Кабинет не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить кабинет", selflink='workplace:room_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context
