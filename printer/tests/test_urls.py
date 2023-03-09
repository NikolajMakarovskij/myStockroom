import pytest, warnings
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse
from ..models import Categories, Printer

#list and create
@pytest.mark.django_db
def test_list_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   links = ['/printer/','/printer/search']
   for link in links:
      url = (link)
      response = client.get(url)
      assert response.status_code == 200

@pytest.mark.django_db
def test_list_uses_correct_url_nad_template(client):
   warnings.filterwarnings(action="ignore")
   links = [
      {'link': 'printer:printer_list','template': 'printer/printer_list.html'},
      {'link': 'printer:printer_search','template': 'printer/printer_list.html'},
      {'link': 'printer:new-printer','template': 'Forms/add.html'},
   ]
   for each in links:
      url = reverse(each.get('link'))
      response = client.get(url)
      assert response.status_code == 200
      assertTemplateUsed(response, each.get('template'))

#detail_update_delete
@pytest.mark.django_db
def test_details_url(client):
   warnings.filterwarnings(action="ignore")
   links = [
      {'model': Printer,'link': 'printer:printer-detail', 'template': 'printer/printer_detail.html'},
      {'model': Printer,'link': 'printer:printer-update', 'template': 'Forms/add.html'},
      {'model': Printer,'link': 'printer:printer-delete', 'template': 'Forms/delete.html'},
   ]
   for each in links:
      model = each.get('model').objects.create(name="some_model")
      url = reverse(each.get('link'), kwargs={"pk": model.pk})
      response = client.get(url)
      assert response.status_code == 200
      assertTemplateUsed(response, each.get('template'))

#category
@pytest.mark.django_db
def test_printer_category_url(client):
   warnings.filterwarnings(action="ignore")
   Categories.objects.create(name="some_category",slug="some_category")
   url = reverse('printer:category', kwargs={"category_slug": Categories.objects.get(slug="some_category")})
   response = client.get(url)
   assert response.status_code == 200
   assertTemplateUsed(response, 'printer/printer_list.html')
