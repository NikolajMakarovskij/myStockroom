import pytest, warnings
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse
from ..models import Categories, Workstation, Monitor, Mouse, KeyBoard

#list and create
@pytest.mark.django_db
def test_list_url_exists_at_desired_location(client):
   warnings.filterwarnings(action="ignore")
   links = [
      '/workstation/','/workstation/search',
      '/workstation/monitor/','/workstation/monitor/search',
      '/workstation/keyBoard/','/workstation/keyBoard/search',
      '/workstation/mouse/','/workstation/mouse/search',
      ]
   for link in links:
      url = (link)
      response = client.get(url)
      assert response.status_code == 200

@pytest.mark.django_db
def test_list_uses_correct_url_nad_template(client):
   warnings.filterwarnings(action="ignore")
   links = [
      {'link': 'workstation:workstation_list','template': 'workstation/workstation_list.html'},
      {'link': 'workstation:workstation_search','template': 'workstation/workstation_list.html'},
      {'link': 'workstation:new-workstation','template': 'Forms/add.html'},
      {'link': 'workstation:monitor_list','template': 'workstation/monitor_list.html'},
      {'link': 'workstation:monitor_search','template': 'workstation/monitor_list.html'},
      {'link': 'workstation:new-monitor','template': 'Forms/add.html'},
      {'link': 'workstation:keyBoard_list','template': 'workstation/keyBoard_list.html'},
      {'link': 'workstation:keyBoard_search','template': 'workstation/keyBoard_list.html'},
      {'link': 'workstation:new-keyBoard','template': 'Forms/add.html'},
      {'link': 'workstation:mouse_list','template': 'workstation/mouse_list.html'},
      {'link': 'workstation:mouse_search','template': 'workstation/mouse_list.html'},
      {'link': 'workstation:new-mouse','template': 'Forms/add.html'},      
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
      {'model': Workstation,'link': 'workstation:workstation-detail', 'template': 'workstation/workstation_detail.html'},
      {'model': Workstation,'link': 'workstation:workstation-update', 'template': 'Forms/add.html'},
      {'model': Workstation,'link': 'workstation:workstation-delete', 'template': 'Forms/delete.html'},
      {'model': Monitor,'link': 'workstation:monitor-detail', 'template': 'workstation/monitor_detail.html'},
      {'model': Monitor,'link': 'workstation:monitor-update', 'template': 'Forms/add.html'},
      {'model': Monitor,'link': 'workstation:monitor-delete', 'template': 'Forms/delete.html'},
      {'model': KeyBoard,'link': 'workstation:keyBoard-detail', 'template': 'workstation/keyBoard_detail.html'},
      {'model': KeyBoard,'link': 'workstation:keyBoard-update', 'template': 'Forms/add.html'},
      {'model': KeyBoard,'link': 'workstation:keyBoard-delete', 'template': 'Forms/delete.html'},
      {'model': Mouse,'link': 'workstation:mouse-detail', 'template': 'workstation/mouse_detail.html'},
      {'model': Mouse,'link': 'workstation:mouse-update', 'template': 'Forms/add.html'},
      {'model': Mouse,'link': 'workstation:mouse-delete', 'template': 'Forms/delete.html'},
   ]
   for each in links:
      model = each.get('model').objects.create(name="some_model")
      url = reverse(each.get('link'), kwargs={"pk": model.pk})
      response = client.get(url)
      assert response.status_code == 200
      assertTemplateUsed(response, each.get('template'))

#category
@pytest.mark.django_db
def test_consumable_category_url(client):
   warnings.filterwarnings(action="ignore")
   Categories.objects.create(name="some_category",slug="some_category")
   url = reverse('consumables:category', kwargs={"category_slug": Categories.objects.get(slug="some_category")})
   response = client.get(url)
   assert response.status_code == 200
   assertTemplateUsed(response, 'consumables/consumables_list.html')