from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from core.utils import DataMixin, FormMessageMixin, menu

from .forms import ManufacturerForm
from .models import Manufacturer


# Контрагенты
class CounterpartyView(
    LoginRequiredMixin, PermissionRequiredMixin, generic.TemplateView
):
    """_CounterpartyView_
    Home page for counterparty app

    Returns:
        template_name (str): _path to template_
        permission_required (str): _permissions_
    """
    template_name = "counterparty/counterparty.html"
    permission_required = "counterparty.view_manufacturer"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (list[str]): _returns title, side menu_
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Контрагенты, поставщики"
        context["menu"] = menu
        return context


# Производитель
class ManufacturerListView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    """_ManufacturerListView_
    List of manufacturer instances

    Returns:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        paginate_by (int, optional): _add pagination_
        model (Manufacturer): _base model for list_
    """
    permission_required = "counterparty.view_manufacturer"
    paginate_by = DataMixin.paginate
    model = Manufacturer
    template_name = "counterparty/manufacturer_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, link for search, link to create manufacturer_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Список производителей",
            searchlink="counterparty:manufacturer_search",
            add="counterparty:new-manufacturer",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_queryset_ 

        Returns:
            object_list (Accounting): _description_
        """
        query = self.request.GET.get("q")
        if not query:
            query = ""
        object_list = Manufacturer.objects.filter(
            Q(name__icontains=query)
            | Q(country__icontains=query)
            | Q(production__icontains=query)
        )
        return object_list


class ManufacturerDetailView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.DetailView
):
    """_ManufacturerDetailView_
    Detail of manufacturer instances

    Returns:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Manufacturer): _base model for list_
    """
    permission_required = "counterparty.view_manufacturer"
    model = Manufacturer
    template_name = "counterparty/manufacturer_detail.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, links to create, update and delete manufacturer instance_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Производитель",
            add="counterparty:new-manufacturer",
            update="counterparty:manufacturer-update",
            delete="counterparty:manufacturer-delete",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ManufacturerCreate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, CreateView
):
    """_ManufacturerCreate_
    Create of manufacturer instances

    Returns:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Manufacturer): _base model for list_
        form_class (ManufacturerForm): _form class to view_
        success_message (str):
        error_message (str):
    """
    permission_required = "counterparty.add_manufacturer"
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = "Forms/add.html"
    success_url = reverse_lazy("counterparty:manufacturer_list")
    success_message = "Производитель %(name)s успешно создан"
    error_message = "Производителя %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Добавить производителя",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ManufacturerUpdate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, UpdateView
):
    """_ManufacturerUpdate_
    Update of manufacturer instances

    Returns:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Manufacturer): _base model for list_
        form_class (ManufacturerForm): _form class to view_
        success_message (str):
        error_message (str):
    """
    permission_required = "counterparty.change_manufacturer"
    model = Manufacturer
    template_name = "Forms/add.html"
    form_class = ManufacturerForm
    success_url = reverse_lazy("counterparty:manufacturer_list")
    success_message = "Производитель %(name)s успешно обновлен"
    error_message = "Производителя %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Редактировать производителя",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ManufacturerDelete( # type: ignore[misc]
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, DeleteView
):
    """_ManufacturerDelete_
    Delete of manufacturer instances

    Returns:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Manufacturer): _base model for list_
        success_url (str): _switches to url in case of successful deletion_
        success_message (str):
        error_message (str):
    """
    permission_required = "counterparty.delete_manufacturer"
    model = Manufacturer
    template_name = "Forms/delete.html"
    success_url = reverse_lazy("counterparty:manufacturer_list")
    success_message = "Производитель успешно удален"
    error_message = "Производителя не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to accounting list_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Удалить производителя", selflink="counterparty:manufacturer_list"
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context
