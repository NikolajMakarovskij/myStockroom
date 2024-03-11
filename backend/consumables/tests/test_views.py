
from ..models import Categories, Consumables, AccCat, Accessories
from counterparty.models import Manufacturer
import json, pytest
from core.tests.test_login import auto_login_user


# Расходники
class TestConsumablesEndpoints:

    endpoint = '/api/consumables/consumable/'

    @pytest.mark.django_db
    def test_consumables_list(self, auto_login_user):
        Categories.objects.get_or_create(name='category_01', slug='category_01')
        Manufacturer.objects.get_or_create(name='manufacturer')
        cat = Categories.objects.get(name='category_01')
        man = Manufacturer.objects.get(name='manufacturer')
        Consumables.objects.bulk_create([
            Consumables(name='01', categories=cat, manufacturer=man),
            Consumables(name='02'),
            Consumables(name='03'),
        ])
        client, user = auto_login_user()
        response = client.get(
            '/api/consumables/consumable_list/'
        )
        data = json.loads(response.content)
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]['name'] == '01'
        assert data[0]['categories']['name'] == 'category_01'
        assert data[0]['categories']['slug'] == 'category_01'
        assert data[0]['manufacturer']['name'] == 'manufacturer'
        assert data[1]['name'] == '02'
        assert data[2]['name'] == '03'

    @pytest.mark.django_db
    def test_consumables_list_2(self, auto_login_user):
        Consumables.objects.bulk_create([
            Consumables(name='01'),
            Consumables(name='02'),
            Consumables(name='03'),
        ])
        client, user = auto_login_user()
        response = client.get(
            self.endpoint
        )
        data = json.loads(response.content)
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]['name'] == '01'
        assert data[1]['name'] == '02'
        assert data[2]['name'] == '03'

    @pytest.mark.django_db
    def test_create(self, auto_login_user):
        client, user = auto_login_user()
        expected_json = {
            'name': '04',
            #'room': room.id
        }

        response = client.post(
            self.endpoint,
            data=expected_json,
            format='json'
        )
        get_response = client.get(
            '/api/consumables/consumable_list/'
        )
        data = json.loads(get_response.content)
        assert response.status_code == 200
        assert data[0]['name'] == '04'
        #assert data[0]['room']['name'] == '01'
        #assert data[0]['room']['floor'] == '01'
        #assert data[0]['room']['building'] == 'Главное'

    @pytest.mark.django_db
    def test_retrieve(self, auto_login_user):
        client, user = auto_login_user()
        Consumables.objects.get_or_create(name='10')
        test_cons =Consumables.objects.get(name='10')
        url = f'{self.endpoint}{test_cons.id}/'

        response = client.get(url)

        assert response.status_code == 200
        assert json.loads(response.content)['name'] == '10'

    @pytest.mark.django_db
    def test_delete(self, auto_login_user):
        client, user = auto_login_user()
        Consumables.objects.get_or_create(name='10')
        test_cons =Consumables.objects.get(name='10')
        url = f'{self.endpoint}{test_cons.id}/'

        response = client.delete(url)

        assert response.status_code == 204
        assert Consumables.objects.all().count() == 0