import pytest, warnings
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse
from ..models import Manufacturer

#counterparty
@pytest.mark.django_db
def test_counterparty_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_counterparty_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('counterparty:counterparty')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_counterparty_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('counterparty:counterparty')
   response = client.get(url)
   assertTemplateUsed(response, 'counterparty/counterparty.html')

#list
@pytest.mark.django_db
def test_manufacturer_list_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('/counterparty/manufacturer/')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_manufacturer_list_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('counterparty:manufacturer_list')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_manufacturer_list_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('counterparty:manufacturer_list')
   response = client.get(url)
   assertTemplateUsed(response, 'counterparty/manufacturer_list.html')

#search
@pytest.mark.django_db
def test_manufacturer_search_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('/consumables/search')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_manufacturer_search_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('counterparty:manufacturer_search')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_manufacturer_search_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('counterparty:manufacturer_search')
   response = client.get(url)
   assertTemplateUsed(response, 'counterparty/manufacturer_list.html')

#detail
@pytest.mark.django_db
def test_manufacturer_detail_url(client):
   warnings.filterwarnings(action="ignore")
   Manufacturer.objects.create(
      name="some_manufacturer",
   )
   man = Manufacturer.objects.get(name="some_manufacturer")
   url = reverse('counterparty:manufacturer-detail', kwargs={"pk": man.pk})
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_manufacturer_detail_uses_correct_template(client):
    warnings.filterwarnings(action="ignore")
    Manufacturer.objects.create(
      name="some_manufacturer",
    )
    man = Manufacturer.objects.get(name="some_manufacturer")
    url = reverse('counterparty:manufacturer-detail', kwargs={"pk": man.pk})
    response = client.get(url)
    assertTemplateUsed(response, 'counterparty/manufacturer_detail.html')

#create
@pytest.mark.django_db
def test_manufacturer_create_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('counterparty:new-manufacturer')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_manufacturer_create_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('counterparty:new-manufacturer')
   response = client.get(url)
   assertTemplateUsed(response, 'Forms/add.html')

#update
@pytest.mark.django_db
def test_manufacturer_update_url(client):
    warnings.filterwarnings(action="ignore")
    Manufacturer.objects.create(
      name="some_manufacturer",
    )
    man = Manufacturer.objects.get(name="some_manufacturer")
    url = reverse('counterparty:manufacturer-update', kwargs={"pk": man.pk})
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_manufacturer_update_uses_correct_template(client):
    warnings.filterwarnings(action="ignore")
    Manufacturer.objects.create(
      name="some_manufacturer",
    )
    man = Manufacturer.objects.get(name="some_manufacturer")
    url = reverse('counterparty:manufacturer-update', kwargs={"pk": man.pk})
    response = client.get(url)
    assertTemplateUsed(response, "Forms/add.html")

#delete
@pytest.mark.django_db
def test_manufacturer_delete_url(client):
    warnings.filterwarnings(action="ignore")
    Manufacturer.objects.create(
      name="some_manufacturer",
    )
    man = Manufacturer.objects.get(name="some_manufacturer")
    url = reverse('counterparty:manufacturer-delete', kwargs={"pk": man.pk})
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_manufacturer_delete_uses_correct_template(client):
    warnings.filterwarnings(action="ignore")
    Manufacturer.objects.create(
      name="some_manufacturer",
    )
    man = Manufacturer.objects.get(name="some_manufacturer")
    url = reverse('counterparty:manufacturer-delete', kwargs={"pk": man.pk})
    response = client.get(url)
    assertTemplateUsed(response, 'Forms/delete.html')