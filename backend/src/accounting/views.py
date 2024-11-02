from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from rest_framework import viewsets

from core.utils import DataMixin, FormMessageMixin, menu

from .forms import AccountingForm, CategoriesForm
from .models import Accounting, Categories
from .serializers import AccountingModelSerializer, CategoriesModelSerializer


# Index
class AccountingIndexView(
    LoginRequiredMixin, PermissionRequiredMixin, generic.TemplateView
):
    """_AccountingIndexView_
    Home page for accounting app

    Returns:
        template_name (str): _path to template_
        permission_required (str): _permissions_
    """

    template_name = "accounting/accounting_index.html"
    permission_required = "accounting.view_accounting"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (list[str]): _returns title, side menu_
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Расходники и комплектующие"
        context["menu"] = menu
        return context


# Accounting
class AccountingView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    """_AccountingView_
    List of accounting instances

    Returns:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        paginate_by (int, optional): _add pagination_
        model (Accounting): _base model for list_
    """
    permission_required = "accounting.view_accounting"
    template_name = "accounting/accounting_list.html"
    paginate_by = DataMixin.paginate
    model = Accounting

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, link for search, link to create accounting, categories for filtering queryset_
        """
        acn_cat = cache.get("acn_cat")
        if not acn_cat:
            acn_cat = Categories.objects.all()
            cache.set("acn_cat", acn_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Баланс",
            searchlink="accounting:accounting_search",
            add="accounting:new-accounting",
            menu_categories=acn_cat,
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
        object_list = Accounting.objects.filter(
            Q(name__icontains=query)
            | Q(account__icontains=query)
            | Q(consumable__name__icontains=query)
            | Q(accessories__name__icontains=query)
            | Q(categories__name__icontains=query)
            | Q(code__icontains=query)
            | Q(quantity__icontains=query)
            | Q(cost__icontains=query)
            | Q(note__icontains=query)
        ).select_related("categories", "consumable", "accessories")
        return object_list


class AccountingCategoriesView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    """_AccountingCategoriesView_
    List of accounting instances filtered by categories

    Returns:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        paginate_by (int, optional): _add pagination_
        model (Accounting): _base model for list_
    """
    permission_required = "accounting.view_accounting"
    template_name = "accounting/accounting_list.html"
    paginate_by = DataMixin.paginate
    model = Accounting

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, link for search, link to create accounting, categories for filtering queryset_
        """
        acn_cat = cache.get("acn_cat")
        if not acn_cat:
            acn_cat = Categories.objects.all()
            cache.set("acn_cat", acn_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Баланс",
            searchlink="accounting:accounting_search",
            add="accounting:new-accounting",
            menu_categories=acn_cat,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_queryset_ 

        Returns:
            object_list (Accounting): _filtered by categories_
        """
        object_list = Accounting.objects.filter(
            categories__slug=self.kwargs["category_slug"]
        ).select_related("categories", "consumable", "accessories")
        return object_list


class AccountingRestView(DataMixin, FormMessageMixin, viewsets.ModelViewSet):
    """_AccountingRestView_ returns accounting

    Returns:
        queryset (Accounting): 
        serializer_class (AccountingModelSerializer): 
        success_message (str):
        error_message (str):
    """
    queryset = Accounting.objects.all()
    serializer_class = AccountingModelSerializer
    success_message = "%(categories)s %(name)s успешно создано"
    error_message = "%(categories)s %(name)s не удалось создать"

    def get_serializer_context(self):
        """_context_ returns serializer context

        Returns:
            context (list[]): _serializer context_
        """
        context = super().get_serializer_context()
        context.update({"request": self.request})
        context.update({"menu": menu})
        return context


class AccountingDetailView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.DetailView
):
    """_AccountingDetailView_
    Detail of accounting instances

    Returns:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Accounting): _base model for list_
    """
    permission_required = "accounting.view_accounting"
    model = Accounting
    template_name = "accounting/accounting_detail.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, links to create, update and delete accounting instance_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Расходник",
            add="accounting:new-accounting",
            update="accounting:accounting-update",
            delete="accounting:accounting-delete",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class AccountingCreate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, CreateView
):
    """_AccountingCreate_
    Create of accounting instances

    Returns:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Accounting): _base model for list_
        form_class (AccountingForm): _form class to view_
        success_message (str):
        error_message (str):
    """
    permission_required = "accounting.add_accounting"
    model = Accounting
    form_class = AccountingForm
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


class AccountingUpdate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, UpdateView
):
    """_AccountingUpdate_
    Update of accounting instances

    Returns:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Accounting): _base model for list_
        form_class (AccountingForm): _form class to view_
        success_message (str):
        error_message (str):
    """
    permission_required = "accounting.change_accounting"
    model = Accounting
    template_name = "Forms/add.html"
    form_class = AccountingForm
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


class AccountingDelete(# type: ignore[misc]
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, DeleteView
    ):  
    """_AccountingDelete_
    Delete of accounting instances

    Returns:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Accounting): _base model for list_
        success_url (str): _switches to url in case of successful deletion_
        success_message (str):
        error_message (str):
    """
    permission_required = "accounting.delete_accounting"
    model = Accounting
    template_name = "Forms/delete.html"
    success_url = reverse_lazy("accounting:accounting_list")
    success_message = "Расходник успешно удален"
    error_message = "Расходник не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to accounting list_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Удалить расходник", selflink="accounting:accounting_list"
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


# Categories
class CategoryView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    """_CategoryView_
    List of categories instances

    Returns:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        paginate_by (int, optional): _add pagination_
        model (Categories): _base model for list_
    """
    permission_required = "accounting.view_category"
    template_name = "accounting/categories_list.html"
    paginate_by = DataMixin.paginate
    model = Categories

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to add category, link for search_
        """

        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Категории",
            searchlink="accounting:categories_search",
            add="accounting:new-categories",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_returns queryset_

        Returns:
            object_list (Categories): _returns queryset_
        """
        query = self.request.GET.get("q")
        if not query:
            query = ""
        object_list = Categories.objects.filter(Q(name__icontains=query))
        return object_list


class CategoriesRestView(DataMixin, FormMessageMixin, viewsets.ModelViewSet):
    """_CategoriesRestView_ returns categories

    Returns:
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
        return context


