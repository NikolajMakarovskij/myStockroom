from django.urls import reverse_lazy
from ..forms import employeeForm, postForm, departamentForm
from ..models.employee_model import *
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from ..utils import DataMixin

#Сотрудники 
class EmployeeListView(DataMixin, generic.ListView):
    model = employee
    template_name = 'catalog/employee/employee_list.html' 
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Список сотрудников", searchlink='employee', add='new-employee')
        context = dict(list(context.items()) + list(c_def.items()))
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = employee.objects.filter(
                Q(name__icontains=query) | 
                Q(sername__icontains=query) | 
                Q(family__icontains=query) | 
                Q(post__departament__name__icontains=query) |
                Q(post__name__icontains=query) |  
                Q(workplace__name__icontains=query) |
                Q(workplace__room__name__icontains=query) |
                Q(workplace__room__floor__icontains=query) |
                Q(workplace__room__building__icontains=query) 
        )
        return object_list

class EmployeeDetailView(DataMixin, generic.DetailView):
    model = employee
    template_name = 'catalog/employee/employee_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Сотрудник",add='new-employee',update='employee-update',delete='employee-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class EmployeeCreate(DataMixin, CreateView):
    model = employee
    form_class = employeeForm
    template_name = 'Forms/add.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить сотрудника",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class EmployeeUpdate(DataMixin, UpdateView):
    model = employee
    template_name = 'Forms/add.html'
    form_class = employeeForm
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать сотрудника",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class EmployeeDelete(DataMixin, DeleteView):
    model = employee
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('employee')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить сотрудника",selflink='employee')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Должность
class postListView(DataMixin, generic.ListView):
    model = post
    template_name = 'catalog/employee/post_list.html' 
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Список должностей", searchlink='post',add='new-post')
        context = dict(list(context.items()) + list(c_def.items()))
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = post.objects.filter(
                Q(name__icontains=query) | 
                Q(departament__name__icontains=query)  
        )
        return object_list

class postDetailView(DataMixin, generic.DetailView):
    model = post
    template_name = 'catalog/employee/post_detail.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Должность",add='new-post',update='post-update',delete='post-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class postCreate(DataMixin, CreateView):
    model = post
    form_class = postForm
    template_name = 'Forms/add.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить должность",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class postUpdate(DataMixin, UpdateView):
    model = post
    template_name = 'Forms/add.html'
    form_class = postForm
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать должность",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class postDelete(DataMixin, DeleteView):
    model = post
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('post')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить должность",selflink='post')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Отдел
class departamentListView(DataMixin, generic.ListView):
    model = departament
    template_name = 'catalog/employee/departament_list.html' 
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Список отделов", searchlink='departament',add='new-departament')
        context = dict(list(context.items()) + list(c_def.items()))
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = departament.objects.filter(
                Q(name__icontains=query)  
        )
        return object_list

class departamentDetailView(DataMixin, generic.DetailView):
    model = departament
    template_name = 'catalog/employee/departament_detail.html'
    success_url = reverse_lazy('departament')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Отдел",add='new-departament',update='departament-update',delete='departament-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class departamentCreate(DataMixin, CreateView):
    model = departament
    form_class = departamentForm
    template_name = 'Forms/add.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить отдел",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class departamentUpdate(DataMixin, UpdateView):
    model = departament
    template_name = 'Forms/add.html'
    form_class = departamentForm
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать отдел",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class departamentDelete(DataMixin, DeleteView):
    model = departament
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('departament')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить отдел",selflink='departament')
        context = dict(list(context.items()) + list(c_def.items()))
        return context