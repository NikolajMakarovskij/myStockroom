from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from core.utils import DataMixin


class StockroomIndexView(LoginRequiredMixin, DataMixin, generic.TemplateView):
    """
    Index
    """
    template_name = 'stock/stock_index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Расходники и комплектующие",
            searchlink='stockroom:stock_search',
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

