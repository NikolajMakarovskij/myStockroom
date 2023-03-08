import pytest, warnings
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse
from ..models import Categories, Stockroom, Consumables

#list
@pytest.mark.django_db
def test_stockroom_list_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_stockroom_list_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('stockroom:stock_list')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_stockroom_list_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('stockroom:stock_list')
   response = client.get(url)
   assertTemplateUsed(response, 'stock/stock_list.html')

#search
@pytest.mark.django_db
def test_stockroom_search_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('/stockroom/search')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_stockroom_search_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('stockroom:stock_search')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_stockroom_search_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('stockroom:stock_search')
   response = client.get(url)
   assertTemplateUsed(response, 'stock/stock_list.html')

#category
@pytest.mark.django_db
def test_stockroom_category_url(client):
   warnings.filterwarnings(action="ignore")
   Categories.objects.create(name="some_category",slug="some_category")
   url = reverse('stockroom:category', kwargs={"category_slug": Categories.objects.get(slug="some_category")})
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_stockroom_category_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   Categories.objects.create(name="some_category",slug="some_category")
   url = reverse('stockroom:category', kwargs={"category_slug": Categories.objects.get(slug="some_category")})
   response = client.get(url)
   assertTemplateUsed(response, 'stock/stock_list.html')

