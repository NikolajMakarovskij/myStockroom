import pytest, warnings
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse
from ..models import Employee, Post, Departament

#employee_list
@pytest.mark.django_db
def test_employee_list_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_employee_list_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('employee:employee_list')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_employee_list_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('employee:employee_list')
   response = client.get(url)
   assertTemplateUsed(response, 'employee/employee_list.html')

#employee_search
@pytest.mark.django_db
def test_employee_search_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('/employee/search')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_employee_search_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('employee:employee_search')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_employee_search_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('employee:employee_search')
   response = client.get(url)
   assertTemplateUsed(response, 'employee/employee_list.html')

#employee_detail
@pytest.mark.django_db
def test_employee_detail_url(client):
   warnings.filterwarnings(action="ignore")
   Employee.objects.create(
      name="some_employee",
   )
   em = Employee.objects.get(name="some_employee")
   url = reverse('employee:employee-detail', kwargs={"pk": em.pk})
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_employee_detail_uses_correct_template(client):
    warnings.filterwarnings(action="ignore")
    Employee.objects.create(
        name="some_employee",
    )
    em = Employee.objects.get(name="some_employee")
    url = reverse('employee:employee-detail', kwargs={"pk": em.pk})
    response = client.get(url)
    assertTemplateUsed(response, 'employee/employee_detail.html')

#employee_create
@pytest.mark.django_db
def test_employee_create_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('employee:new-employee')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_employee_create_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('employee:new-employee')
   response = client.get(url)
   assertTemplateUsed(response, 'Forms/add.html')

#employee_update
@pytest.mark.django_db
def test_employee_update_url(client):
   warnings.filterwarnings(action="ignore")
   Employee.objects.create(
      name="some_employee",
   )
   em = Employee.objects.get(name="some_employee")
   url = reverse('employee:employee-update', kwargs={"pk": em.pk})
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_employee_update_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   Employee.objects.create(
      name="some_employee",
   )
   em = Employee.objects.get(name="some_employee")
   url = reverse('employee:employee-update', kwargs={"pk": em.pk})
   response = client.get(url)
   assertTemplateUsed(response, "Forms/add.html")

#employee_delete
@pytest.mark.django_db
def test_employee_delete_url(client):
   warnings.filterwarnings(action="ignore")
   Employee.objects.create(
      name="some_employee",
   )
   em = Employee.objects.get(name="some_employee")
   url = reverse('employee:employee-delete', kwargs={"pk": em.pk})
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_employee_delete_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   Employee.objects.create(
      name="some_employee",
   )
   em = Employee.objects.get(name="some_employee")
   url = reverse('employee:employee-delete', kwargs={"pk": em.pk})
   response = client.get(url)
   assertTemplateUsed(response, 'Forms/delete.html')

#post_list
@pytest.mark.django_db
def test_post_list_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('/employee/post/')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_post_list_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('employee:post_list')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_post_list_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('employee:post_list')
   response = client.get(url)
   assertTemplateUsed(response, 'employee/post_list.html')

#post_search
@pytest.mark.django_db
def test_post_search_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('/employee/post/search')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_post_search_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('employee:post_search')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_post_search_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('employee:post_search')
   response = client.get(url)
   assertTemplateUsed(response, 'employee/post_list.html')

#post_detail
@pytest.mark.django_db
def test_post_detail_url(client):
   warnings.filterwarnings(action="ignore")
   Post.objects.create(
      name="some_post",
   )
   post = Post.objects.get(name="some_post")
   url = reverse('employee:post-detail', kwargs={"pk": post.pk})
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_post_detail_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   Post.objects.create(
      name="some_post",
   )
   post = Post.objects.get(name="some_post")
   url = reverse('employee:post-detail', kwargs={"pk": post.pk})
   response = client.get(url)
   assertTemplateUsed(response, 'employee/post_detail.html')

