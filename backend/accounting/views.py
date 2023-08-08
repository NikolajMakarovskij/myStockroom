from django.core.cache import cache
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets
from core.utils import menu, DataMixin, FormMessageMixin
from .forms import AccountingForm, CategoriesForm
from .models import Accounting, Categories
from .serializers import AccountingModelSerializer, CategoriesModelSerializer


# Index
class AccountingIndexView(LoginRequiredMixin, generic.TemplateView):
    """
    Home
    """
    template_name = 'accounting/accounting_index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Расходники и комплектующие'
        context['menu'] = menu
        return context


# Accounting
class AccountingView(LoginRequiredMixin, DataMixin, generic.ListView):
    template_name = 'accounting/accounting_list.html'
    model = Accounting

    def get_context_data(self, *, object_list=None, **kwargs):
        acn_cat = cache.get('acn_cat')
        if not acn_cat:
            acn_cat = Categories.objects.all()
            cache.set('acn_cat', acn_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Баланс", searchlink='accounting:accounting_search',
                                      add='accounting:new-accounting', menu_categories=acn_cat)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            query = ''
        object_list = Accounting.objects.filter(
            Q(name__icontains=query) |
            Q(account__icontains=query) |
            Q(consumable__name__icontains=query) |
            Q(accessories__name__icontains=query) |
            Q(categories__name__icontains=query) |
            Q(code__icontains=query) |
            Q(quantity__icontains=query) |
            Q(cost__icontains=query) |
            Q(note__icontains=query)
        ).select_related('categories', 'consumable', 'accessories')
        return object_list


class AccountingCategoriesView(LoginRequiredMixin, DataMixin, generic.ListView):
    template_name = 'accounting/accounting_list.html'
    model = Accounting.objects

    def get_context_data(self, *, object_list=None, **kwargs):
        acn_cat = cache.get('acn_cat')
        if not acn_cat:
            acn_cat = Categories.objects.all()
            cache.set('acn_cat', acn_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Баланс", searchlink='accounting:accounting_search',
                                      add='accounting:new-accounting', menu_categories=acn_cat)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        object_list = Accounting.objects.filter(categories__slug=self.kwargs['category_slug']).select_related(
            'categories', 'consumable', 'accessories')
        return object_list


class AccountingRestView(DataMixin, FormMessageMixin, viewsets.ModelViewSet):
    queryset = Accounting.objects.all()
    serializer_class = AccountingModelSerializer
    success_message = f"%(categories)s %(name)s успешно создано"
    error_message = f"%(categories)s %(name)s не удалось создать"

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        context.update({"menu": menu})
        return context


class AccountingDetailView(LoginRequiredMixin, DataMixin, generic.DetailView):
    model = Accounting
    template_name = 'accounting/accounting_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Расходник", add='accounting:new-accounting',
                                      update='accounting:accounting-update', delete='accounting:accounting-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class AccountingCreate(LoginRequiredMixin, DataMixin, FormMessageMixin, CreateView):
    model = Accounting
    form_class = AccountingForm
    template_name = 'Forms/add.html'
    success_message = f"Расходник %(name)s успешно создан"
    error_message = f"Расходник %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить расходник", )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class AccountingUpdate(LoginRequiredMixin, DataMixin, FormMessageMixin, UpdateView):
    model = Accounting
    template_name = 'Forms/add.html'
    form_class = AccountingForm
    success_message = f"Расходник %(name)s успешно обновлен"
    error_message = f"Расходник %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать расходник")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class AccountingDelete(LoginRequiredMixin, DataMixin, FormMessageMixin, DeleteView):
    model = Accounting
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('accounting:accounting_list')
    success_message = f"Расходник успешно удален"
    error_message = f"Расходник не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить расходник", selflink='accounting:accounting_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


# Categories
class CategoryView(LoginRequiredMixin, DataMixin, generic.ListView):
    template_name = 'accounting/categories_list.html'
    model = Categories

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Категории", searchlink='accounting:categories_search',
                                      add='accounting:new-categories')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            query = ''
        object_list = Categories.objects.filter(Q(name__icontains=query))
        return object_list


class CategoriesRestView(DataMixin, FormMessageMixin, viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesModelSerializer
    success_message = f"Категория %(name)s успешно создана"
    error_message = f"Категория %(name)s не удалось создать"

    def get_serializer_context(self):
        context = super().get_serializer_context()
        return context


class CategoryCreate(LoginRequiredMixin, DataMixin, FormMessageMixin, CreateView):
    model = Categories
    form_class = CategoriesForm
    template_name = 'Forms/add.html'
    success_message = f"Категория %(name)s успешно создан"
    error_message = f"Категорию %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить категорию", )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class CategoryUpdate(LoginRequiredMixin, DataMixin, FormMessageMixin, UpdateView):
    model = Categories
    template_name = 'Forms/add.html'
    form_class = AccountingForm
    success_message = f"Категория %(name)s успешно обновлен"
    error_message = f"Категорию %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать категорию")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class CategoryDelete(LoginRequiredMixin, DataMixin, FormMessageMixin, DeleteView):
    model = Categories
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('accounting:categories_list')
    success_message = f"Категория успешно удалена"
    error_message = f"Категорию не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить категорию", selflink='accounting:categories_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context
