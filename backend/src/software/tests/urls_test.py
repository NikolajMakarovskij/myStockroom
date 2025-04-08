import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from core.tests.test_login import auto_login_user  # noqa F401

from ..models import Os, Software


# list and create
@pytest.mark.django_db
def test_list_url_exists_at_desired_location(auto_login_user):  # noqa F811
    client, user = auto_login_user()
    links = [
        "/software/",
        "/software/software/",
        "/software/software/search",
        "/software/OS/",
        "/software/OS/search",
    ]
    for link in links:
        url = link
        response = client.get(url)
        assert response.status_code == 200


@pytest.mark.django_db
def test_list_uses_correct_url_nad_template(auto_login_user):  # noqa F811
    client, user = auto_login_user()
    links = [
        {"link": "software:software_index", "template": "software/soft_index.html"},
        {"link": "software:software_list", "template": "software/software_list.html"},
        {"link": "software:software_search", "template": "software/software_list.html"},
        {"link": "software:new-software", "template": "Forms/add.html"},
        {"link": "software:OS_list", "template": "software/OS_list.html"},
        {"link": "software:OS_search", "template": "software/OS_list.html"},
        {"link": "software:new-OS", "template": "Forms/add.html"},
    ]
    for each in links:
        url = reverse(each.get("link"))
        response = client.get(url)
        assert response.status_code == 200
        assertTemplateUsed(response, each.get("template"))


# detail_update_delete
@pytest.mark.django_db
def test_details_url(auto_login_user):  # noqa F811
    client, user = auto_login_user()
    links = [
        {
            "model": Software,
            "link": "software:software-detail",
            "template": "software/software_detail.html",
        },
        {
            "model": Software,
            "link": "software:software-update",
            "template": "Forms/add.html",
        },
        {
            "model": Software,
            "link": "software:software-delete",
            "template": "Forms/delete.html",
        },
        {
            "model": Os,
            "link": "software:OS-detail",
            "template": "software/OS_detail.html",
        },
        {"model": Os, "link": "software:OS-update", "template": "Forms/add.html"},
        {"model": Os, "link": "software:OS-delete", "template": "Forms/delete.html"},
    ]
    for each in links:
        model = each.get("model").objects.create(name="some_model")
        url = reverse(each.get("link"), kwargs={"pk": model.pk})
        response = client.get(url)
        assert response.status_code == 200
        assertTemplateUsed(response, each.get("template"))
