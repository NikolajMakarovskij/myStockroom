from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from core.utils import menu


class StockroomIndexView(LoginRequiredMixin, generic.TemplateView):
    """
    Index
    """
    template_name = 'stock/stock_index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Расходники и комплектующие'
        context['menu'] = menu
        return context
