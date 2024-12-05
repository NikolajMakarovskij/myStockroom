from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.db.models import Q
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View, generic
from django.views.generic.edit import CreateView, DeleteView, FormMixin, UpdateView
from rest_framework import viewsets

from consumables.resources import AccessoriesResource, ConsumableResource
from core.utils import DataMixin, FormMessageMixin, menu
from stockroom.forms import StockAddForm

from .forms import AccessoriesForm, ConsumablesForm
from .models import AccCat, Accessories, Categories, Consumables
from .serializers import (
    AccCatModelSerializer,
    AccessoriesModelSerializer,
    CategoriesModelSerializer,
    ConsumablesModelSerializer,
)


# Расходники главная
class ConsumableIndexView(
    LoginRequiredMixin, PermissionRequiredMixin, generic.TemplateView
):
    """_ConsumableIndexView_
    Home page for consumables app

    Returns:
        template_name (str): _path to template_
        permission_required (str): _permissions_
    """

    template_name = "consumables/consumables_index.html"
    permission_required = "consumables.view_consumables"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (list[str]): _returns title, side menu_
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Расходники и комплектующие"
        context["menu"] = menu
        return context


# Расходники
class ConsumablesView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    """_ConsumablesView_
    List of consumables instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        paginate_by (int, optional): _add pagination_
        model (Consumables): _base model for list_
    """

    permission_required = "consumables.view_consumables"
    template_name = "consumables/consumables_list.html"
    paginate_by = DataMixin.paginate
    model = Consumables

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, link for search, link to create consumables, categories for filtering queryset_
        """
        cons_cat = cache.get("cons_cat")
        if not cons_cat:
            cons_cat = Categories.objects.all()
            cache.set("cons_cat", cons_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Расходники",
            searchlink="consumables:consumables_search",
            add="consumables:new-consumables",
            menu_categories=cons_cat,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_queryset_

        Returns:
            object_list (Consumables): _description_
        """
        query = self.request.GET.get("q")
        if not query:
            query = ""
        object_list = (
            Consumables.objects.filter(
                Q(name__icontains=query)
                | Q(manufacturer__name__icontains=query)
                | Q(categories__name__icontains=query)
                | Q(device__name__icontains=query)
                | Q(device__workplace__name__icontains=query)
                | Q(device__workplace__room__name__icontains=query)
                | Q(device__workplace__room__building__icontains=query)
                | Q(device__workplace__employee__name__icontains=query)
                | Q(device__workplace__employee__surname__icontains=query)
                | Q(device__workplace__employee__last_name__icontains=query)
                | Q(quantity__icontains=query)
                | Q(serial__icontains=query)
                | Q(invent__icontains=query)
            )
            .select_related("categories")
            .prefetch_related("device")
            .distinct()
        )
        return object_list


class ConsumablesCategoriesView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    """_ConsumablesCategoriesView_
    List of consumables instances filtered by categories

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        paginate_by (int, optional): _add pagination_
        model (Consumables): _base model for list_
    """

    permission_required = "consumables.view_consumables"
    template_name = "consumables/consumables_list.html"
    paginate_by = DataMixin.paginate
    model = Consumables

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, link for search, link to create consumables, categories for filtering queryset_
        """
        cons_cat = cache.get("cons_cat")
        if not cons_cat:
            cons_cat = Categories.objects.all()
            cache.set("cons_cat", cons_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Расходники",
            searchlink="consumables:consumables_search",
            add="consumables:new-consumables",
            menu_categories=cons_cat,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_queryset_

        Returns:
            object_list (Consumables): _filtered by categories_
        """
        object_list = Consumables.objects.filter(
            categories__slug=self.kwargs["category_slug"]
        ).select_related("categories")
        return object_list


class ConsumablesRestView(DataMixin, FormMessageMixin, viewsets.ModelViewSet):
    """_ConsumablesRestView_ returns consumables

    Other parameters:
        queryset (Consumables):
        serializer_class (ConsumablesModelSerializer):
        success_message (str):
        error_message (str):
    """

    queryset = Consumables.objects.all()
    serializer_class = ConsumablesModelSerializer
    success_message = "%(categories)s %(name)s успешно создано"
    error_message = "%(categories)s %(name)s не удалось создать"

    def get_serializer_context(self):
        """_context_ returns serializer context

        Returns:
            context (list[]): _serializer context_
        """
        context = super().get_serializer_context()
        return context


