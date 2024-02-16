import json, pytest
from workplace.models import Room, Workplace
from core.tests.test_login import auto_login_user


pytestmark = pytest.mark.django_db


class TestRoomEndpoints:

    endpoint = '/api/workplace/room/'

    @pytest.mark.django_db
    def test_room_list(self, auto_login_user):
        Room.objects.bulk_create([
            Room(name='01', floor='01', building='Главное'),
            Room(name='02'),
            Room(name='03'),
        ])
        client, user = auto_login_user()
        response = client.get(
            '/api/workplace/room_list/'
        )
        data = json.loads(response.content)
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]['name'] == '01'
        assert data[0]['floor'] == '01'
        assert data[0]['building'] == 'Главное'
        assert data[1]['name'] == '02'
        assert data[2]['name'] == '03'

    @pytest.mark.django_db
    def test_room_list_2(self, auto_login_user):
        Room.objects.bulk_create([
            Room(name='01', floor='01', building='Главное'),
            Room(name='02'),
            Room(name='03'),
        ])
        client, user = auto_login_user()
        response = client.get(
            self.endpoint
        )
        data = json.loads(response.content)
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]['name'] == '01'
        assert data[0]['floor'] == '01'
        assert data[0]['building'] == 'Главное'
        assert data[1]['name'] == '02'
        assert data[2]['name'] == '03'

    @pytest.mark.django_db
    def test_create(self, auto_login_user):
        client, user = auto_login_user()
        expected_json = {
            'name': '04',
            'floor': '01',
            'building': 'Главное'
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
        assert data[0]['floor'] == '01'
        assert data[0]['building'] == 'Главное'

    @pytest.mark.django_db
    def test_retrieve(self, auto_login_user):
        client, user = auto_login_user()
        Room.objects.get_or_create(name='10', floor='01', building='Главное')
        test_room = Room.objects.get(name='10')
        url = f'{self.endpoint}{test_room.id}/'

        response = client.get(url)

        assert response.status_code == 200
        assert json.loads(response.content)['name'] == '10'
        assert json.loads(response.content)['floor'] == '01'
        assert json.loads(response.content)['building'] == 'Главное'

    @pytest.mark.django_db
    def test_delete(self, auto_login_user):
        client, user = auto_login_user()
        Room.objects.get_or_create(name='10', floor='01', building='Главное')
        test_room = Room.objects.get(name='10')
        url = f'{self.endpoint}{test_room.id}/'

        response = client.delete(url)

        assert response.status_code == 204
        assert Room.objects.all().count() == 0

class TestWorkplaceEndpoints:

    endpoint = '/api/workplace/workplace/'

    @pytest.mark.django_db
    def test_workplace_list(self, auto_login_user):
        Room.objects.get_or_create(name='01')
        room = Room.objects.get(name='01')
        Workplace.objects.bulk_create([
            Workplace(name='01', room=room),
            Workplace(name='02'),
            Workplace(name='03'),
        ])
        client, user = auto_login_user()
        response = client.get(
            '/api/workplace/workplace_list/'
        )
        data = json.loads(response.content)
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]['name'] == '01'
        assert data[0]['room']['name'] == '01'
        assert data[1]['name'] == '02'
        assert data[2]['name'] == '03'

    @pytest.mark.django_db
    def test_workplace_list_2(self, auto_login_user):
        Room.objects.get_or_create(name='01', floor='01', building='Главное')
        room = Room.objects.get(name='01')
        Workplace.objects.bulk_create([
            Workplace(name='01', room=room),
            Workplace(name='02'),
            Workplace(name='03'),
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
        Room.objects.get_or_create(name='01', floor='01', building='Главное')
        room = Room.objects.get(name='01')
        expected_json = {
            'name': '04',
            'room': room.id
        }

        response = client.post(
            self.endpoint,
            data=expected_json,
            format='json'
        )
        get_response = client.get(
            '/api/workplace/workplace_list/'
        )
        data = json.loads(get_response.content)
        assert response.status_code == 200
        assert data[0]['name'] == '04'
        assert data[0]['room']['name'] == '01'
        assert data[0]['room']['floor'] == '01'
        assert data[0]['room']['building'] == 'Главное'

    @pytest.mark.django_db
    def test_retrieve(self, auto_login_user):
        client, user = auto_login_user()
        Workplace.objects.get_or_create(name='10')
        test_room = Workplace.objects.get(name='10')
        url = f'{self.endpoint}{test_room.id}/'

        response = client.get(url)

        assert response.status_code == 200
        assert json.loads(response.content)['name'] == '10'

    @pytest.mark.django_db
    def test_delete(self, auto_login_user):
        client, user = auto_login_user()
        Workplace.objects.get_or_create(name='10')
        test_room = Workplace.objects.get(name='10')
        url = f'{self.endpoint}{test_room.id}/'

        response = client.delete(url)

        assert response.status_code == 204
        assert Workplace.objects.all().count() == 0