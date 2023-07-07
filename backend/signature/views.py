from .forms import SignatureForm
from .models import Signature
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from catalog.utils import DataMixin, FormMessageMixin
from stockroom.forms import ConsumableInstallForm


class SignatureListView(DataMixin, generic.ListView):
    model = Signature
    template_name = 'signature/signature_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="ЭЦП", searchlink='signature:signature_search',
                                      add='signature:new-signature')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            query = ''
        object_list = Signature.objects.filter(
            Q(name__icontains=query) |
            Q(periodOpen__icontains=query) |
            Q(periodClose__icontains=query) |
            Q(employeeRegister__name__icontains=query) |
            Q(employeeStorage__name__icontains=query) |
            Q(storage__name__icontains=query) |
            Q(workstation__name__icontains=query) |
            Q(workstation__workplace__name__icontains=query) |
            Q(workstation__workplace__room__name__icontains=query) |
            Q(workstation__workplace__room__floor__icontains=query) |
            Q(workstation__workplace__room__building__icontains=query)
        ).select_related('employeeRegister', 'employeeStorage', 'storage', 'workstation', 'workstation__workplace',
                         'workstation__workplace__room')
        return object_list


class SignatureDetailView(DataMixin, FormMixin, generic.DetailView):
    model = Signature
    template_name = 'signature/signature_detail.html'
    form_class = ConsumableInstallForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="ЭЦП", add='signature:new-signature', update='signature:signature-update',
                                      delete='signature:signature-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class SignatureCreate(DataMixin, FormMessageMixin, CreateView):
    model = Signature
    form_class = SignatureForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('signature:signature_list')
    success_message = f"ЭЦП %(name)s успешно создана"
    error_message = f"ЭЦП %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить ЭЦП", )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class SignatureUpdate(DataMixin, FormMessageMixin, UpdateView):
    model = Signature
    template_name = 'Forms/add.html'
    form_class = SignatureForm
    success_url = reverse_lazy('signature:signature_list')
    success_message = f"ЭЦП %(name)s успешно обновлена"
    error_message = f"ЭЦП %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать ЭЦП", )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class SignatureDelete(DataMixin, FormMessageMixin, DeleteView):
    model = Signature
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('signature:signature_list')
    success_message = f"ЭЦП успешно удалена"
    error_message = f"ЭЦП не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить ЭЦП", selflink='signature:signature_list')
        context = dict(list(context.items()) + list(c_def.items()))
        return context
