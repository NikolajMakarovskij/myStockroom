import pytest, warnings
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse
from ..models import Ups, Cassette

#ups_list
@pytest.mark.django_db
def test_ups_list_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_ups_list_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('ups:ups_list')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_ups_list_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('ups:ups_list')
   response = client.get(url)
   assertTemplateUsed(response, 'ups/ups_list.html')

#ups_search
@pytest.mark.django_db
def test_ups_search_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('/ups/search')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_ups_search_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('ups:ups_search')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_ups_search_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('ups:ups_search')
   response = client.get(url)
   assertTemplateUsed(response, 'ups/ups_list.html')

#ups_detail
@pytest.mark.django_db
def test_ups_detail_url(client):
   warnings.filterwarnings(action="ignore")
   Ups.objects.create(
      name="some_ups",
   )
   ups = Ups.objects.get(name="some_ups")
   url = reverse('ups:ups-detail', kwargs={"pk": ups.pk})
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_ups_detail_uses_correct_template(client):
    warnings.filterwarnings(action="ignore")
    Ups.objects.create(
      name="some_ups",
    )
    ups = Ups.objects.get(name="some_ups")
    url = reverse('ups:ups-detail', kwargs={"pk": ups.pk})
    response = client.get(url)
    assertTemplateUsed(response, 'ups/ups_detail.html')

#ups_create
@pytest.mark.django_db
def test_ups_create_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('ups:new-ups')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_ups_create_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('ups:new-ups')
   response = client.get(url)
   assertTemplateUsed(response, 'Forms/add.html')

#ups_update
@pytest.mark.django_db
def test_ups_update_url(client):
    warnings.filterwarnings(action="ignore")
    Ups.objects.create(
      name="some_ups",
    )
    ups = Ups.objects.get(name="some_ups")
    url = reverse('ups:ups-update', kwargs={"pk": ups.pk})
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_ups_update_uses_correct_template(client):
    warnings.filterwarnings(action="ignore")
    Ups.objects.create(
      name="some_ups",
    )
    ups = Ups.objects.get(name="some_ups")
    url = reverse('ups:ups-update', kwargs={"pk": ups.pk})
    response = client.get(url)
    assertTemplateUsed(response, "Forms/add.html")

#ups_delete
@pytest.mark.django_db
def test_ups_delete_url(client):
    warnings.filterwarnings(action="ignore")
    Ups.objects.create(
      name="some_ups",
    )
    ups = Ups.objects.get(name="some_ups")
    url = reverse('ups:ups-delete', kwargs={"pk": ups.pk})
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_ups_delete_uses_correct_template(client):
    warnings.filterwarnings(action="ignore")
    Ups.objects.create(
      name="some_ups",
    )
    ups = Ups.objects.get(name="some_ups")
    url = reverse('ups:ups-delete', kwargs={"pk": ups.pk})
    response = client.get(url)
    assertTemplateUsed(response, 'Forms/delete.html')

#cassette_list
@pytest.mark.django_db
def test_cassette_list_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('/ups/cassette/')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_cassette_list_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('ups:cassette_list')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_cassette_list_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('ups:cassette_list')
   response = client.get(url)
   assertTemplateUsed(response, 'ups/cassette_list.html')

#cassette_search
@pytest.mark.django_db
def test_cassette_search_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('/ups/cassette/search')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_cassette_search_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('ups:cassette_search')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_cassette_search_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('ups:cassette_search')
   response = client.get(url)
   assertTemplateUsed(response, 'ups/cassette_list.html')

#cassette_detail
@pytest.mark.django_db
def test_cassette_detail_url(client):
   warnings.filterwarnings(action="ignore")
   Cassette.objects.create(
      name="some_ups",
   )
   ups = Cassette.objects.get(name="some_ups")
   url = reverse('ups:cassette-detail', kwargs={"pk": ups.pk})
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_cassette_detail_uses_correct_template(client):
    warnings.filterwarnings(action="ignore")
    Cassette.objects.create(
      name="some_ups",
    )
    ups = Cassette.objects.get(name="some_ups")
    url = reverse('ups:cassette-detail', kwargs={"pk": ups.pk})
    response = client.get(url)
    assertTemplateUsed(response, 'ups/cassette_detail.html')

#cassette_create
@pytest.mark.django_db
def test_cassette_create_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('ups:new-cassette')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_cassette_create_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('ups:new-cassette')
   response = client.get(url)
   assertTemplateUsed(response, 'Forms/add.html')

#cassette_update
@pytest.mark.django_db
def test_cassette_update_url(client):
    warnings.filterwarnings(action="ignore")
    Cassette.objects.create(
      name="some_ups",
    )
    ups = Cassette.objects.get(name="some_ups")
    url = reverse('ups:cassette-update', kwargs={"pk": ups.pk})
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_cassette_update_uses_correct_template(client):
    warnings.filterwarnings(action="ignore")
    Cassette.objects.create(
      name="some_ups",
    )
    ups = Cassette.objects.get(name="some_ups")
    url = reverse('ups:cassette-update', kwargs={"pk": ups.pk})
    response = client.get(url)
    assertTemplateUsed(response, "Forms/add.html")

#cassette_delete
@pytest.mark.django_db
def test_cassette_delete_url(client):
    warnings.filterwarnings(action="ignore")
    Cassette.objects.create(
      name="some_ups",
    )
    ups = Cassette.objects.get(name="some_ups")
    url = reverse('ups:cassette-delete', kwargs={"pk": ups.pk})
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_cassette_delete_uses_correct_template(client):
    warnings.filterwarnings(action="ignore")
    Cassette.objects.create(
      name="some_ups",
    )
    ups = Cassette.objects.get(name="some_ups")
    url = reverse('ups:cassette-delete', kwargs={"pk": ups.pk})
    response = client.get(url)
    assertTemplateUsed(response, 'Forms/delete.html')

