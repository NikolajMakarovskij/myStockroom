import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from core.tests.test_login import auto_login_user  # noqa F401

from ..models import Departament, Employee, Post


# list and create
@pytest.mark.django_db
def test_list_url_exists_at_desired_location(auto_login_user): # noqa F811
    client, user = auto_login_user()
    links = ['/employee/', '/employee/employee/', '/employee/employee/search', '/employee/post/',
             '/employee/post/search', '/employee/departament/', '/employee/departament/search']
    for link in links:
        url = link
        response = client.get(url)
        assert response.status_code == 200


@pytest.mark.django_db
def test_list_uses_correct_url_nad_template(auto_login_user): # noqa F811
    client, user = auto_login_user()
    links = [
        {'link': 'employee:employee_index', 'template': 'employee/employee_index.html'},
        {'link': 'employee:employee_list', 'template': 'employee/employee_list.html'},
        {'link': 'employee:employee_search', 'template': 'employee/employee_list.html'},
        {'link': 'employee:new-employee', 'template': 'Forms/add.html'},
        {'link': 'employee:post_list', 'template': 'employee/post_list.html'},
        {'link': 'employee:post_search', 'template': 'employee/post_list.html'},
        {'link': 'employee:new-post', 'template': 'Forms/add.html'},
        {'link': 'employee:departament_list', 'template': 'employee/departament_list.html'},
        {'link': 'employee:departament_search', 'template': 'employee/departament_list.html'},
        {'link': 'employee:new-departament', 'template': 'Forms/add.html'},
    ]
    for each in links:
        url = reverse(each.get('link'))
        response = client.get(url)
        assert response.status_code == 200
        assertTemplateUsed(response, each.get('template'))


# detail_update_delete
@pytest.mark.django_db
def test_details_url(auto_login_user): # noqa F811
    client, user = auto_login_user()
    links = [
        {'model': Employee, 'link': 'employee:employee-detail', 'template': 'employee/employee_detail.html'},
        {'model': Employee, 'link': 'employee:employee-update', 'template': 'Forms/add.html'},
        {'model': Employee, 'link': 'employee:employee-delete', 'template': 'Forms/delete.html'},
        {'model': Post, 'link': 'employee:post-detail', 'template': 'employee/post_detail.html'},
        {'model': Post, 'link': 'employee:post-update', 'template': 'Forms/add.html'},
        {'model': Post, 'link': 'employee:post-delete', 'template': 'Forms/delete.html'},
        {'model': Departament, 'link': 'employee:departament-detail', 'template': 'employee/departament_detail.html'},
        {'model': Departament, 'link': 'employee:departament-update', 'template': 'Forms/add.html'},
        {'model': Departament, 'link': 'employee:departament-delete', 'template': 'Forms/delete.html'},
    ]
    for each in links:
        model = each.get('model').objects.create(name="some_model")
        url = reverse(each.get('link'), kwargs={"pk": model.pk})
        response = client.get(url)
        assert response.status_code == 200
        assertTemplateUsed(response, each.get('template'))
