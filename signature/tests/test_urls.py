import pytest, warnings
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse
from ..models import Signature

#list
@pytest.mark.django_db
def test_signature_list_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_signature_list_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('signature:signature_list')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_signature_list_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('signature:signature_list')
   response = client.get(url)
   assertTemplateUsed(response, 'signature/signature_list.html')

#search
@pytest.mark.django_db
def test_signature_search_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   url = ('/signature/search')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_signature_search_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('signature:signature_search')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_signature_search_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('signature:signature_search')
   response = client.get(url)
   assertTemplateUsed(response, 'signature/signature_list.html')

#detail
@pytest.mark.django_db
def test_signature_detail_url(client):
   warnings.filterwarnings(action="ignore")
   Signature.objects.create(
      name="some_signature",
   )
   sig = Signature.objects.get(name="some_signature")
   url = reverse('signature:signature-detail', kwargs={"pk": sig.pk})
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_signature_detail_uses_correct_template(client):
    warnings.filterwarnings(action="ignore")
    Signature.objects.create(
      name="some_signature",
    )
    sig = Signature.objects.get(name="some_signature")
    url = reverse('signature:signature-detail', kwargs={"pk": sig.pk})
    response = client.get(url)
    assertTemplateUsed(response, 'signature/signature_detail.html')

#create
@pytest.mark.django_db
def test_signature_create_url(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('signature:new-signature')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_signature_create_uses_correct_template(client):
   warnings.filterwarnings(action="ignore")
   url = reverse('signature:new-signature')
   response = client.get(url)
   assertTemplateUsed(response, 'Forms/add.html')

#update
@pytest.mark.django_db
def test_signature_update_url(client):
    warnings.filterwarnings(action="ignore")
    Signature.objects.create(
      name="some_signature",
    )
    sig = Signature.objects.get(name="some_signature")
    url = reverse('signature:signature-update', kwargs={"pk": sig.pk})
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_signature_update_uses_correct_template(client):
    warnings.filterwarnings(action="ignore")
    Signature.objects.create(
      name="some_signature",
    )
    sig = Signature.objects.get(name="some_signature")
    url = reverse('signature:signature-update', kwargs={"pk": sig.pk})
    response = client.get(url)
    assertTemplateUsed(response, "Forms/add.html")

#delete
@pytest.mark.django_db
def test_signature_delete_url(client):
    warnings.filterwarnings(action="ignore")
    Signature.objects.create(
      name="some_signature",
    )
    sig = Signature.objects.get(name="some_signature")
    url = reverse('signature:signature-delete', kwargs={"pk": sig.pk})
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_manufacturer_delete_uses_correct_template(client):
    warnings.filterwarnings(action="ignore")
    Signature.objects.create(
      name="some_signature",
    )
    sig = Signature.objects.get(name="some_signature")
    url = reverse('signature:signature-delete', kwargs={"pk": sig.pk})
    response = client.get(url)
    assertTemplateUsed(response, 'Forms/delete.html')