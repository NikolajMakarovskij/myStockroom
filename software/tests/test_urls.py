import pytest, warnings
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse
from ..models import Software, Os

#software_list
@pytest.mark.django_db
def test_software_list_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_software_list_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('software:software_list')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_software_list_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('software:software_list')
   response = client.get(url)
   assertTemplateUsed(response, 'software/software_list.html')

#software_search
@pytest.mark.django_db
def test_software_search_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('/software/search')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_software_search_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('software:software_search')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_software_search_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('software:software_search')
   response = client.get(url)
   assertTemplateUsed(response, 'software/software_list.html')

#software_detail
@pytest.mark.django_db
def test_software_detail_url(client):
   warnings.filterwarnings(action="ignore")
   Software.objects.create(
      name="some_software",
   )
   soft = Software.objects.get(name="some_software")
   url = reverse('software:software-detail', kwargs={"pk": soft.pk})
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_software_detail_uses_correct_template(client):
    warnings.filterwarnings(action="ignore")
    Software.objects.create(
      name="some_software",
    )
    soft = Software.objects.get(name="some_software")
    url = reverse('software:software-detail', kwargs={"pk": soft.pk})
    response = client.get(url)
    assertTemplateUsed(response, 'software/software_detail.html')

#software_create
@pytest.mark.django_db
def test_software_create_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('software:new-software')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_software_create_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('software:new-software')
   response = client.get(url)
   assertTemplateUsed(response, 'Forms/add.html')

#software_update
@pytest.mark.django_db
def test_software_update_url(client):
    warnings.filterwarnings(action="ignore")
    Software.objects.create(
      name="some_software",
    )
    soft = Software.objects.get(name="some_software")
    url = reverse('software:software-update', kwargs={"pk": soft.pk})
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_software_update_uses_correct_template(client):
    warnings.filterwarnings(action="ignore")
    Software.objects.create(
      name="some_software",
    )
    soft = Software.objects.get(name="some_software")
    url = reverse('software:software-update', kwargs={"pk": soft.pk})
    response = client.get(url)
    assertTemplateUsed(response, "Forms/add.html")

#software_delete
@pytest.mark.django_db
def test_software_delete_url(client):
    warnings.filterwarnings(action="ignore")
    Software.objects.create(
      name="some_software",
    )
    soft = Software.objects.get(name="some_software")
    url = reverse('software:software-delete', kwargs={"pk": soft.pk})
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_software_delete_uses_correct_template(client):
    warnings.filterwarnings(action="ignore")
    Software.objects.create(
      name="some_software",
    )
    soft = Software.objects.get(name="some_software")
    url = reverse('software:software-delete', kwargs={"pk": soft.pk})
    response = client.get(url)
    assertTemplateUsed(response, 'Forms/delete.html')

#OS_list
@pytest.mark.django_db
def test_OS_list_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('/software/OS/')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_OS_list_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('software:OS_list')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_OS_list_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('software:OS_list')
   response = client.get(url)
   assertTemplateUsed(response, 'software/OS_list.html')

#software_search
@pytest.mark.django_db
def test_OS_search_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('/software/OS/search')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_OS_search_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('software:OS_search')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_OS_search_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('software:OS_search')
   response = client.get(url)
   assertTemplateUsed(response, 'software/OS_list.html')

#software_detail
@pytest.mark.django_db
def test_OS_detail_url(client):
   warnings.filterwarnings(action="ignore")
   Os.objects.create(
      name="some_OS",
   )
   OS = Os.objects.get(name="some_OS")
   url = reverse('software:OS-detail', kwargs={"pk": OS.pk})
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_OS_detail_uses_correct_template(client):
    warnings.filterwarnings(action="ignore")
    Os.objects.create(
      name="some_OS",
    )
    OS = Os.objects.get(name="some_OS")
    url = reverse('software:OS-detail', kwargs={"pk": OS.pk})
    response = client.get(url)
    assertTemplateUsed(response, 'software/OS_detail.html')

#software_create
@pytest.mark.django_db
def test_OS_create_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('software:new-OS')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_OS_create_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('software:new-OS')
   response = client.get(url)
   assertTemplateUsed(response, 'Forms/add.html')

#software_update
@pytest.mark.django_db
def test_OS_update_url(client):
    warnings.filterwarnings(action="ignore")
    Os.objects.create(
      name="some_OS",
    )
    OS = Os.objects.get(name="some_OS")
    url = reverse('software:OS-update', kwargs={"pk": OS.pk})
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_OS_update_uses_correct_template(client):
    warnings.filterwarnings(action="ignore")
    Os.objects.create(
      name="some_OS",
    )
    OS = Os.objects.get(name="some_OS")
    url = reverse('software:OS-update', kwargs={"pk": OS.pk})
    response = client.get(url)
    assertTemplateUsed(response, "Forms/add.html")

#software_delete
@pytest.mark.django_db
def test_OS_delete_url(client):
    warnings.filterwarnings(action="ignore")
    Os.objects.create(
      name="some_OS",
    )
    OS = Os.objects.get(name="some_OS")
    url = reverse('software:OS-delete', kwargs={"pk": OS.pk})
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_OS_delete_uses_correct_template(client):
    warnings.filterwarnings(action="ignore")
    Os.objects.create(
      name="some_OS",
    )
    OS = Os.objects.get(name="some_OS")
    url = reverse('software:OS-delete', kwargs={"pk": OS.pk})
    response = client.get(url)
    assertTemplateUsed(response, 'Forms/delete.html')