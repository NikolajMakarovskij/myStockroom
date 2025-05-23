from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from core.utils import DataMixin, FormMessageMixin, menu

from .forms import DepartamentForm, EmployeeForm, PostForm
from .models import Departament, Employee, Post


class IndexView(LoginRequiredMixin, PermissionRequiredMixin, generic.TemplateView):
    """_IndexView_
    Home page for employee app

    Returns:
        template_name (str): _path to template_
        permission_required (str): _permissions_
    """

    permission_required = "employee.view_employee"
    template_name = "employee/employee_index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (list[str]): _returns title, side menu_
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Сотрудники, Должности, Отделы"
        context["menu"] = menu
        return context


# Сотрудники
class EmployeeListView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DataMixin,
    generic.ListView,  # type: ignore[type-arg]
):
    """_EmployeeListView_
    List of employee instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        paginate_by (int, optional): _add pagination_
        model (Employee): _base model for list_
    """

    permission_required = "employee.view_employee"
    paginate_by = DataMixin.paginate
    model = Employee
    template_name = "employee/employee_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, link for search, link to create employee_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Список сотрудников",
            searchlink="employee:employee_search",
            add="employee:new-employee",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_queryset_

        Returns:
            object_list (Employee): _description_
        """
        query = self.request.GET.get("q")
        if not query:
            query = ""
        object_list = Employee.objects.filter(
            Q(name__icontains=query)
            | Q(surname__icontains=query)
            | Q(last_name__icontains=query)
            | Q(post__departament__name__icontains=query)
            | Q(post__name__icontains=query)
            | Q(workplace__name__icontains=query)
            | Q(workplace__room__name__icontains=query)
            | Q(workplace__room__floor__icontains=query)
            | Q(workplace__room__building__icontains=query)
        ).select_related(
            "workplace",
            "post",
        )
        return object_list


class EmployeeDetailView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DataMixin,
    generic.DetailView,  # type: ignore[type-arg]
):
    """_EmployeeDetailView_
    Detail of employee instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Employee): _base model for list_
    """

    permission_required = "employee.view_employee"
    paginate_by = DataMixin.paginate
    model = Employee
    template_name = "employee/employee_detail.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, links to create, update and delete employee instance_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Сотрудник",
            add="employee:new-employee",
            update="employee:employee-update",
            delete="employee:employee-delete",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class EmployeeCreate(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DataMixin,
    FormMessageMixin,
    CreateView,  # type: ignore[type-arg]
):
    """_EmployeeCreate_
    Create of employee instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Employee): _base model for list_
        form_class (EmployeeForm): _form class to view_
        success_message (str):
        error_message (str):
    """

    permission_required = "employee.add_employee"
    model = Employee
    form_class = EmployeeForm
    template_name = "Forms/add.html"
    success_url = reverse_lazy("employee:employee_list")
    success_message = "Сотрудник %(name)s успешно создан"
    error_message = "Сотрудника %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Добавить сотрудника",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class EmployeeUpdate(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DataMixin,
    FormMessageMixin,
    UpdateView,  # type: ignore[type-arg]
):
    """_EmployeeUpdate_
    Update of employee instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Employee): _base model for list_
        form_class (EmployeeForm): _form class to view_
        success_message (str):
        error_message (str):
    """

    permission_required = "employee.change_employee"
    model = Employee
    template_name = "Forms/add.html"
    form_class = EmployeeForm
    success_url = reverse_lazy("employee:employee_list")
    success_message = "Сотрудник %(name)s успешно обновлен"
    error_message = "Сотрудника %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Редактировать сотрудника",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class EmployeeDelete(  # type: ignore[misc]
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DataMixin,
    FormMessageMixin,
    DeleteView,  # type: ignore[type-arg]
):
    """_EmployeeDelete_
    Delete of employee instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Employee): _base model for list_
        success_url (str): _switches to url in case of successful deletion_
        success_message (str):
        error_message (str):
    """

    permission_required = "employee.delete_employee"
    model = Employee
    template_name = "Forms/delete.html"
    success_url = reverse_lazy("employee:employee_list")
    success_message = "Сотрудник успешно удален"
    error_message = "Сотрудника не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to employee list_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Удалить сотрудника", selflink="employee:employee_list"
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


# Должность
class PostListView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DataMixin,
    generic.ListView,  # type: ignore[type-arg]
):
    """_PostListView_
    List of post instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        paginate_by (int, optional): _add pagination_
        model (Post: _base model for list_
    """

    permission_required = "employee.view_post"
    paginate_by = DataMixin.paginate
    model = Post
    template_name = "employee/post_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, link for search, link to create post_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Список должностей",
            searchlink="employee:post_search",
            add="employee:new-post",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_queryset_

        Returns:
            object_list (Post): _description_
        """
        query = self.request.GET.get("q")
        if not query:
            query = ""
        object_list = Post.objects.filter(
            Q(name__icontains=query) | Q(departament__name__icontains=query)
        ).select_related("departament")
        return object_list


class PostDetailView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DataMixin,
    generic.DetailView,  # type: ignore[type-arg]
):
    """_PostDetailView_
    Detail of post instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Post): _base model for list_
    """

    permission_required = "employee.view_post"
    model = Post
    template_name = "employee/post_detail.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, links to create, update and delete post instance_
        """

        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Должность",
            add="employee:new-post",
            update="employee:post-update",
            delete="employee:post-delete",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class PostCreate(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DataMixin,
    FormMessageMixin,
    CreateView,  # type: ignore[type-arg]
):
    """_PostCreate_
    Create of post instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Post): _base model for list_
        form_class (PostForm): _form class to view_
        success_message (str):
        error_message (str):
    """

    permission_required = "employee.add_post"
    model = Post
    form_class = PostForm
    template_name = "Forms/add.html"
    success_url = reverse_lazy("employee:post_list")
    success_message = "Должность %(name)s успешно создана"
    error_message = "Должность %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Добавить должность",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class PostUpdate(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DataMixin,
    FormMessageMixin,
    UpdateView,  # type: ignore[type-arg]
):
    """_PostUpdate_
    Update of post instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Post): _base model for list_
        form_class (PostForm): _form class to view_
        success_message (str):
        error_message (str):
    """

    permission_required = "employee.change_post"
    model = Post
    template_name = "Forms/add.html"
    form_class = PostForm
    success_url = reverse_lazy("employee:post_list")
    success_message = "Должность %(name)s успешно обновлена"
    error_message = "Должность %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Редактировать должность",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class PostDelete(  # type: ignore[misc]
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DataMixin,
    FormMessageMixin,
    DeleteView,  # type: ignore[type-arg]
):
    """_PostDelete_
    Delete of post instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Post): _base model for list_
        success_url (str): _switches to url in case of successful deletion_
        success_message (str):
        error_message (str):
    """

    permission_required = "employee.delete_post"
    model = Post
    template_name = "Forms/delete.html"
    success_url = reverse_lazy("employee:post_list")
    success_message = "Должность успешно удалена"
    error_message = "Должность не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to post list_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Удалить должность", selflink="employee:post_list"
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


# Отдел
class DepartamentListView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DataMixin,
    generic.ListView,  # type: ignore[type-arg]
):
    """_DepartamentListView_
    List of departament instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        paginate_by (int, optional): _add pagination_
        model (Departament): _base model for list_
    """

    permission_required = "employee.view_departament"
    paginate_by = DataMixin.paginate
    model = Departament
    template_name = "employee/departament_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, link for search, link to create departament_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Список отделов",
            searchlink="employee:departament_search",
            add="employee:new-departament",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_queryset_

        Returns:
            object_list (Departament): _description_
        """
        query = self.request.GET.get("q")
        if not query:
            query = ""
        object_list = Departament.objects.filter(Q(name__icontains=query))
        return object_list


