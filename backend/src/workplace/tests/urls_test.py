import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from core.tests.test_login import auto_login_user  # noqa F401

from ..models import Room, Workplace


# list and create
@pytest.mark.django_db
def test_list_url_exists_at_desired_location(auto_login_user):  # noqa F811
    client, user = auto_login_user()
    links = [
        "/workplace/",
        "/workplace/workplace/",
        "/workplace/workplace/search",
        "/workplace/room/",
        "/workplace/room/search",
    ]
    for link in links:
        url = link
        response = client.get(url)
        assert response.status_code == 200


@pytest.mark.django_db
def test_list_uses_correct_url_nad_template(auto_login_user):  # noqa F811
    client, user = auto_login_user()
    links = [
        {
            "link": "workplace:workplace_index",
            "template": "workplace/workplace_index.html",
        },
        {
            "link": "workplace:workplace_list",
            "template": "workplace/workplace_list.html",
        },
        {
            "link": "workplace:workplace_search",
            "template": "workplace/workplace_list.html",
        },
        {"link": "workplace:new-workplace", "template": "Forms/add.html"},
        {"link": "workplace:room_list", "template": "workplace/room_list.html"},
        {"link": "workplace:room_search", "template": "workplace/room_list.html"},
        {"link": "workplace:new-room", "template": "Forms/add.html"},
    ]
    for each in links:
        url = reverse(each.get("link"))
        response = client.get(url)
        assert response.status_code == 200
        assertTemplateUsed(response, each.get("template"))


# detail_update_delete
@pytest.mark.django_db
def test_ups_detail_url(auto_login_user):  # noqa F811
    client, user = auto_login_user()
    links = [
        {
            "model": Workplace,
            "link": "workplace:workplace-detail",
            "template": "workplace/workplace_detail.html",
        },
        {
            "model": Workplace,
            "link": "workplace:workplace-update",
            "template": "Forms/add.html",
        },
        {
            "model": Workplace,
            "link": "workplace:workplace-delete",
            "template": "Forms/delete.html",
        },
        {
            "model": Room,
            "link": "workplace:room-detail",
            "template": "workplace/room_detail.html",
        },
        {"model": Room, "link": "workplace:room-update", "template": "Forms/add.html"},
        {
            "model": Room,
            "link": "workplace:room-delete",
            "template": "Forms/delete.html",
        },
    ]
    for each in links:
        model = each.get("model").objects.create(name="some_model")  # type: ignore[attr-defined]
        url = reverse(each.get("link"), kwargs={"pk": model.pk})  # type: ignore[arg-type]
        response = client.get(url)
        assert response.status_code == 200
        assertTemplateUsed(response, each.get("template"))  # type: ignore[arg-type]
