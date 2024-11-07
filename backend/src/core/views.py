from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .utils import menu


# Главная
class IndexView(LoginRequiredMixin, generic.TemplateView):
    """_IndexView_ Home page

    Other parameters:
        template_name (str): _path to template_
    """

    template_name = "index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to accessories list_
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная страница"
        context["menu"] = menu
        return context
