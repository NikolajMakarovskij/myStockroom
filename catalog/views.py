from .forms import *
from .models import References
from django.views import generic
from .utils import *


#Главная
class indexView(generic.ListView):
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['menu'] = menu
        return context

#Справочники
class referencesView(DataMixin, generic.ListView):
    model = References
    template_name = 'catalog/references.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Справочники", searchlink='catalog:references',)
        context = dict(list(context.items()) + list(c_def.items()))
        return context














