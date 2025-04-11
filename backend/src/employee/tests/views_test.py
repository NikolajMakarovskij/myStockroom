import pytest

from core.tests.login_test import auto_login_user  # noqa: F401
from employee.models import Departament, Employee, Post
from workplace.models import Workplace


class TestDepartamentEndpoints:
    endpoint = "/api/employee/departament/"

    @pytest.mark.django_db
    def test_list(self, auto_login_user):  # noqa: F811
        Departament.objects.bulk_create(
            [
                Departament(name="01"),
                Departament(name="02"),
                Departament(name="03"),
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
        expected_json = {"name": "04"}

        response = client.post(self.endpoint, data=expected_json, format="json")
        get_response = client.get(self.endpoint)
        data = get_response.data
        assert response.status_code == 200
        assert data[0]["name"] == "04"

    @pytest.mark.django_db
    def test_retrieve(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Departament.objects.get_or_create(name="10")
        test_data = Departament.objects.get(name="10")
        url = f"{self.endpoint}{test_data.id}/"

        response = client.get(url)

        assert response.status_code == 200
        assert response.data["name"] == "10"

    @pytest.mark.django_db
    def test_delete(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Departament.objects.get_or_create(name="10")
        test_data = Departament.objects.get(name="10")
        url = f"{self.endpoint}{test_data.id}/"

        response = client.delete(url)

        assert response.status_code == 204
        assert Departament.objects.all().count() == 0


class TestPostEndpoints:
    endpoint = "/api/employee/post/"

    @pytest.mark.django_db
    def test_list(self, auto_login_user):  # noqa: F811
        Departament.objects.get_or_create(name="01")
        departament = Departament.objects.get(name="01")
        Post.objects.bulk_create(
            [
                Post(name="01", departament=departament),
                Post(name="02"),
                Post(name="03"),
            ]
        )
        client, user = auto_login_user()
        response = client.get("/api/employee/post_list/")
        data = response.data
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]["name"] == "01"
        assert data[0]["departament"]["name"] == "01"
        assert data[1]["name"] == "02"
        assert data[2]["name"] == "03"

    @pytest.mark.django_db
    def test_workplace_list_2(self, auto_login_user):  # noqa: F811
        Departament.objects.get_or_create(name="01")
        departament = Departament.objects.get(name="01")
        Post.objects.bulk_create(
            [
                Post(name="01", departament=departament),
                Post(name="02"),
                Post(name="03"),
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
        Departament.objects.get_or_create(name="01")
        departament = Departament.objects.get(name="01")
        expected_json = {"name": "04", "departament": departament.id}

        response = client.post(self.endpoint, data=expected_json, format="json")
        get_response = client.get("/api/employee/post_list/")
        data = get_response.data
        assert response.status_code == 200
        assert data[0]["name"] == "04"
        assert data[0]["departament"]["name"] == "01"

    @pytest.mark.django_db
    def test_retrieve(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Post.objects.get_or_create(name="10")
        test_data = Post.objects.get(name="10")
        url = f"{self.endpoint}{test_data.id}/"

        response = client.get(url)

        assert response.status_code == 200
        assert response.data["name"] == "10"

    @pytest.mark.django_db
    def test_delete(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Post.objects.get_or_create(name="01")
        test_data = Post.objects.get(name="01")
        url = f"{self.endpoint}{test_data.id}/"

        response = client.delete(url)

        assert response.status_code == 204
        assert Post.objects.all().count() == 0


class TestEmployeeEndpoints:
    endpoint = "/api/employee/employee/"

    @pytest.mark.django_db
    def test_list(self, auto_login_user):  # noqa: F811
        Post.objects.create(name="01")
        post = Post.objects.get(name="01")
        Workplace.objects.create(name="01")
        workplace = Workplace.objects.get(name="01")
        Employee.objects.bulk_create(
            [
                Employee(name="01", surname="01", post=post, workplace=workplace),
                Employee(name="02", surname="02"),
                Employee(name="03", surname="03"),
            ]
        )
        client, user = auto_login_user()
        response = client.get("/api/employee/employee_list/")
        data = response.data
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]["name"] == "01"
        assert data[0]["post"]["name"] == "01"
        assert data[0]["workplace"]["name"] == "01"
        assert data[1]["name"] == "02"
        assert data[2]["name"] == "03"

    @pytest.mark.django_db
    def test_list_2(self, auto_login_user):  # noqa: F811
        Employee.objects.bulk_create(
            [
                Employee(name="01", surname="01"),
                Employee(name="02", surname="02"),
                Employee(name="03", surname="03"),
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
        Post.objects.create(name="01")
        post = Post.objects.get(name="01")
        Workplace.objects.create(name="01")
        workplace = Workplace.objects.get(name="01")
        expected_json = {
            "name": "04",
            "last_name": "12",
            "surname": "22",
            "post": post.id,
            "workplace": workplace.id,
            "employeeEmail": "12345@qw.com",
        }

        response = client.post(self.endpoint, data=expected_json, format="json")
        get_response = client.get("/api/employee/employee_list/")
        data = get_response.data
        assert response.status_code == 200
        assert data[0]["name"] == "04"
        assert data[0]["last_name"] == "12"
        assert data[0]["surname"] == "22"
        assert data[0]["employeeEmail"] == "12345@qw.com"
        assert data[0]["post"]["name"] == "01"
        assert data[0]["workplace"]["name"] == "01"

    @pytest.mark.django_db
    def test_retrieve(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Employee.objects.get_or_create(name="10")
        test_data = Employee.objects.get(name="10")
        url = f"{self.endpoint}{test_data.id}/"

        response = client.get(url)

        assert response.status_code == 200
        assert response.data["name"] == "10"

    @pytest.mark.django_db
    def test_delete(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Employee.objects.get_or_create(name="01")
        test_data = Employee.objects.get(name="01")
        url = f"{self.endpoint}{test_data.id}/"

        response = client.delete(url)

        assert response.status_code == 204
        assert Post.objects.all().count() == 0
