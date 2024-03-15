from ..models import Categories, Accounting
from consumables.models import Consumables, Accessories
import json, pytest
from core.tests.test_login import auto_login_user


class TestAccountingEndpoints:

    endpoint = '/api/accounting/accounting/'

    @pytest.mark.django_db
    def test_accounting_list(self, auto_login_user):
        Categories.objects.get_or_create(name='category_01', slug='category_01')
        cat = Categories.objects.get(name='category_01')
        Accounting.objects.bulk_create([
            Accounting(name='01', categories=cat, quantity=3, cost=2.79),
            Accounting(name='02'),
            Accounting(name='03'),
        ])
        client, user = auto_login_user()
        response = client.get(
            '/api/accounting/accounting_list/'
        )
        data = json.loads(response.content)
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]['name'] == '01'
        assert data[0]['categories']['name'] == 'category_01'
        assert data[0]['categories']['slug'] == 'category_01'
        assert data[0]['costAll'] == 8.37
        assert data[1]['name'] == '02'
        assert data[2]['name'] == '03'

    @pytest.mark.django_db
    def test_accounting_list_2(self, auto_login_user):
        Accounting.objects.bulk_create([
            Accounting(name='01'),
            Accounting(name='02'),
            Accounting(name='03'),
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
        Categories.objects.get_or_create(name='category_01', slug='category_01')
        cat = Categories.objects.get(name='category_01')
        expected_json = {
            'name': '04',
            'categories': cat.id,
        }

        response = client.post(
            self.endpoint,
            data=expected_json,
            format='json'
        )
        get_response = client.get(
            '/api/accounting/accounting_list/'
        )
        data = json.loads(get_response.content)
        assert response.status_code == 200
        assert data[0]['name'] == '04'
        assert data[0]['categories']['name'] == 'category_01'
        assert data[0]['categories']['slug'] == 'category_01'

    @pytest.mark.django_db
    def test_retrieve(self, auto_login_user):
        client, user = auto_login_user()
        Accounting.objects.get_or_create(name='10')
        test_acc =Accounting.objects.get(name='10')
        url = f'{self.endpoint}{test_acc.id}/'

        response = client.get(url)

        assert response.status_code == 200
        assert json.loads(response.content)['name'] == '10'

    @pytest.mark.django_db
    def test_delete(self, auto_login_user):
        client, user = auto_login_user()
        Accounting.objects.get_or_create(name='10')
        test_acc = Accounting.objects.get(name='10')
        url = f'{self.endpoint}{test_acc.id}/'

        response = client.delete(url)

        assert response.status_code == 204
        assert Accounting.objects.all().count() == 0


class TestCategoryEndpoints:

    endpoint = '/api/accounting/accounting_category/'

    @pytest.mark.django_db
    def test_categories_list(self, auto_login_user):
        Categories.objects.get_or_create(name='category_01', slug='category_01'),
        Categories.objects.get_or_create(name='category_02', slug='category_02'),
        Categories.objects.get_or_create(name='category_03', slug='category_03'),
        client, user = auto_login_user()
        response = client.get(
            self.endpoint
        )
        data = json.loads(response.content)
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]['name'] == 'category_01'
        assert data[0]['slug'] == 'category_01'
        assert data[1]['name'] == 'category_02'
        assert data[1]['slug'] == 'category_02'
        assert data[2]['name'] == 'category_03'
        assert data[2]['slug'] == 'category_03'

    @pytest.mark.django_db
    def test_create(self, auto_login_user):
        client, user = auto_login_user()
        expected_json = {
            'name': '04',
            'slug': '04',
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
        assert data[0]['slug'] == '04'

    @pytest.mark.django_db
    def test_retrieve(self, auto_login_user):
        client, user = auto_login_user()
        Categories.objects.get_or_create(name='10', slug='10')
        test_cat = Categories.objects.get(name='10')
        url = f'{self.endpoint}{test_cat.id}/'

        response = client.get(url)

        assert response.status_code == 200
        assert json.loads(response.content)['name'] == '10'
        assert json.loads(response.content)['slug'] == '10'

    @pytest.mark.django_db
    def test_delete(self, auto_login_user):
        client, user = auto_login_user()
        Categories.objects.get_or_create(name='10')
        test_cat =Categories.objects.get(name='10')
        url = f'{self.endpoint}{test_cat.id}/'

        response = client.delete(url)

        assert response.status_code == 204
        assert Categories.objects.all().count() == 0



