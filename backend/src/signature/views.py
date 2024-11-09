from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, FormMixin, UpdateView

from core.utils import DataMixin, FormMessageMixin
from stockroom.forms import ConsumableInstallForm

from .forms import SignatureForm
from .models import Signature


class SignatureListView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    """_SignatureListView_
    List of signature instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        paginate_by (int, optional): _add pagination_
        model (Signature): _base model for list_
    """

    permission_required = "signature.view_signature"
    paginate_by = DataMixin.paginate
    model = Signature
    template_name = "signature/signature_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, link for search, link to create signature_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="ЭЦП",
            searchlink="signature:signature_search",
            add="signature:new-signature",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_queryset_

        Returns:
            object_list (Signature): _description_
        """
        query = self.request.GET.get("q")
        if not query:
            query = ""
        object_list = Signature.objects.filter(
            Q(name__icontains=query)
            | Q(periodOpen__icontains=query)
            | Q(periodClose__icontains=query)
            | Q(employeeRegister__name__icontains=query)
            | Q(employeeStorage__name__icontains=query)
            | Q(storage__name__icontains=query)
            | Q(workstation__name__icontains=query)
            | Q(workstation__workplace__name__icontains=query)
            | Q(workstation__workplace__room__name__icontains=query)
            | Q(workstation__workplace__room__floor__icontains=query)
            | Q(workstation__workplace__room__building__icontains=query)
        ).select_related(
            "employeeRegister",
            "employeeStorage",
            "storage",
            "workstation",
            "workstation__workplace",
            "workstation__workplace__room",
        )
        return object_list


class SignatureDetailView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DataMixin,
    FormMixin,
    generic.DetailView,
):
    """_SignatureDetailView_
    Detail of signature instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Signature): _base model for list_
    """

    permission_required = "signature.view_signature"
    model = Signature
    template_name = "signature/signature_detail.html"
    form_class = ConsumableInstallForm

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, links to create, update and delete signature instance_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="ЭЦП",
            add="signature:new-signature",
            update="signature:signature-update",
            delete="signature:signature-delete",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class SignatureCreate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, CreateView
):
    """_SignatureCreate_
    Create signature instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Signature): _base model for list_
        form_class (SignatureForm): _form class to view_
        success_message (str):
        error_message (str):
    """

    permission_required = "signature.add_signature"
    model = Signature
    form_class = SignatureForm
    template_name = "Forms/add.html"
    success_url = reverse_lazy("signature:signature_list")
    success_message = "ЭЦП %(name)s успешно создана"
    error_message = "ЭЦП %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Добавить ЭЦП",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class SignatureUpdate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, UpdateView
):
    """_SignatureUpdate_
    Update signature instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Signature): _base model for list_
        form_class (SignatureForm): _form class to view_
        success_message (str):
        error_message (str):
    """

    permission_required = "signature.change_signature"
    model = Signature
    template_name = "Forms/add.html"
    form_class = SignatureForm
    success_url = reverse_lazy("signature:signature_list")
    success_message = "ЭЦП %(name)s успешно обновлена"
    error_message = "ЭЦП %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title_
        """

        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Редактировать ЭЦП",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class SignatureDelete(  # type: ignore[misc]
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, DeleteView
):
    """_SignatureDelete_
    Delete signature instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Signature): _base model for list_
        success_url (str): _switches to url in case of successful deletion_
        success_message (str):
        error_message (str):
    """

    permission_required = "signature.delete_signature"
    model = Signature
    template_name = "Forms/delete.html"
    success_url = reverse_lazy("signature:signature_list")
    success_message = "ЭЦП успешно удалена"
    error_message = "ЭЦП не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to signature list_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Удалить ЭЦП", selflink="signature:signature_list"
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context
