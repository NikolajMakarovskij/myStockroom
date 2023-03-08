import pytest, warnings
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse

#index
@pytest.mark.django_db
def test_index_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_index_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('catalog:index')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_index_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('catalog:index')
   response = client.get(url)
   assertTemplateUsed(response, 'index.html')

#ref_list
@pytest.mark.django_db
def test_references_list_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('/references/')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_references_list_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('catalog:references_list')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_references_list_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('catalog:references_list')
   response = client.get(url)
   assertTemplateUsed(response, 'catalog/references.html')

#ref_search
@pytest.mark.django_db
def test_references_search_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('/references/search')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_references_search_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('catalog:references_search')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_references_search_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('catalog:references_search')
   response = client.get(url)
   assertTemplateUsed(response, 'catalog/references.html')