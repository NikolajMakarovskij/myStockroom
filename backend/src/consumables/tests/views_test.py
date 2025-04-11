import pytest

from accounting.models import Accounting
from core.tests.login_test import auto_login_user  # noqa: F401
from counterparty.models import Manufacturer

from ..models import AccCat, Accessories, Categories, Consumables


# Расходники
class TestConsumablesEndpoints:
    endpoint = "/api/consumables/consumable/"

    @pytest.mark.django_db
    def test_consumables_list(self, auto_login_user):  # noqa: F811
        Categories.objects.get_or_create(name="category_01", slug="category_01")
        Manufacturer.objects.get_or_create(name="manufacturer")
        cat = Categories.objects.get(name="category_01")
        man = Manufacturer.objects.get(name="manufacturer")
        Consumables.objects.bulk_create(
            [
                Consumables(name="01", categories=cat, manufacturer=man, quantity=1),
                Consumables(name="02"),
                Consumables(name="03"),
            ]
        )
        Accounting.objects.get_or_create(
            name="category_01",
            quantity=2,
            consumable=Consumables.objects.get(name="01"),
        )
        client, user = auto_login_user()
        response = client.get("/api/consumables/consumable_list/")
        data = response.data
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]["name"] == "01"
        assert data[0]["categories"]["name"] == "category_01"
        assert data[0]["categories"]["slug"] == "category_01"
        assert data[0]["manufacturer"]["name"] == "manufacturer"
        assert data[0]["difference"] == -1
        assert data[1]["name"] == "02"
        assert data[2]["name"] == "03"

    @pytest.mark.django_db
    def test_consumables_list_2(self, auto_login_user):  # noqa: F811
        Consumables.objects.bulk_create(
            [
                Consumables(name="01"),
                Consumables(name="02"),
                Consumables(name="03"),
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
        Categories.objects.get_or_create(name="category_01", slug="category_01")
        Manufacturer.objects.get_or_create(name="manufacturer")
        cat = Categories.objects.get(name="category_01")
        man = Manufacturer.objects.get(name="manufacturer")
        expected_json = {"name": "04", "categories": cat.id, "manufacturer": man.id}

        response = client.post(self.endpoint, data=expected_json, format="json")
        get_response = client.get("/api/consumables/consumable_list/")
        data = get_response.data
        assert response.status_code == 200
        assert data[0]["name"] == "04"
        assert data[0]["categories"]["name"] == "category_01"
        assert data[0]["categories"]["slug"] == "category_01"
        assert data[0]["manufacturer"]["name"] == "manufacturer"

    @pytest.mark.django_db
    def test_retrieve(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Consumables.objects.get_or_create(name="10")
        test_cons = Consumables.objects.get(name="10")
        url = f"{self.endpoint}{test_cons.id}/"

        response = client.get(url)

        assert response.status_code == 200
        assert response.data["name"] == "10"

    @pytest.mark.django_db
    def test_delete(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Consumables.objects.get_or_create(name="10")
        test_cons = Consumables.objects.get(name="10")
        url = f"{self.endpoint}{test_cons.id}/"

        response = client.delete(url)

        assert response.status_code == 204
        assert Consumables.objects.all().count() == 0


class TestConsumablesCategoryEndpoints:
    endpoint = "/api/consumables/consumable_category/"

    @pytest.mark.django_db
    def test_categories_list(self, auto_login_user):  # noqa: F811
        (Categories.objects.get_or_create(name="category_01", slug="category_01"),)
        (Categories.objects.get_or_create(name="category_02", slug="category_02"),)
        (Categories.objects.get_or_create(name="category_03", slug="category_03"),)
        client, user = auto_login_user()
        response = client.get(self.endpoint)
        data = response.data
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]["name"] == "category_01"
        assert data[0]["slug"] == "category_01"
        assert data[1]["name"] == "category_02"
        assert data[1]["slug"] == "category_02"
        assert data[2]["name"] == "category_03"
        assert data[2]["slug"] == "category_03"

    @pytest.mark.django_db
    def test_create(self, auto_login_user):  # noqa: F811
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
    def test_retrieve(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Categories.objects.get_or_create(name="10", slug="10")
        test_cat = Categories.objects.get(name="10")
        url = f"{self.endpoint}{test_cat.id}/"

        response = client.get(url)

        assert response.status_code == 200
        assert response.data["name"] == "10"
        assert response.data["slug"] == "10"

    @pytest.mark.django_db
    def test_delete(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Categories.objects.get_or_create(name="10")
        test_cat = Categories.objects.get(name="10")
        url = f"{self.endpoint}{test_cat.id}/"

        response = client.delete(url)

        assert response.status_code == 204
        assert Categories.objects.all().count() == 0


# Комплектующие
class TestAccessoriesEndpoints:
    endpoint = "/api/consumables/accessories/"

    @pytest.mark.django_db
    def test_accessories_list(self, auto_login_user):  # noqa: F811
        AccCat.objects.get_or_create(name="category_01", slug="category_01")
        Manufacturer.objects.get_or_create(name="manufacturer")
        cat = AccCat.objects.get(name="category_01")
        man = Manufacturer.objects.get(name="manufacturer")
        Accessories.objects.bulk_create(
            [
                Accessories(name="01", categories=cat, manufacturer=man, quantity=1),
                Accessories(name="02"),
                Accessories(name="03"),
            ]
        )
        Accounting.objects.get_or_create(
            name="category_01",
            quantity=2,
            accessories=Accessories.objects.get(name="01"),
        )
        client, user = auto_login_user()
        response = client.get("/api/consumables/accessories_list/")
        data = response.data
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]["name"] == "01"
        assert data[0]["categories"]["name"] == "category_01"
        assert data[0]["categories"]["slug"] == "category_01"
        assert data[0]["manufacturer"]["name"] == "manufacturer"
        assert data[0]["difference"] == -1
        assert data[1]["name"] == "02"
        assert data[2]["name"] == "03"

    @pytest.mark.django_db
    def test_accessories_list_2(self, auto_login_user):  # noqa: F811
        Accessories.objects.bulk_create(
            [
                Accessories(name="01"),
                Accessories(name="02"),
                Accessories(name="03"),
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
        AccCat.objects.get_or_create(name="category_01", slug="category_01")
        Manufacturer.objects.get_or_create(name="manufacturer")
        cat = AccCat.objects.get(name="category_01")
        man = Manufacturer.objects.get(name="manufacturer")
        expected_json = {"name": "04", "categories": cat.id, "manufacturer": man.id}

        response = client.post(self.endpoint, data=expected_json, format="json")
        get_response = client.get("/api/consumables/accessories_list/")
        data = get_response.data
        assert response.status_code == 200
        assert data[0]["name"] == "04"
        assert data[0]["categories"]["name"] == "category_01"
        assert data[0]["categories"]["slug"] == "category_01"
        assert data[0]["manufacturer"]["name"] == "manufacturer"

    @pytest.mark.django_db
    def test_retrieve(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Accessories.objects.get_or_create(name="10")
        test_cons = Accessories.objects.get(name="10")
        url = f"{self.endpoint}{test_cons.id}/"

        response = client.get(url)

        assert response.status_code == 200
        assert response.data["name"] == "10"

    @pytest.mark.django_db
    def test_delete(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Accessories.objects.get_or_create(name="10")
        test_cons = Accessories.objects.get(name="10")
        url = f"{self.endpoint}{test_cons.id}/"

        response = client.delete(url)

        assert response.status_code == 204
        assert Accessories.objects.all().count() == 0


class TestAccessoriesCategoryEndpoints:
    endpoint = "/api/consumables/accessories_category/"

    @pytest.mark.django_db
    def test_categories_list(self, auto_login_user):  # noqa: F811
        (AccCat.objects.get_or_create(name="category_01", slug="category_01"),)
        (AccCat.objects.get_or_create(name="category_02", slug="category_02"),)
        (AccCat.objects.get_or_create(name="category_03", slug="category_03"),)
        client, user = auto_login_user()
        response = client.get(self.endpoint)
        data = response.data
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]["name"] == "category_01"
        assert data[0]["slug"] == "category_01"
        assert data[1]["name"] == "category_02"
        assert data[1]["slug"] == "category_02"
        assert data[2]["name"] == "category_03"
        assert data[2]["slug"] == "category_03"

    @pytest.mark.django_db
    def test_create(self, auto_login_user):  # noqa: F811
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
    def test_retrieve(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        AccCat.objects.get_or_create(name="10", slug="10")
        test_cat = AccCat.objects.get(name="10")
        url = f"{self.endpoint}{test_cat.id}/"

        response = client.get(url)

        assert response.status_code == 200
        assert response.data["name"] == "10"
        assert response.data["slug"] == "10"

    @pytest.mark.django_db
    def test_delete(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        AccCat.objects.get_or_create(name="10")
        test_cat = AccCat.objects.get(name="10")
        url = f"{self.endpoint}{test_cat.id}/"

        response = client.delete(url)

        assert response.status_code == 204
        assert AccCat.objects.all().count() == 0
