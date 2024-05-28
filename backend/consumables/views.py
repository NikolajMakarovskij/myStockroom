from django.core.cache import cache
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework import viewsets
from core.utils import menu, DataMixin, FormMessageMixin
from stockroom.forms import StockAddForm
from .forms import ConsumablesForm, AccessoriesForm
from .models import Consumables, Categories, Accessories, AccCat
from .serializers import (
    ConsumablesModelSerializer,
    CategoriesModelSerializer,
    AccessoriesModelSerializer,
    AccCatModelSerializer,
)
from consumables.resources import ConsumableResource, AccessoriesResource
from django.http import HttpResponse
from datetime import datetime


# Расходники главная
class ConsumableIndexView(
    LoginRequiredMixin, PermissionRequiredMixin, generic.TemplateView
):
    """
    Главная
    """

    template_name = "consumables/consumables_index.html"
    permission_required = "consumables.view_consumables"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Расходники и комплектующие"
        context["menu"] = menu
        return context


# Расходники
class ConsumablesView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    permission_required = "consumables.view_consumables"
    template_name = "consumables/consumables_list.html"
    model = Consumables

    def get_context_data(self, *, object_list=None, **kwargs):
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
    permission_required = "consumables.view_consumables"
    template_name = "consumables/consumables_list.html"
    model = Consumables.objects

    def get_context_data(self, *, object_list=None, **kwargs):
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
        object_list = Consumables.objects.filter(
            categories__slug=self.kwargs["category_slug"]
        ).select_related("categories")
        return object_list


class ConsumablesRestView(DataMixin, FormMessageMixin, viewsets.ModelViewSet):
    queryset = Consumables.objects.all()
    serializer_class = ConsumablesModelSerializer
    success_message = "%(categories)s %(name)s успешно создано"
    error_message = "%(categories)s %(name)s не удалось создать"

    def get_serializer_context(self):
        context = super().get_serializer_context()
        return context


class CategoriesRestView(DataMixin, FormMessageMixin, viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesModelSerializer
    success_message = "Категория %(name)s успешно создана"
    error_message = "Категория %(name)s не удалось создать"

    def get_serializer_context(self):
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
    permission_required = "consumables.view_consumables"
    model = Consumables
    template_name = "consumables/consumables_detail.html"
    form_class = StockAddForm

    def get_context_data(self, *, object_list=None, **kwargs):
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
    permission_required = "consumables.add_consumables"
    model = Consumables
    form_class = ConsumablesForm
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


class ConsumablesUpdate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, UpdateView
):
    permission_required = "consumables.change_consumables"
    model = Consumables
    template_name = "Forms/add.html"
    form_class = ConsumablesForm
    success_message = "Расходник %(name)s успешно обновлен"
    error_message = "Расходник %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать расходник")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ConsumablesDelete(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, DeleteView
):
    permission_required = "consumables.delete_consumables"
    model = Consumables
    template_name = "Forms/delete.html"
    success_url = reverse_lazy("consumables:consumables_list")
    success_message = "Расходник успешно удален"
    error_message = "Расходник не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Удалить расходник", selflink="consumables:consumables_list"
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ExportConsumable(View):
    def get(self, *args, **kwargs):
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
    def get_context_data(self, *, object_list=None, **kwargs):
        cons_cat = cache.get("cons_cat")
        if not cons_cat:
            cons_cat = Categories.objects.all()
            cache.set("cons_cat", cons_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(menu_categories=cons_cat)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get(self, queryset=None, *args, **kwargs):
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
    permission_required = "consumables.view_accessories"
    template_name = "consumables/accessories_list.html"
    model = Accessories

    def get_context_data(self, *, object_list=None, **kwargs):
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
    permission_required = "consumables.view_accessories"
    template_name = "consumables/accessories_list.html"
    model = Accessories.objects

    def get_context_data(self, *, object_list=None, **kwargs):
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
        object_list = Accessories.objects.filter(
            categories__slug=self.kwargs["category_slug"]
        ).select_related("categories")
        return object_list


class AccessoriesRestView(DataMixin, FormMessageMixin, viewsets.ModelViewSet):
    queryset = Accessories.objects.all()
    serializer_class = AccessoriesModelSerializer
    success_message = "%(categories)s %(name)s успешно создано"
    error_message = "%(categories)s %(name)s не удалось создать"


class AccCatRestView(
    LoginRequiredMixin, DataMixin, FormMessageMixin, viewsets.ModelViewSet
):
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
    permission_required = "consumables.view_accessories"
    model = Accessories
    template_name = "consumables/accessories_detail.html"
    form_class = StockAddForm

    def get_context_data(self, *, object_list=None, **kwargs):
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
    permission_required = "consumables.add_accessories"
    model = Accessories
    form_class = AccessoriesForm
    template_name = "Forms/add.html"
    success_message = "Комплектующее %(name)s успешно создано"
    error_message = "Комплектующее %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Добавить комплектующее",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class AccessoriesUpdate(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, UpdateView
):
    permission_required = "consumables.change_accessories"
    model = Accessories
    template_name = "Forms/add.html"
    form_class = AccessoriesForm
    success_message = "Комплектующее %(name)s успешно обновлен"
    error_message = "Комплектующее %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать комплектующее")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class AccessoriesDelete(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, FormMessageMixin, DeleteView
):
    permission_required = "consumables.delete_accessories"
    model = Accessories
    template_name = "Forms/delete.html"
    success_url = reverse_lazy("consumables:accessories_list")
    success_message = "Комплектующее успешно удален"
    error_message = "Комплектующее не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Удалить комплектующее", selflink="consumables:accessories_list"
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ExportAccessories(View):
    def get(self, *args, **kwargs):
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
    def get_context_data(self, *, object_list=None, **kwargs):
        acc_cat = cache.get("acc_cat")
        if not acc_cat:
            acc_cat = AccCat.objects.all()
            cache.set("acc_cat", acc_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(menu_categories=acc_cat)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get(self, queryset=None, *args, **kwargs):
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
