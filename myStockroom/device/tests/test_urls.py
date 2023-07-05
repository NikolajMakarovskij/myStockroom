import pytest
import warnings
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from ..models import Device, DeviceCat


# list and create
@pytest.mark.django_db
def test_list_url_exists_at_desired_location(client):
    warnings.filterwarnings(action="ignore")
    links = ['/device/', '/device/search']
    for link in links:
        url = link
        response = client.get(url)
        assert response.status_code == 200


@pytest.mark.django_db
def test_list_uses_correct_url_nad_template(client):
    warnings.filterwarnings(action="ignore")
    links = [
        {'link': 'device:device_list', 'template': 'device/device_list.html'},
        {'link': 'device:device_search', 'template': 'device/device_list.html'},
        {'link': 'device:new-device', 'template': 'Forms/add.html'},
    ]
    for each in links:
        url = reverse(each.get('link'))
        response = client.get(url)
        assert response.status_code == 200
        assertTemplateUsed(response, each.get('template'))


# detail_update_delete
@pytest.mark.django_db
def test_details_url(client):
    warnings.filterwarnings(action="ignore")
    links = [
        {'model': Device, 'link': 'device:device-detail', 'template': 'device/device_detail.html'},
        {'model': Device, 'link': 'device:device-update', 'template': 'Forms/add.html'},
        {'model': Device, 'link': 'device:device-delete', 'template': 'Forms/delete.html'},
    ]
    for each in links:
        model = each.get('model').objects.create(name="some_model")
        url = reverse(each.get('link'), kwargs={"pk": model.pk})
        response = client.get(url)
        assert response.status_code == 200
        assertTemplateUsed(response, each.get('template'))


# category
@pytest.mark.django_db
def test_device_category_url(client):
    warnings.filterwarnings(action="ignore")
    DeviceCat.objects.create(name="some_category", slug="some_category")
    url = reverse('device:category', kwargs={"category_slug": DeviceCat.objects.get(slug="some_category")})
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, 'device/device_list.html')