class CategoryCreate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, CreateView
):
    """_CategoryCreate_
    Create of category instances

    Returns:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Categories): _base model for list_
        form_class (CategoriesForm): _form class to view_
        success_message (str):
        error_message (str):
    """
    permission_required = "accounting.add_category"
    model = Categories
    form_class = CategoriesForm
    template_name = "Forms/add.html"
    success_url = reverse_lazy("accounting:categories_list")
    success_message = "Категория %(name)s успешно создан"
    error_message = "Категорию %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title_
        """

        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Добавить категорию",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class CategoryUpdate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, UpdateView
):
    """_CategoryUpdate_
    Update of category instances

    Returns:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Categories): _base model for list_
        form_class (CategoriesForm): _form class to view_
        success_message (str):
        error_message (str):
    """
    permission_required = "accounting.update_category"
    model = Categories
    template_name = "Forms/add.html"
    form_class = CategoriesForm
    success_url = reverse_lazy("accounting:categories_list")
    success_message = "Категория %(name)s успешно обновлен"
    error_message = "Категорию %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title_
        """

        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать категорию")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class CategoryDelete( # type: ignore[misc]
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, DeleteView
    ):
    """_CategoryDelete_
    Delete of accounting instances

    Returns:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Categories): _base model for list_
        success_url (str): _switches to url in case of successful deletion_
        success_message (str):
        error_message (str):
    """
    permission_required = "accounting.delete_category"
    model = Categories
    template_name = "Forms/delete.html"
    success_url = reverse_lazy("accounting:categories_list")
    success_message = "Категория успешно удалена"
    error_message = "Категорию не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to accounting list_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Удалить категорию", selflink="accounting:categories_list"
        )
        context = dict(list(context.items()) + list(c_def.items()))

        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Удалить категорию", selflink="accounting:categories_list"
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context