#post_create
@pytest.mark.django_db
def test_post_create_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('employee:new-post')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_post_create_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('employee:new-post')
   response = client.get(url)
   assertTemplateUsed(response, 'Forms/add.html')

#post_update
@pytest.mark.django_db
def test_post_update_url(client):
   warnings.filterwarnings(action="ignore")
   Post.objects.create(
      name="some_post",
   )
   post = Post.objects.get(name="some_post")
   url = reverse('employee:post-update', kwargs={"pk": post.pk})
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_post_update_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   Post.objects.create(
      name="some_post",
   )
   post = Post.objects.get(name="some_post")
   url = reverse('employee:post-update', kwargs={"pk": post.pk})
   response = client.get(url)
   assertTemplateUsed(response, "Forms/add.html")

#post_delete
@pytest.mark.django_db
def test_post_delete_url(client):
   warnings.filterwarnings(action="ignore")
   Post.objects.create(
      name="some_post",
   )
   post = Post.objects.get(name="some_post")
   url = reverse('employee:post-delete', kwargs={"pk": post.pk})
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_post_delete_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   Post.objects.create(
      name="some_post",
   )
   post = Post.objects.get(name="some_post")
   url = reverse('employee:post-delete', kwargs={"pk": post.pk})
   response = client.get(url)
   assertTemplateUsed(response, 'Forms/delete.html')

#departament_list
@pytest.mark.django_db
def test_departament_list_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('/employee/departament/')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_departament_list_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('employee:departament_list')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_departament_list_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('employee:departament_list')
   response = client.get(url)
   assertTemplateUsed(response, 'employee/departament_list.html')

#departament_search
@pytest.mark.django_db
def test_departament_search_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('/employee/departament/search')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_departament_search_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('employee:departament_search')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_departament_search_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('employee:departament_search')
   response = client.get(url)
   assertTemplateUsed(response, 'employee/departament_list.html')

#departament_detail
@pytest.mark.django_db
def test_departament_detail_url(client):
   warnings.filterwarnings(action="ignore")
   Departament.objects.create(
      name="some_departament",
   )
   dep = Departament.objects.get(name="some_departament")
   url = reverse('employee:departament-detail', kwargs={"pk": dep.pk})
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_departament_detail_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   Departament.objects.create(
      name="some_departament",
   )
   dep = Departament.objects.get(name="some_departament")
   url = reverse('employee:departament-detail', kwargs={"pk": dep.pk})
   response = client.get(url)
   assertTemplateUsed(response, 'employee/departament_detail.html')

#departament_create
@pytest.mark.django_db
def test_departament_create_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('employee:new-departament')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_departament_create_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('employee:new-departament')
   response = client.get(url)
   assertTemplateUsed(response, 'Forms/add.html')

#departament_update
@pytest.mark.django_db
def test_departament_update_url(client):
   warnings.filterwarnings(action="ignore")
   Departament.objects.create(
      name="some_departament",
   )
   dep = Departament.objects.get(name="some_departament")
   url = reverse('employee:departament-update', kwargs={"pk": dep.pk})
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_departament_update_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   Departament.objects.create(
      name="some_departament",
   )
   dep = Departament.objects.get(name="some_departament")
   url = reverse('employee:departament-update', kwargs={"pk": dep.pk})
   response = client.get(url)
   assertTemplateUsed(response, "Forms/add.html")

#departament_delete
@pytest.mark.django_db
def test_departament_delete_url(client):
   warnings.filterwarnings(action="ignore")
   Departament.objects.create(
      name="some_departament",
   )
   dep = Departament.objects.get(name="some_departament")
   url = reverse('employee:departament-delete', kwargs={"pk": dep.pk})
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_departament_delete_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   Departament.objects.create(
      name="some_departament",
   )
   dep = Departament.objects.get(name="some_departament")
   url = reverse('employee:departament-delete', kwargs={"pk": dep.pk})
   response = client.get(url)
   assertTemplateUsed(response, 'Forms/delete.html')