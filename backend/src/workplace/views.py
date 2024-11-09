from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from rest_framework import permissions, viewsets  # noqa F401

from core.utils import DataMixin, FormMessageMixin, menu

from .forms import RoomForm, WorkplaceForm
from .models import Room, Workplace
from .serializers import RoomModelSerializer, WorkplaceModelSerializer


class IndexView(LoginRequiredMixin, PermissionRequiredMixin, generic.TemplateView):
    """_IndexView_
    Home page for workplace app

    Returns:
        template_name (str): _path to template_
        permission_required (str): _permissions_
    """

    permission_required = "workplace.view_workplace"
    template_name = "workplace/workplace_index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (list[str]): _returns title, side menu_
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Рабочие места, Помещения"
        context["menu"] = menu
        return context


# Рабочие места
class WorkplaceListView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    """_WorkplaceListView_
    List of workplace instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        paginate_by (int, optional): _add pagination_
        model (Workplace): _base model for list_
    """

    permission_required = "workplace.view_workplace"
    paginate_by = DataMixin.paginate
    model = Workplace
    template_name = "workplace/workplace_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, link for search, link to create workplace, categories for filtering queryset_
        """

        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Рабочие места",
            searchlink="workplace:workplace_search",
            add="workplace:new-workplace",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_returns queryset_

        Returns:
            object_list (Workplace): _returns queryset_
        """

        query = self.request.GET.get("q")
        if not query:
            query = ""
        object_list = Workplace.objects.filter(
            Q(name__icontains=query)
            | Q(room__name__icontains=query)
            | Q(room__floor__icontains=query)
            | Q(room__building__icontains=query)
        ).select_related("room")
        return object_list


class WorkplaceRestView(DataMixin, viewsets.ModelViewSet):
    """_WorkplaceRestView_ returns workplace

    Other parameters:
        queryset (Workplace):
        serializer_class (WorkplaceModelSerializer):
    """

    queryset = Workplace.objects.all()
    serializer_class = WorkplaceModelSerializer
    # permission_classes = [permissions.IsAuthenticated]


class WorkplaceDetailView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.DetailView
):
    """_WorkplaceDetailView_
    Detail of workplace instance

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Workplace): _base model for detail_
    """

    permission_required = "workplace.view_workplace"
    model = Workplace
    template_name = "workplace/workplace_detail.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, links to create, update and delete workplace instance_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Рабочее место",
            add="workplace:new-workplace",
            update="workplace:workplace-update",
            delete="workplace:workplace-delete",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class WorkplaceCreate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, CreateView
):
    """_WorkplaceCreate_
    Create workplace instance

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Workplace): _base model for create_
        form_class (WorkplaceForm): _form for create_
        success_url (str): _redirect to workplace list_
        success_message (str):
        error_message (str):
    """

    permission_required = "workplace.add_workplace"
    model = Workplace
    form_class = WorkplaceForm
    template_name = "Forms/add.html"
    success_url = reverse_lazy("workplace:workplace_list")
    success_message = "Рабочее место %(name)s успешно создано"
    error_message = "Рабочее место %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Добавить рабочее место",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class WorkplaceUpdate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, UpdateView
):
    """_WorkplaceUpdate_
    Update of workplace instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Workplace): _base model for list_
        form_class (WorkplaceForm): _form class to view_
        success_message (str):
        error_message (str):
    """

    permission_required = "workplace.change_workplace"
    model = Workplace
    template_name = "Forms/add.html"
    form_class = WorkplaceForm
    success_url = reverse_lazy("workplace:workplace_list")
    success_message = "Рабочее место %(name)s успешно обновлено"
    error_message = "Рабочее место %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Редактировать рабочее место",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class WorkplaceDelete(  # type: ignore[misc]
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, DeleteView
):
    """_WorkplaceDelete_
    Delete workplace instance

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Workplace): _base model for delete_
        success_url (str): _redirect to workplace list_
        success_message (str):
        error_message (str):
    """

    permission_required = "workplace.delete_workplace"
    model = Workplace
    template_name = "Forms/delete.html"
    success_url = reverse_lazy("workplace:workplace_list")
    success_message = "Рабочее место успешно удалено"
    error_message = "Рабочее место не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to workplace list_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Удалить рабочее место", selflink="workplace:workplace_list"
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


# Кабинеты
class RoomListView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    """_RoomListView_
    List of room instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        paginate_by (int, optional): _add pagination_
        model (Room): _base model for list_
    """

    permission_required = "workplace.view_room"
    paginate_by = DataMixin.paginate
    model = Room
    template_name = "workplace/room_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, links to search, add room instance_
        """

        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Кабинеты",
            searchlink="workplace:room_search",
            add="workplace:new-room",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_returns queryset_

        Returns:
            object_list (object[Room]): _returns queryset_
        """

        query = self.request.GET.get("q")
        if not query:
            query = ""
        object_list = Room.objects.filter(
            Q(name__icontains=query)
            | Q(floor__icontains=query)
            | Q(building__icontains=query)
        )
        return object_list


class RoomRestView(DataMixin, viewsets.ModelViewSet):
    """_RoomRestView_
    List of room instances

    Other parameters:
        queryset (Room): _base model for list_
        serializer_class (RoomModelSerializer): _serializer_
    """

    queryset = Room.objects.all()
    serializer_class = RoomModelSerializer
    # permission_classes = [permissions.IsAuthenticated]


class RoomDetailView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.DetailView
):
    """_RoomDetailView_
    Detail of room instance

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Room): _base model for detail_
    """

    permission_required = "workplace.view_room"
    model = Room
    template_name = "workplace/room_detail.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, links to create, update and delete room instance_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Кабинет",
            add="workplace:new-room",
            update="workplace:room-update",
            delete="workplace:room-delete",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class RoomCreate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, CreateView
):
    """_RoomCreate_
    Create room instance

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Room): _base model for create_
        form_class (RoomForm): _form class to create_
        success_url (str): _redirect to room list_
        success_message (str):
        error_message (str):
    """

    permission_required = "workplace.add_room"
    model = Room
    form_class = RoomForm
    template_name = "Forms/add.html"
    success_url = reverse_lazy("workplace:room_list")
    success_message = "Кабинет %(name)s успешно создан"
    error_message = "Кабинет %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Добавить кабинет",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class RoomUpdate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, UpdateView
):
    """_RoomUpdate_
    Update of room instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Room): _base model for list_
        form_class (RoomForm): _form class to view_
        success_message (str):
        error_message (str):
    """

    permission_required = "workplace.change_room"
    model = Room
    template_name = "Forms/add.html"
    form_class = RoomForm
    success_url = reverse_lazy("workplace:room_list")
    success_message = "Кабинет %(name)s успешно обновлен"
    error_message = "Кабинет %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title_
        """

        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Редактировать кабинет",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class RoomDelete(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, DeleteView
):  # type: ignore[misc]
    """_RoomDelete_
    Delete room instance

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Room): _base model for delete_
        success_url (str): _redirect to room list_
        success_message (str):
        error_message (str):
    """

    permission_required = "workplace.delete_room"
    model = Room
    template_name = "Forms/delete.html"
    success_url = reverse_lazy("workplace:room_list")
    success_message = "Кабинет успешно удален"
    error_message = "Кабинет не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to room list_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Удалить кабинет", selflink="workplace:room_list"
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context
