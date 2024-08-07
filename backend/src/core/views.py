from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .utils import menu


# Главная
class IndexView(LoginRequiredMixin, generic.TemplateView):
    """_IndexView_ Home page

    Returns:
        context (dict[list[str], dict[str, str]]): _returns context, title, side menu_
    """

    template_name = "index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная страница"
        context["menu"] = menu
        return context
