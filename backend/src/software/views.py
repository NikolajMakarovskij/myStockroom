from core.utils import DataMixin, FormMessageMixin, menu
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import OSForm, SoftwareForm
from .models import Os, Software


class IndexView(LoginRequiredMixin, PermissionRequiredMixin, generic.TemplateView):
    permission_required = "software.view_software"
    template_name = "software/soft_index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "СОФТ, ОС"
        context["menu"] = menu
        return context


class SoftwareListView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    permission_required = "software.view_software"
    paginate_by = DataMixin.paginate
    model = Software
    template_name = "software/software_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Список ПО",
            searchlink="software:software_search",
            add="software:new-software",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get("q")
        if not query:
            query = ""
        object_list = Software.objects.filter(
            Q(name__icontains=query)
            | Q(manufacturer__name__icontains=query)
            | Q(version__icontains=query)
            | Q(bitDepth__icontains=query)
        ).select_related("manufacturer")
        return object_list


class SoftwareDetailView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.DetailView
):
    permission_required = "software.view_software"
    model = Software
    template_name = "software/software_detail.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Программное обеспечение",
            add="software:new-software",
            update="software:software-update",
            delete="software:software-delete",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class SoftwareCreate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, CreateView
):
    permission_required = "software.add_software"
    model = Software
    form_class = SoftwareForm
    template_name = "Forms/add.html"
    success_url = reverse_lazy("software:software_list")
    success_message = "ПО %(name)s успешно создано"
    error_message = "ПО %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Добавить ПО",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class SoftwareUpdate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, UpdateView
):
    permission_required = "software.change_software"
    model = Software
    template_name = "Forms/add.html"
    form_class = SoftwareForm
    success_url = reverse_lazy("software:software_list")
    success_message = "ПО %(name)s успешно обновлено"
    error_message = "ПО %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Редактировать ПО",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class SoftwareDelete(  # type: ignore[misc]
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, DeleteView
):
    permission_required = "software.delete_software"
    model = Software
    template_name = "Forms/delete.html"
    success_url = reverse_lazy("software:software_list")
    success_message = "ПО успешно удалено"
    error_message = "ПО не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Удалить ПО", selflink="software:software_list"
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


# ОС
class OSListView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    permission_required = "software.view_os"
    model = Os
    paginate_by = DataMixin.paginate
    template_name = "software/OS_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Список ОС", searchlink="software:OS_search", add="software:new-OS"
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get("q")
        if not query:
            query = ""
        object_list = Os.objects.filter(
            Q(name__icontains=query)
            | Q(manufacturer__name__icontains=query)
            | Q(version__icontains=query)
            | Q(bitDepth__icontains=query)
        ).select_related("manufacturer")
        return object_list


class OSDetailView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.DetailView
):
    permission_required = "software.view_os"
    model = Os
    template_name = "software/OS_detail.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Операционная система",
            add="software:new-OS",
            update="software:OS-update",
            delete="software:OS-delete",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class OSCreate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, CreateView
):
    permission_required = "software.add_os"
    model = Os
    form_class = OSForm
    template_name = "Forms/add.html"
    success_url = reverse_lazy("software:OS_list")
    success_message = "ОС %(name)s успешно создана"
    error_message = "ОС %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Добавить ОС",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class OSUpdate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, UpdateView
):
    permission_required = "software.change_os"
    model = Os
    template_name = "Forms/add.html"
    form_class = OSForm
    success_url = reverse_lazy("software:OS_list")
    success_message = "ОС %(name)s успешно обновлена"
    error_message = "ОС %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Редактировать ОС",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class OSDelete(  # type: ignore[misc]
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, DeleteView
):
    permission_required = "software.delete_os"
    model = Os
    template_name = "Forms/delete.html"
    success_url = reverse_lazy("software:OS_list")
    success_message = "ОС успешно удалена"
    error_message = "ОС не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить ОС", selflink="software:OS_list")
        context = dict(list(context.items()) + list(c_def.items()))
        return context
