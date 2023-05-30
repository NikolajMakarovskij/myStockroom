import pytest, warnings
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse
from ..models import Ups, Cassette

#list and create
@pytest.mark.django_db
def test_list_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   links = ['/ups/','/ups/search','/ups/cassette/','/ups/cassette/search']
   for link in links:
      url = (link)
      response = client.get(url)
      assert response.status_code == 200

@pytest.mark.django_db
def test_list_uses_correct_url_nad_template(client):
   warnings.filterwarnings(action="ignore")
   links = [
      {'link': 'ups:ups_list','template': 'ups/ups_list.html'},
      {'link': 'ups:ups_search','template': 'ups/ups_list.html'},
      {'link': 'ups:new-ups','template': 'Forms/add.html'},
      {'link': 'ups:cassette_list','template': 'ups/cassette_list.html'},
      {'link': 'ups:cassette_search','template': 'ups/cassette_list.html'},
      {'link': 'ups:new-cassette','template': 'Forms/add.html'},
   ]
   for each in links:
      url = reverse(each.get('link'))
      response = client.get(url)
      assert response.status_code == 200
      assertTemplateUsed(response, each.get('template'))

#detail_update_delete
@pytest.mark.django_db
def test_ups_detail_url(client):
   warnings.filterwarnings(action="ignore")
   links = [
      {'model': Ups,'link': 'ups:ups-detail', 'template': 'ups/ups_detail.html'},
      {'model': Ups,'link': 'ups:ups-update', 'template': 'Forms/add.html'},
      {'model': Ups,'link': 'ups:ups-delete', 'template': 'Forms/delete.html'},
      {'model': Cassette,'link': 'ups:cassette-detail', 'template': 'ups/cassette_detail.html'},
      {'model': Cassette,'link': 'ups:cassette-update', 'template': 'Forms/add.html'},
      {'model': Cassette,'link': 'ups:cassette-delete', 'template': 'Forms/delete.html'},
   ]
   for each in links:
      model = each.get('model').objects.create(name="some_model")
      url = reverse(each.get('link'), kwargs={"pk": model.pk})
      response = client.get(url)
      assert response.status_code == 200
      assertTemplateUsed(response, each.get('template'))


