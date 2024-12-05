from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic

from core.utils import menu


class StockroomIndexView(
    LoginRequiredMixin, PermissionRequiredMixin, generic.TemplateView
):
    """_StockroomIndexView_
    Home page for stockroom app

    Returns:
        template_name (str): _path to template_
        permission_required (str): _permissions_
    """

    permission_required = "stockroom.view_stockroom"
    template_name = "stock/stock_index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (list[str]): _returns title, side menu_
        """

        context = super().get_context_data(**kwargs)
        context["title"] = "Расходники и комплектующие"
        context["menu"] = menu
        return context
