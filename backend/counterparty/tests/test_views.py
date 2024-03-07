import json, pytest
from counterparty.models import Manufacturer
from core.tests.test_login import auto_login_user

pytestmark = pytest.mark.django_db


class TestManufacturerEndpoints:

    endpoint = '/api/counterparty/manufacturer/'

    @pytest.mark.django_db
    def test_manufacturer_list(self, auto_login_user):
        Manufacturer.objects.bulk_create([
            Manufacturer(name='01', country='Китай', production='Китай'),
            Manufacturer(name='02'),
            Manufacturer(name='03'),
        ])
        client, user = auto_login_user()
        response = client.get(
            self.endpoint
        )
        data = json.loads(response.content)
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]['name'] == '01'
        assert data[0]['country'] == 'Китай'
        assert data[0]['production'] == 'Китай'
        assert data[1]['name'] == '02'
        assert data[2]['name'] == '03'

    @pytest.mark.django_db
    def test_create_manufacturer(self, auto_login_user):
        client, user = auto_login_user()
        expected_json = {
            'name': '04',
            'country': 'Китай',
            'production': 'Китай'
        }

        response = client.post(
            self.endpoint,
            data=expected_json,
            format='json'
        )
        get_response = client.get(
            self.endpoint
        )
        data = json.loads(get_response.content)
        assert response.status_code == 200
        assert data[0]['name'] == '04'
        assert data[0]['country'] == 'Китай'
        assert data[0]['production'] == 'Китай'

    @pytest.mark.django_db
    def test_retrieve_manufacturer(self, auto_login_user):
        client, user = auto_login_user()
        Manufacturer.objects.get_or_create(name='10', country='Китай', production='Китай')
        test_manufacturer = Manufacturer.objects.get(name='10')
        url = f'{self.endpoint}{test_manufacturer.id}/'

        response = client.get(url)

        assert response.status_code == 200
        assert json.loads(response.content)['name'] == '10'
        assert json.loads(response.content)['country'] == 'Китай'
        assert json.loads(response.content)['production'] == 'Китай'

    @pytest.mark.django_db
    def test_delete_manufacturer(self, auto_login_user):
        client, user = auto_login_user()
        Manufacturer.objects.get_or_create(name='10', country='Китай', production='Китай')
        test_manufacturer = Manufacturer.objects.get(name='10')
        url = f'{self.endpoint}{test_manufacturer.id}/'

        response = client.delete(url)

        assert response.status_code == 204
        assert Manufacturer.objects.all().count() == 0