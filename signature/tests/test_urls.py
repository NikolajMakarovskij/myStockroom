import pytest, warnings
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse
from ..models import Signature

#list and create
@pytest.mark.django_db
def test_list_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   links = ['/signature/','/signature/search']
   for link in links:
      url = (link)
      response = client.get(url)
      assert response.status_code == 200

@pytest.mark.django_db
def test_list_uses_correct_url_nad_template(client):
   warnings.filterwarnings(action="ignore")
   links = [
      {'link': 'signature:signature_list','template': 'signature/signature_list.html'},
      {'link': 'signature:signature_search','template': 'signature/signature_list.html'},
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
      {'model': Signature,'link': 'signature:signature-detail', 'template': 'signature/signature_detail.html'},
      {'model': Signature,'link': 'signature:signature-update', 'template': 'Forms/add.html'},
      {'model': Signature,'link': 'signature:signature-delete', 'template': 'Forms/delete.html'},
   ]
   for each in links:
      model = each.get('model').objects.create(name="some_model")
      url = reverse(each.get('link'), kwargs={"pk": model.pk})
      response = client.get(url)
      assert response.status_code == 200
      assertTemplateUsed(response, each.get('template'))