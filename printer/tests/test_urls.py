import pytest, warnings
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse
from ..models import Categories, Printer

#list
@pytest.mark.django_db
def test_printer_list_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_printer_list_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('printer:printer_list')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_printer_list_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('printer:printer_list')
   response = client.get(url)
   assertTemplateUsed(response, 'printer/printer_list.html')

#search
@pytest.mark.django_db
def test_printer_search_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('/printer/search')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_printer_search_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('printer:printer_search')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_printer_search_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('printer:printer_search')
   response = client.get(url)
   assertTemplateUsed(response, 'printer/printer_list.html')

#category
@pytest.mark.django_db
def test_printer_category_url(client):
   warnings.filterwarnings(action="ignore")
   Categories.objects.create(name="some_category",slug="some_category")
   url = reverse('printer:category', kwargs={"category_slug": Categories.objects.get(slug="some_category")})
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_printer_category_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   Categories.objects.create(name="some_category",slug="some_category")
   url = reverse('printer:category', kwargs={"category_slug": Categories.objects.get(slug="some_category")})
   response = client.get(url)
   assertTemplateUsed(response, 'printer/printer_list.html')

#detail
@pytest.mark.django_db
def test_printer_detail_url(client):
   warnings.filterwarnings(action="ignore")
   Printer.objects.create(
      name="some_printer",
   )
   printer = Printer.objects.get(name="some_printer")
   url = reverse('printer:printer-detail', kwargs={"pk": printer.pk})
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_printer_detail_uses_correct_template(client):
    warnings.filterwarnings(action="ignore")
    Printer.objects.create(
        name="some_printer",
    )
    printer = Printer.objects.get(name="some_printer")
    url = reverse('printer:printer-detail', kwargs={"pk": printer.pk})
    response = client.get(url)
    assertTemplateUsed(response, 'printer/printer_detail.html')

#create
@pytest.mark.django_db
def test_printer_create_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('printer:new-printer')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_printer_create_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('printer:new-printer')
   response = client.get(url)
   assertTemplateUsed(response, 'Forms/add.html')

#update
@pytest.mark.django_db
def test_printer_update_url(client):
   warnings.filterwarnings(action="ignore")
   Printer.objects.create(
      name="some_printer",
   )
   printer = Printer.objects.get(name="some_printer")
   url = reverse('printer:printer-update', kwargs={"pk": printer.pk})
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_printer_update_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   Printer.objects.create(
      name="some_printer",
   )
   printer = Printer.objects.get(name="some_printer")
   url = reverse('printer:printer-update', kwargs={"pk": printer.pk})
   response = client.get(url)
   assertTemplateUsed(response, "Forms/add.html")

#delete
@pytest.mark.django_db
def test_printer_delete_url(client):
   warnings.filterwarnings(action="ignore")
   Printer.objects.create(
      name="some_printer",
   )
   printer = Printer.objects.get(name="some_printer")
   url = reverse('printer:printer-delete', kwargs={"pk": printer.pk})
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_printer_delete_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   Printer.objects.create(
      name="some_printer",
   )
   printer = Printer.objects.get(name="some_printer")
   url = reverse('printer:printer-delete', kwargs={"pk": printer.pk})
   response = client.get(url)
   assertTemplateUsed(response, 'Forms/delete.html')