from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework import viewsets

from core.utils import menu, DataMixin, FormMessageMixin
from .forms import AccountingForm, CategoriesForm
from .models import Accounting, Categories
from .serializers import AccountingModelSerializer, CategoriesModelSerializer


# Index
class AccountingIndexView(
    LoginRequiredMixin, PermissionRequiredMixin, generic.TemplateView
):
    """
    Home
    """

    template_name = "accounting/accounting_index.html"
    permission_required = "accounting.view_accounting"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Расходники и комплектующие"
        context["menu"] = menu
        return context


# Accounting
class AccountingView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    permission_required = "accounting.view_accounting"
    template_name = "accounting/accounting_list.html"
    model = Accounting

    def get_context_data(self, *, object_list=None, **kwargs):
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
    permission_required = "accounting.view_accounting"
    template_name = "accounting/accounting_list.html"
    model = Accounting.objects

    def get_context_data(self, *, object_list=None, **kwargs):
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
        object_list = Accounting.objects.filter(
            categories__slug=self.kwargs["category_slug"]
        ).select_related("categories", "consumable", "accessories")
        return object_list


class AccountingRestView(DataMixin, FormMessageMixin, viewsets.ModelViewSet):
    queryset = Accounting.objects.all()
    serializer_class = AccountingModelSerializer
    success_message = "%(categories)s %(name)s успешно создано"
    error_message = "%(categories)s %(name)s не удалось создать"

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        context.update({"menu": menu})
        return context


class AccountingDetailView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.DetailView
):
    permission_required = "accounting.view_accounting"
    model = Accounting
    template_name = "accounting/accounting_detail.html"

    def get_context_data(self, *, object_list=None, **kwargs):
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
    permission_required = "accounting.add_accounting"
    model = Accounting
    form_class = AccountingForm
    template_name = "Forms/add.html"
    success_message = "Расходник %(name)s успешно создан"
    error_message = "Расходник %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Добавить расходник",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class AccountingUpdate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, UpdateView
):
    permission_required = "accounting.change_accounting"
    model = Accounting
    template_name = "Forms/add.html"
    form_class = AccountingForm
    success_message = "Расходник %(name)s успешно обновлен"
    error_message = "Расходник %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать расходник")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class AccountingDelete(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, DeleteView
):
    permission_required = "accounting.delete_accounting"
    model = Accounting
    template_name = "Forms/delete.html"
    success_url = reverse_lazy("accounting:accounting_list")
    success_message = "Расходник успешно удален"
    error_message = "Расходник не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
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
    permission_required = "accounting.view_category"
    template_name = "accounting/categories_list.html"
    model = Categories

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Категории",
            searchlink="accounting:categories_search",
            add="accounting:new-categories",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get("q")
        if not query:
            query = ""
        object_list = Categories.objects.filter(Q(name__icontains=query))
        return object_list


class CategoriesRestView(DataMixin, FormMessageMixin, viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesModelSerializer
    success_message = "Категория %(name)s успешно создана"
    error_message = "Категория %(name)s не удалось создать"

    def get_serializer_context(self):
        context = super().get_serializer_context()
        return context


class CategoryCreate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, CreateView
):
    permission_required = "accounting.add_category"
    model = Categories
    form_class = CategoriesForm
    template_name = "Forms/add.html"
    success_url = reverse_lazy("accounting:categories_list")
    success_message = "Категория %(name)s успешно создан"
    error_message = "Категорию %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Добавить категорию",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class CategoryUpdate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, UpdateView
):
    permission_required = "accounting.update_category"
    model = Categories
    template_name = "Forms/add.html"
    form_class = CategoriesForm
    success_url = reverse_lazy("accounting:categories_list")
    success_message = "Категория %(name)s успешно обновлен"
    error_message = "Категорию %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать категорию")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class CategoryDelete(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, DeleteView
):
    permission_required = "accounting.delete_category"
    model = Categories
    template_name = "Forms/delete.html"
    success_url = reverse_lazy("accounting:categories_list")
    success_message = "Категория успешно удалена"
    error_message = "Категорию не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Удалить категорию", selflink="accounting:categories_list"
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context