class CategoriesRestView(DataMixin, FormMessageMixin, viewsets.ModelViewSet):
    """_ConsumablesRestView_ returns categories of consumables

    Other parameters:
        queryset (Categories):
        serializer_class (CategoriesModelSerializer):
        success_message (str):
        error_message (str):
    """

    queryset = Categories.objects.all()
    serializer_class = CategoriesModelSerializer
    success_message = "Категория %(name)s успешно создана"
    error_message = "Категория %(name)s не удалось создать"

    def get_serializer_context(self):
        """_context_ returns serializer context

        Returns:
            context (list[]): _serializer context_
        """
        context = super().get_serializer_context()
        context.update({"request": self.request})
        context.update({"menu": menu})
        return context


class ConsumablesDetailView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DataMixin,
    FormMixin,
    generic.DetailView,
):
    """_ConsumablesDetailView_
    Detail of consumables instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Consumables): _base model for list_
        form_class (StockAddForm): _form for adding consumables to the stock_
    """

    permission_required = "consumables.view_consumables"
    model = Consumables
    template_name = "consumables/consumables_detail.html"
    form_class = StockAddForm

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, links to create, update and delete consumables instance_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Расходник",
            add="consumables:new-consumables",
            update="consumables:consumables-update",
            delete="consumables:consumables-delete",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ConsumablesCreate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, CreateView
):
    """_ConsumablesCreate_
    Create of consumables instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Consumables): _base model for list_
        form_class (ConsumablesForm): _form class to view_
        success_message (str):
        error_message (str):
    """

    permission_required = "consumables.add_consumables"
    model = Consumables
    form_class = ConsumablesForm
    template_name = "Forms/add.html"
    success_message = "Расходник %(name)s успешно создан"
    error_message = "Расходник %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Добавить расходник",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ConsumablesUpdate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, UpdateView
):
    """_ConsumablesUpdate_
    Update of consumables instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Consumables): _base model for list_
        form_class (ConsumablesForm): _form class to view_
        success_message (str):
        error_message (str):
    """

    permission_required = "consumables.change_consumables"
    model = Consumables
    template_name = "Forms/add.html"
    form_class = ConsumablesForm
    success_message = "Расходник %(name)s успешно обновлен"
    error_message = "Расходник %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать расходник")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ConsumablesDelete(  # type: ignore[misc]
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, DeleteView
):
    """_ConsumablesDelete_
    Delete of consumables instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Consumables): _base model for list_
        success_url (str): _switches to url in case of successful deletion_
        success_message (str):
        error_message (str):
    """

    permission_required = "consumables.delete_consumables"
    model = Consumables
    template_name = "Forms/delete.html"
    success_url = reverse_lazy("consumables:consumables_list")
    success_message = "Расходник успешно удален"
    error_message = "Расходник не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to consumables list_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Удалить расходник", selflink="consumables:consumables_list"
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ExportConsumable(View):
    """_ExportConsumable_
    Returns an Excel file with all records of consumables from the database
    """

    def get(self, *args, **kwargs):
        """extracts all records of consumables from the database and converts them into an xlsx file

        Returns:
            response (HttpResponse): _returns xlsx file_

        Other parameters:
            resource (ConsumableResource): _dict of consumables for export into an xlsx file_
        """
        resource = ConsumableResource()
        dataset = resource.export()
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f'Consumables_{datetime.today().strftime("%Y_%m_%d")}',
                ext="xlsx",
            )
        )
        return response


