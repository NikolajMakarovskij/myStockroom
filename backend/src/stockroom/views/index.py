from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic

from core.utils import menu


class StockroomIndexView(LoginRequiredMixin, PermissionRequiredMixin, generic.TemplateView):
    """
    Index
    """
    permission_required = 'stockroom.view_stockroom'
    template_name = 'stock/stock_index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Расходники и комплектующие'
        context['menu'] = menu
        return context
