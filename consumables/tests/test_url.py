import pytest, warnings
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse
from ..models import Categories, Consumables

#list
@pytest.mark.django_db
def test_consumable_list_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_consumable_list_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('consumables:consumables_list')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_consumable_list_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('consumables:consumables_list')
   response = client.get(url)
   assertTemplateUsed(response, 'consumables/consumables_list.html')

#search
@pytest.mark.django_db
def test_consumable_search_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('/consumables/search')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_consumable_search_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('consumables:consumables_search')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_consumable_search_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('consumables:consumables_search')
   response = client.get(url)
   assertTemplateUsed(response, 'consumables/consumables_list.html')

#category
@pytest.mark.django_db
def test_consumable_category_url(client):
   warnings.filterwarnings(action="ignore")
   Categories.objects.create(name="some_category",slug="some_category")
   url = reverse('consumables:category', kwargs={"category_slug": Categories.objects.get(slug="some_category")})
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_consumable_category_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   Categories.objects.create(name="some_category",slug="some_category")
   url = reverse('consumables:category', kwargs={"category_slug": Categories.objects.get(slug="some_category")})
   response = client.get(url)
   assertTemplateUsed(response, 'consumables/consumables_list.html')

#detail
@pytest.mark.django_db
def test_consumable_detail_url(client):
   warnings.filterwarnings(action="ignore")
   Consumables.objects.create(
      name="some_consumable",
   )
   con = Consumables.objects.get(name="some_consumable")
   url = reverse('consumables:consumables-detail', kwargs={"pk": con.pk})
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_consumable_detail_uses_correct_template(client):
    warnings.filterwarnings(action="ignore")
    Consumables.objects.create(
        name="some_consumable",
    )
    con = Consumables.objects.get(name="some_consumable")
    url = reverse('consumables:consumables-detail', kwargs={"pk": con.pk})
    response = client.get(url)
    assertTemplateUsed(response, 'consumables/consumables_detail.html')

#create
@pytest.mark.django_db
def test_consumable_create_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('consumables:new-consumables')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_consumable_create_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('consumables:new-consumables')
   response = client.get(url)
   assertTemplateUsed(response, 'Forms/add.html')

#update
@pytest.mark.django_db
def test_consumable_update_url(client):
   warnings.filterwarnings(action="ignore")
   Consumables.objects.create(
      name="some_consumable",
   )
   con = Consumables.objects.get(name="some_consumable")
   url = reverse('consumables:consumables-update', kwargs={"pk": con.pk})
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_consumable_update_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   Consumables.objects.create(
      name="some_consumable",
   )
   con = Consumables.objects.get(name="some_consumable")
   url = reverse('consumables:consumables-update', kwargs={"pk": con.pk})
   response = client.get(url)
   assertTemplateUsed(response, "Forms/add.html")

#delete
@pytest.mark.django_db
def test_consumable_delete_url(client):
   warnings.filterwarnings(action="ignore")
   Consumables.objects.create(
      name="some_consumable",
   )
   con = Consumables.objects.get(name="some_consumable")
   url = reverse('consumables:consumables-delete', kwargs={"pk": con.pk})
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_consumable_delete_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   Consumables.objects.create(
      name="some_consumable",
   )
   con = Consumables.objects.get(name="some_consumable")
   url = reverse('consumables:consumables-delete', kwargs={"pk": con.pk})
   response = client.get(url)
   assertTemplateUsed(response, 'Forms/delete.html')