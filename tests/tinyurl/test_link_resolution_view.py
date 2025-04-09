import pytest
from django.urls import reverse
from rest_framework import status

from tinyurl.models import Link


@pytest.fixture
def link_fixture():
    return Link.objects.create(original_url="http://my-site.pl/admin/?foo=bar")


@pytest.mark.django_db
def test_link_resolution_view_success(api_client, link_fixture):
    response = api_client.get(
        reverse("link-resolution", kwargs={"pk": link_fixture.pk}), follow=False
    )
    assert (response.url, response.status_code) == (
        link_fixture.original_url,
        status.HTTP_301_MOVED_PERMANENTLY,
    )


@pytest.mark.django_db
def test_link_view_not_found(api_client):
    response = api_client.get(reverse("link-resolution", kwargs={"pk": 1}))
    assert response.status_code == status.HTTP_404_NOT_FOUND