class DepartamentDetailView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DataMixin,
    generic.DetailView,  # type: ignore[type-arg]
):
    """_DepartamentDetailView_
    Detail of departament instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Departament): _base model for list_
    """

    permission_required = "employee.view_departament"
    model = Departament
    template_name = "employee/departament_detail.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, links to create, update and delete departament_
        """

        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Отдел",
            add="employee:new-departament",
            update="employee:departament-update",
            delete="employee:departament-delete",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class DepartamentCreate(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DataMixin,
    FormMessageMixin,
    CreateView,  # type: ignore[type-arg]
):
    """_DepartamentCreate_
    Create of departament instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Departament): _base model for list_
        form_class (DepartamentForm): _form class to view_
        success_message (str):
        error_message (str):
    """

    permission_required = "employee.add_departament"
    model = Departament
    form_class = DepartamentForm
    template_name = "Forms/add.html"
    success_url = reverse_lazy("employee:departament_list")
    success_message = "Отдел %(name)s успешно создана"
    error_message = "Отдел %(name)s не удалось создать"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title_
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Добавить отдел",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class DepartamentUpdate(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DataMixin,
    FormMessageMixin,
    UpdateView,  # type: ignore[type-arg]
):
    """_DepartamentUpdate_
    Update of departament instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        model (Departament): _base model for list_
        form_class (DepartamentForm): _form class to view_
        success_message (str):
        error_message (str):
    """

    permission_required = "employee.change_departament"
    model = Departament
    template_name = "Forms/add.html"
    form_class = DepartamentForm
    success_url = reverse_lazy("employee:departament_list")
    success_message = "Отдел %(name)s успешно обновлен"
    error_message = "Отдел %(name)s не удалось обновить"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title_
        """

        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Редактировать отдел",
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class DepartamentDelete(  # type: ignore[misc]
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DataMixin,
    FormMessageMixin,
    DeleteView,  # type: ignore[type-arg]
):
    """_DepartamentDelete_
    Delete of departament instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        success_url (str): _switches to url in case of successful deletion_
        model (Departament): _base model for list_
        success_message (str):
        error_message (str):
    """

    permission_required = "employee.delete_departament"
    model = Departament
    template_name = "Forms/delete.html"
    success_url = reverse_lazy("employee:departament_list")
    success_message = "Отдел успешно удален"
    error_message = "Отдел не удалось удалить"

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to departament list_
        """

        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Удалить отдел", selflink="employee:departament_list"
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context
