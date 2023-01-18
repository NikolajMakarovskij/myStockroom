from django.urls import reverse_lazy
from .forms import employeeForm, postForm, departamentForm
from .models import Employee, Departament, Post
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from catalog.utils import DataMixin

#Сотрудники 
class EmployeeListView(DataMixin, generic.ListView):
    model = Employee
    template_name = 'employee/employee_list.html' 
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Список сотрудников", searchlink='employee:employee', add='employee:new-employee')
        context = dict(list(context.items()) + list(c_def.items()))
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = Employee.objects.filter(
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
    model = Employee
    template_name = 'employee/employee_detail.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Сотрудник",add='employee:new-employee',update='employee:employee-update',delete='employee:employee-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class EmployeeCreate(DataMixin, CreateView):
    model = Employee
    form_class = employeeForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('employee:employee')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить сотрудника",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class EmployeeUpdate(DataMixin, UpdateView):
    model = Employee
    template_name = 'Forms/add.html'
    form_class = employeeForm
    success_url = reverse_lazy('employee:employee')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать сотрудника",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class EmployeeDelete(DataMixin, DeleteView):
    model = Employee
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('employee:employee')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить сотрудника",selflink='employee:employee')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Должность
class postListView(DataMixin, generic.ListView):
    model = Post
    template_name = 'employee/post_list.html' 
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Список должностей", searchlink='employee:post',add='employee:new-post')
        context = dict(list(context.items()) + list(c_def.items()))
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = Post.objects.filter(
                Q(name__icontains=query) | 
                Q(departament__name__icontains=query)  
        )
        return object_list

class postDetailView(DataMixin, generic.DetailView):
    model = Post
    template_name = 'employee/post_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Должность",add='employee:new-post',update='employee:post-update',delete='employee:post-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class postCreate(DataMixin, CreateView):
    model = Post
    form_class = postForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('employee:post')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить должность",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class postUpdate(DataMixin, UpdateView):
    model = Post
    template_name = 'Forms/add.html'
    form_class = postForm
    success_url = reverse_lazy('employee:post')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать должность",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class postDelete(DataMixin, DeleteView):
    model = Post
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('employee:post')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить должность",selflink='employee:post')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Отдел
class departamentListView(DataMixin, generic.ListView):
    model = Departament
    template_name = 'employee/departament_list.html' 
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Список отделов", searchlink='employee:departament',add='employee:new-departament')
        context = dict(list(context.items()) + list(c_def.items()))
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = Departament.objects.filter(
                Q(name__icontains=query)  
        )
        return object_list

class departamentDetailView(DataMixin, generic.DetailView):
    model = Departament
    template_name = 'employee/departament_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Отдел",add='employee:new-departament',update='employee:departament-update',delete='employee:departament-delete')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class departamentCreate(DataMixin, CreateView):
    model = Departament
    form_class = departamentForm
    template_name = 'Forms/add.html'
    success_url = reverse_lazy('employee:departament')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить отдел",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class departamentUpdate(DataMixin, UpdateView):
    model = Departament
    template_name = 'Forms/add.html'
    form_class = departamentForm
    success_url = reverse_lazy('employee:departament')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактировать отдел",)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class departamentDelete(DataMixin, DeleteView):
    model = Departament
    template_name = 'Forms/delete.html'
    success_url = reverse_lazy('employee:departament')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить отдел",selflink='employee:departament')
        context = dict(list(context.items()) + list(c_def.items()))
        return context