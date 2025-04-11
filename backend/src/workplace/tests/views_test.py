import pytest

from core.tests.login_test import auto_login_user  # noqa: F401

from ..models import Room, Workplace

pytestmark = pytest.mark.django_db


class TestRoomEndpoints:
    endpoint = "/api/workplace/room/"

    @pytest.mark.django_db
    def test_room_list(self, auto_login_user):  # noqa: F811
        Room.objects.bulk_create(
            [
                Room(name="01", floor="01", building="Главное"),
                Room(name="02"),
                Room(name="03"),
            ]
        )
        client, user = auto_login_user()
        response = client.get("/api/workplace/room_list/")
        data = response.data
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]["name"] == "01"
        assert data[0]["floor"] == "01"
        assert data[0]["building"] == "Главное"
        assert data[1]["name"] == "02"
        assert data[2]["name"] == "03"

    @pytest.mark.django_db
    def test_room_list_2(self, auto_login_user):  # noqa: F811
        Room.objects.bulk_create(
            [
                Room(name="01", floor="01", building="Главное"),
                Room(name="02"),
                Room(name="03"),
            ]
        )
        client, user = auto_login_user()
        response = client.get(self.endpoint)
        data = response.data
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]["name"] == "01"
        assert data[0]["floor"] == "01"
        assert data[0]["building"] == "Главное"
        assert data[1]["name"] == "02"
        assert data[2]["name"] == "03"

    @pytest.mark.django_db
    def test_create(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        expected_json = {"name": "04", "floor": "01", "building": "Главное"}

        response = client.post(self.endpoint, data=expected_json, format="json")
        get_response = client.get(self.endpoint)
        data = get_response.data
        assert response.status_code == 200
        assert data[0]["name"] == "04"
        assert data[0]["floor"] == "01"
        assert data[0]["building"] == "Главное"

    @pytest.mark.django_db
    def test_retrieve(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Room.objects.get_or_create(name="10", floor="01", building="Главное")
        test_room = Room.objects.get(name="10")
        url = f"{self.endpoint}{test_room.id}/"

        response = client.get(url)

        assert response.status_code == 200
        assert response.data["name"] == "10"
        assert response.data["floor"] == "01"
        assert response.data["building"] == "Главное"

    @pytest.mark.django_db
    def test_delete(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Room.objects.get_or_create(name="10", floor="01", building="Главное")
        test_room = Room.objects.get(name="10")
        url = f"{self.endpoint}{test_room.id}/"

        response = client.delete(url)

        assert response.status_code == 204
        assert Room.objects.all().count() == 0


class TestWorkplaceEndpoints:
    endpoint = "/api/workplace/workplace/"
    endpoint_list = "/api/workplace/workplace_list/"

    @pytest.mark.django_db
    def test_workplace_list(self, auto_login_user):  # noqa: F811
        Room.objects.get_or_create(name="01", floor="01", building="Главное")
        room = Room.objects.get(name="01")
        Workplace.objects.bulk_create(
            [
                Workplace(name="01", room=room),
                Workplace(name="02"),
                Workplace(name="03"),
            ]
        )
        client, user = auto_login_user()
        response = client.get(self.endpoint_list)
        data = response.data
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]["name"] == "01"
        assert data[0]["room"]["name"] == "01"
        assert data[1]["name"] == "02"
        assert data[2]["name"] == "03"

    @pytest.mark.django_db
    def test_workplace_list_2(self, auto_login_user):  # noqa: F811
        Room.objects.get_or_create(name="01", floor="01", building="Главное")
        room = Room.objects.get(name="01")
        Workplace.objects.bulk_create(
            [
                Workplace(name="01", room=room),
                Workplace(name="02"),
                Workplace(name="03"),
            ]
        )
        client, user = auto_login_user()
        response = client.get(self.endpoint)
        data = response.data
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]["name"] == "01"
        assert data[1]["name"] == "02"
        assert data[2]["name"] == "03"

    @pytest.mark.django_db
    def test_create(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Room.objects.get_or_create(name="01", floor="01", building="Главное")
        room = Room.objects.get(name="01")
        expected_json = {"name": "04", "room": room.id}

        response = client.post(self.endpoint, data=expected_json, format="json")
        get_response = client.get("/api/workplace/workplace_list/")
        data = get_response.data
        assert response.status_code == 200
        assert data[0]["name"] == "04"
        assert data[0]["room"]["name"] == "01"
        assert data[0]["room"]["floor"] == "01"
        assert data[0]["room"]["building"] == "Главное"

    @pytest.mark.django_db
    def test_retrieve(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Workplace.objects.get_or_create(name="10")
        test_room = Workplace.objects.get(name="10")
        url = f"{self.endpoint}{test_room.id}/"

        response = client.get(url)

        assert response.status_code == 200
        assert response.data["name"] == "10"

    @pytest.mark.django_db
    def test_delete(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Workplace.objects.get_or_create(name="10")
        test_room = Workplace.objects.get(name="10")
        url = f"{self.endpoint}{test_room.id}/"

        response = client.delete(url)

        assert response.status_code == 204
        assert Workplace.objects.all().count() == 0