class ExportConsumableCategory(View):
    """_ExportConsumableCategory_
    Returns an Excel file with filtered records by categories of consumables from the database
    """

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_ The function is used to return a list of categories

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to consumables list_
        """
        cons_cat = cache.get("cons_cat")
        if not cons_cat:
            cons_cat = Categories.objects.all()
            cache.set("cons_cat", cons_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(menu_categories=cons_cat)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get(self, queryset=None, *args, **kwargs):
        """extracts filtered records by categories of consumables from the database and converts them into an xlsx file

        Returns:
            response (HttpResponse): _returns xlsx file_

        Other parameters:
            resource (ConsumableResource): _dict of consumables for export into an xlsx file_
        """
        queryset = Consumables.objects.filter(
            categories__slug=self.kwargs["category_slug"]
        )
        resource = ConsumableResource()
        dataset = resource.export(queryset, *args, **kwargs)
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f'Consumables_{datetime.today().strftime("%Y_%m_%d")}',
                ext="xlsx",
            )
        )
        return response


# Комплектующие
class AccessoriesView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    """_AccessoriesView_
    List of accessories instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        paginate_by (int, optional): _add pagination_
        model (Accessories): _base model for list_
    """

    permission_required = "consumables.view_accessories"
    template_name = "consumables/accessories_list.html"
    paginate_by = DataMixin.paginate
    model = Accessories

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, link for search, link to create consumables, categories for filtering queryset_
        """
        acc_cat = cache.get("acc_cat")
        if not acc_cat:
            acc_cat = AccCat.objects.all()
            cache.set("acc_cat", acc_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Комплектующие",
            searchlink="consumables:accessories_search",
            add="consumables:new-accessories",
            menu_categories=acc_cat,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_queryset_

        Returns:
            object_list (Accessories): _description_
        """
        query = self.request.GET.get("q")
        if not query:
            query = ""
        object_list = (
            Accessories.objects.filter(
                Q(name__icontains=query)
                | Q(manufacturer__name__icontains=query)
                | Q(categories__name__icontains=query)
                | Q(device__name__icontains=query)
                | Q(device__workplace__name__icontains=query)
                | Q(device__workplace__room__name__icontains=query)
                | Q(device__workplace__room__building__icontains=query)
                | Q(device__workplace__employee__name__icontains=query)
                | Q(device__workplace__employee__surname__icontains=query)
                | Q(device__workplace__employee__last_name__icontains=query)
                | Q(quantity__icontains=query)
                | Q(serial__icontains=query)
                | Q(invent__icontains=query)
            )
            .select_related("categories")
            .prefetch_related("device")
            .distinct()
        )
        return object_list


class AccessoriesCategoriesView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    """_AccessoriesCategoriesView_
    List of accessories instances filtered by categories

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        paginate_by (int, optional): _add pagination_
        model (Accessories): _base model for list_
    """

    permission_required = "consumables.view_accessories"
    template_name = "consumables/accessories_list.html"
    paginate_by = DataMixin.paginate
    model = Accessories

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, link for search, link to create accessories, categories for filtering queryset_
        """
        acc_cat = cache.get("acc_cat")
        if not acc_cat:
            acc_cat = AccCat.objects.all()
            cache.set("acc_cat", acc_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Комплектующие",
            searchlink="consumables:accessories_search",
            add="consumables:new-accessories",
            menu_categories=acc_cat,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_queryset_

        Returns:
            object_list (Accessories): _filtered by categories_
        """
        object_list = Accessories.objects.filter(
            categories__slug=self.kwargs["category_slug"]
        ).select_related("categories")
        return object_list


class AccessoriesRestView(DataMixin, FormMessageMixin, viewsets.ModelViewSet):
    """_AccessoriesRestView_ returns accessories

    Other parameters:
        queryset (Accessories):
        serializer_class (AccessoriesModelSerializer):
        success_message (str):
        error_message (str):
    """

    queryset = Accessories.objects.all()
    serializer_class = AccessoriesModelSerializer
    success_message = "%(categories)s %(name)s успешно создано"
    error_message = "%(categories)s %(name)s не удалось создать"


class AccCatRestView(
    LoginRequiredMixin, DataMixin, FormMessageMixin, viewsets.ModelViewSet
):
    """_AccCatRestView_ returns categories of accessories

    Other parameters:
        queryset (AccCat):
        serializer_class (AccCatModelSerializer):
        success_message (str):
        error_message (str):
    """

    queryset = AccCat.objects.all()
    serializer_class = AccCatModelSerializer
    success_message = "Категория %(name)s успешно создана"
    error_message = "Категория %(name)s не удалось создать"


class AccessoriesDetailView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DataMixin,
    FormMixin,
    generic.DetailView,
):
    """_AccessoriesDetailView_
    Detail of accessories instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Accessories): _base model for list_
        form_class (StockAddForm): _form for adding accessories to the stock_
    """

    permission_required = "consumables.view_accessories"
    model = Accessories
    template_name = "consumables/accessories_detail.html"
    form_class = StockAddForm

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, links to create, update and delete accessories instance_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Комплектующее",
            add="consumables:new-accessories",
            update="consumables:accessories-update",
            delete="consumables:accessories-delete",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class AccessoriesCreate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, CreateView
):
    """_AccessoriesCreate_
    Create of accessories instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Accessories): _base model for list_
        form_class (AccessoriesForm): _form class to view_
        success_message (str):
        error_message (str):
    """

    permission_required = "consumables.add_accessories"
    model = Accessories
    form_class = AccessoriesForm
    template_name = "Forms/add.html"
    success_message = "Комплектующее %(name)s успешно создано"
    error_message = "Комплектующее %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Добавить комплектующее",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class AccessoriesUpdate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, UpdateView
):
    """_AccessoriesUpdate_
    Update of accessories instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Accessories): _base model for list_
        form_class (AccessoriesForm): _form class to view_
        success_message (str):
        error_message (str):
    """

    permission_required = "consumables.change_accessories"
    model = Accessories
    template_name = "Forms/add.html"
    form_class = AccessoriesForm
    success_message = "Комплектующее %(name)s успешно обновлен"
    error_message = "Комплектующее %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать комплектующее")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class AccessoriesDelete(  # type: ignore[misc]
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, DeleteView
):
    """_AccessoriesDelete_
    Delete of accessories instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Accessories): _base model for list_
        success_url (str): _switches to url in case of successful deletion_
        success_message (str):
        error_message (str):
    """

    permission_required = "consumables.delete_accessories"
    model = Accessories
    template_name = "Forms/delete.html"
    success_url = reverse_lazy("consumables:accessories_list")
    success_message = "Комплектующее успешно удален"
    error_message = "Комплектующее не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to accessories list_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Удалить комплектующее", selflink="consumables:accessories_list"
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ExportAccessories(View):
    """_ExportAccessories_
    Returns an Excel file with all records of accessories from the database
    """

    def get(self, *args, **kwargs):
        """extracts all records of accessories from the database and converts them into an xlsx file

        Returns:
            response (HttpResponse): _returns xlsx file_

        Other parameters:
            resource (AccessoriesResource): _dict of accessories for export into an xlsx file_
        """
        resource = AccessoriesResource()
        dataset = resource.export()
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f'Accessories_{datetime.today().strftime("%Y_%m_%d")}',
                ext="xlsx",
            )
        )
        return response


class ExportAccessoriesCategory(View):
    """_ExportAccessoriesCategory_
    Returns an Excel file with filtered records by categories of accessories from the database
    """

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_ The function is used to return a list of categories

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to accessories list_
        """
        acc_cat = cache.get("acc_cat")
        if not acc_cat:
            acc_cat = AccCat.objects.all()
            cache.set("acc_cat", acc_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(menu_categories=acc_cat)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get(self, queryset=None, *args, **kwargs):
        """extracts filtered records by categories of accessories from the database and converts them into an xlsx file

        Returns:
            response (HttpResponse): _returns xlsx file_

        Other parameters:
            resource (AccessoriesResource): _dict of accessories for export into an xlsx file_
        """
        queryset = Accessories.objects.filter(
            categories__slug=self.kwargs["category_slug"]
        )
        resource = AccessoriesResource()
        dataset = resource.export(queryset, *args, **kwargs)
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f'Accessories_{datetime.today().strftime("%Y_%m_%d")}',
                ext="xlsx",
            )
        )
        return response
