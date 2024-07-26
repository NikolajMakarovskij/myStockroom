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
    template_name = "counterparty/counterparty.html"
    permission_required = "counterparty.view_manufacturer"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Контрагенты, поставщики"
        context["menu"] = menu
        return context


# Производитель
class ManufacturerListView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    permission_required = "counterparty.view_manufacturer"
    model = Manufacturer
    template_name = "counterparty/manufacturer_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Список производителей",
            searchlink="counterparty:manufacturer_search",
            add="counterparty:new-manufacturer",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
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
    permission_required = "counterparty.view_manufacturer"
    model = Manufacturer
    template_name = "counterparty/manufacturer_detail.html"

    def get_context_data(self, *, object_list=None, **kwargs):
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
    permission_required = "counterparty.add_manufacturer"
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = "Forms/add.html"
    success_url = reverse_lazy("counterparty:manufacturer_list")
    success_message = "Производитель %(name)s успешно создан"
    error_message = "Производителя %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Добавить производителя",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ManufacturerUpdate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, UpdateView
):
    permission_required = "counterparty.change_manufacturer"
    model = Manufacturer
    template_name = "Forms/add.html"
    form_class = ManufacturerForm
    success_url = reverse_lazy("counterparty:manufacturer_list")
    success_message = "Производитель %(name)s успешно обновлен"
    error_message = "Производителя %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Редактировать производителя",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ManufacturerDelete(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, DeleteView
):
    permission_required = "counterparty.delete_manufacturer"
    model = Manufacturer
    template_name = "Forms/delete.html"
    success_url = reverse_lazy("counterparty:manufacturer_list")
    success_message = "Производитель успешно удален"
    error_message = "Производителя не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Удалить производителя", selflink="counterparty:manufacturer_list"
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context
