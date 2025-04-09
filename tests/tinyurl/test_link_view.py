import pytest
from django.urls import reverse
from rest_framework import status

from tinyurl.models import Link


@pytest.mark.django_db
def test_link_view_success(api_client):
    original_url = "http://my-site.pl/123/456/?foo=bar"
    response = api_client.post(reverse("link-create"), {"original_url": original_url})
    assert response.status_code == status.HTTP_201_CREATED, response.json()
    link = Link.objects.first()
    assert link
    assert link.original_url == original_url
    assert response.json() == {"short_url": f"http://testserver/r/{link.pk}/"}


@pytest.mark.parametrize(
    "input_data, expected_json",
    (
        pytest.param(
            {"original_url": f"http://my-site.pl/{'x' * 100}"},
            {"original_url": ["Ensure this field has no more than 100 characters."]},
            id="url_too_long",
        ),
        pytest.param(
            {"original_url": ""}, {"original_url": ["This field may not be blank."]}, id="url_empty"
        ),
        pytest.param({}, {"original_url": ["This field is required."]}, id="no_url_key"),
        pytest.param(
            {"original_url": "nie jestem urlem"},
            {"original_url": ["Enter a valid URL."]},
            id="not_a_url",
        ),
        pytest.param(
            {"original_url": None}, {"original_url": ["This field may not be null."]}, id="null"
        ),
        pytest.param(
            {"original_url": 2}, {"original_url": ["Enter a valid URL."]}, id="invalid_type"
        ),
    ),
)
@pytest.mark.django_db
def test_link_view_errors(api_client, input_data, expected_json):
    response = api_client.post(reverse("link-create"), input_data)
    assert (response.status_code, response.json()) == (status.HTTP_400_BAD_REQUEST, expected_json)
    assert not Link.objects.exists()
