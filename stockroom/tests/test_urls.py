import pytest
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse
from ..models import Stock_cat


#list and create
@pytest.mark.django_db
def test_list_url_exists_at_desired_location(client):
   links = [
      '/stockroom/',
      '/stockroom/search',
      '/stockroom/history',
      '/stockroom/history/search'
      ]
   for link in links:
      url = (link)
      response = client.get(url)
      assert response.status_code == 200

@pytest.mark.django_db
def test_list_uses_correct_url_nad_template(client):
   links = [
      {'link': 'stockroom:stock_list','template': 'stock/stock_list.html'},
      {'link': 'stockroom:stock_search','template': 'stock/stock_list.html'},
      {'link': 'stockroom:history_list','template': 'stock/history_list.html'},
      {'link': 'stockroom:history_search','template': 'stock/history_list.html'},
   ]
   for each in links:
      url = reverse(each.get('link'))
      response = client.get(url)
      assert response.status_code == 200
      assertTemplateUsed(response, each.get('template'))

#category
@pytest.mark.django_db
def test_stockroom_category_url(client):
   links = [
      {'link': 'stockroom:category','template': 'stock/stock_list.html'},
      {'link': 'stockroom:history_category','template': 'stock/history_list.html'},
   ]
   Stock_cat.objects.create(name="some_category",slug="some_category")
   for each in links:
      url = reverse(each.get('link'), kwargs={"category_slug": Stock_cat.objects.get(slug="some_category")})
      response = client.get(url)
      assert response.status_code == 200
      assertTemplateUsed(response, each.get('template'))

   

