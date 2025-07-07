import json

import pytest

from core.tests.login_test import (
    auto_login_user,  # noqa F401
)

from ..models import Accounting, Categories


class TestAccountingEndpoints:
    endpoint = "/api/accounting/accounting/"

    @pytest.mark.django_db
    def test_accounting_list(self, auto_login_user):  # noqa F811
        Categories.objects.get_or_create(name="category_01", slug="category_01")
        cat = Categories.objects.get(name="category_01")
        Accounting.objects.bulk_create(
            [
                Accounting(name="01", categories=cat, quantity=3, cost=2.79),
                Accounting(name="02"),
                Accounting(name="03"),
            ]
        )
        client, user = auto_login_user()
        response = client.get("/api/accounting/accounting_list/")
        data = response.data
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]["name"] == "01"
        assert data[0]["categories"]["name"] == "category_01"
        assert data[0]["categories"]["slug"] == "category_01"
        assert data[0]["costAll"] == 8.37
        assert data[1]["name"] == "02"
        assert data[2]["name"] == "03"

    @pytest.mark.django_db
    def test_accounting_list_2(self, auto_login_user):  # noqa F811
        Accounting.objects.bulk_create(
            [
                Accounting(name="01"),
                Accounting(name="02"),
                Accounting(name="03"),
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
    def test_create(self, auto_login_user):  # noqa F811
        client, user = auto_login_user()
        Categories.objects.get_or_create(name="category_01", slug="category_01")
        cat = Categories.objects.get(name="category_01")
        expected_json = {
            "name": "04",
            "categories": cat.id,
        }

        response = client.post(self.endpoint, data=expected_json, format="json")
        get_response = client.get("/api/accounting/accounting_list/")
        data = get_response.data
        assert response.status_code == 200
        assert data[0]["name"] == "04"
        assert data[0]["categories"]["name"] == "category_01"
        assert data[0]["categories"]["slug"] == "category_01"

    @pytest.mark.django_db
    def test_create_no_valid(self, auto_login_user):  # noqa F811
        client, user = auto_login_user()
        expected_json = {
            "name": "",
            "categories": "",
        }

        response = client.post(self.endpoint, data=expected_json, format="json")
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_retrieve(self, auto_login_user):  # noqa F811
        client, user = auto_login_user()
        Accounting.objects.get_or_create(name="10")
        test_acc = Accounting.objects.get(name="10")
        url = f"{self.endpoint}{test_acc.id}/"

        response = client.get(url)

        assert response.status_code == 200
        assert response.data["name"] == "10"

    @pytest.mark.django_db
    def test_update(self, auto_login_user):  # noqa F811
        client, user = auto_login_user()
        Accounting.objects.get_or_create(name="10")
        test_acc = Accounting.objects.get(name="10")
        Categories.objects.get_or_create(name="category_01", slug="category_01")
        cat = Categories.objects.get(name="category_01").id
        expected_json = {
            "name": "04",
            "categories": cat,
        }
        url = f"{self.endpoint}{test_acc.id}/"
        response = client.put(
            url, data=expected_json, format="json", content_type="application/json"
        )

        get_response = client.get(f"/api/accounting/accounting_list/{test_acc.id}/")
        data = get_response.data
        print(response)
        assert response.status_code == 200
        assert data["name"] == "04"
        assert data["categories"]["name"] == "category_01"
        assert data["categories"]["slug"] == "category_01"

    @pytest.mark.django_db
    def test_update_no_valid(self, auto_login_user):  # noqa F811
        client, user = auto_login_user()
        Accounting.objects.get_or_create(name="10")
        test_acc = Accounting.objects.get(name="10")
        expected_json = {
            "name": "",
            "categories": "",
        }
        url = f"{self.endpoint}{test_acc.id}/"
        response = client.put(
            url, data=expected_json, format="json", content_type="application/json"
        )
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_delete(self, auto_login_user):  # noqa F811
        client, user = auto_login_user()
        Accounting.objects.get_or_create(name="10")
        test_acc = Accounting.objects.get(name="10")
        url = f"{self.endpoint}{test_acc.id}/"

        response = client.delete(url)

        assert response.status_code == 204
        assert Accounting.objects.all().count() == 0


class TestCategoryEndpoints:
    endpoint = "/api/accounting/accounting_category/"

    @pytest.mark.django_db
    def test_categories_list(self, auto_login_user):  # noqa F811
        (Categories.objects.get_or_create(name="category_01", slug="category_01"),)
        (Categories.objects.get_or_create(name="category_02", slug="category_02"),)
        (Categories.objects.get_or_create(name="category_03", slug="category_03"),)
        client, user = auto_login_user()
        response = client.get(self.endpoint)
        data = json.loads(response.content)
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]["name"] == "category_01"
        assert data[0]["slug"] == "category_01"
        assert data[1]["name"] == "category_02"
        assert data[1]["slug"] == "category_02"
        assert data[2]["name"] == "category_03"
        assert data[2]["slug"] == "category_03"

    @pytest.mark.django_db
    def test_create(self, auto_login_user):  # noqa F811
        client, user = auto_login_user()
        expected_json = {
            "name": "04",
            "slug": "04",
        }

        response = client.post(self.endpoint, data=expected_json, format="json")
        get_response = client.get(self.endpoint)
        data = get_response.data
        assert response.status_code == 200
        assert data[0]["name"] == "04"
        assert data[0]["slug"] == "04"

    @pytest.mark.django_db
    def test_create_no_valid(self, auto_login_user):  # noqa F811
        client, user = auto_login_user()
        expected_json = {
            "name": "",
            "slug": "",
        }

        response = client.post(self.endpoint, data=expected_json, format="json")
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_retrieve(self, auto_login_user):  # noqa F811
        client, user = auto_login_user()
        Categories.objects.get_or_create(name="10", slug="10")
        test_cat = Categories.objects.get(name="10")
        url = f"{self.endpoint}{test_cat.id}/"

        response = client.get(url)

        assert response.status_code == 200
        assert response.data["name"] == "10"
        assert response.data["slug"] == "10"

    @pytest.mark.django_db
    def test_update(self, auto_login_user):  # noqa F811
        client, user = auto_login_user()
        Categories.objects.get_or_create(name="category_01", slug="category_01")
        test_cat = Categories.objects.get(name="category_01")
        expected_json = {
            "name": "test",
            "slug": "test",
        }
        url = f"{self.endpoint}{test_cat.id}/"
        response = client.put(
            url, data=expected_json, format="json", content_type="application/json"
        )

        get_response = client.get(f"{self.endpoint}{test_cat.id}/")
        data = get_response.data
        print(response)
        assert response.status_code == 200
        assert data["name"] == "test"
        assert data["slug"] == "test"

    @pytest.mark.django_db
    def test_update_no_valid(self, auto_login_user):  # noqa F811
        client, user = auto_login_user()
        Categories.objects.get_or_create(name="category_01", slug="category_01")
        test_cat = Categories.objects.get(name="category_01")
        expected_json = {
            "name": "",
            "slug": "",
        }
        url = f"{self.endpoint}{test_cat.id}/"
        response = client.put(
            url, data=expected_json, format="json", content_type="application/json"
        )
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_delete(self, auto_login_user):  # noqa F811
        client, user = auto_login_user()
        Categories.objects.get_or_create(name="10")
        test_cat = Categories.objects.get(name="10")
        url = f"{self.endpoint}{test_cat.id}/"

        response = client.delete(url)

        assert response.status_code == 204
        assert Categories.objects.all().count() == 0
