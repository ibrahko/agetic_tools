from rest_framework.test import APIRequestFactory
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.request import Request
from apps.users.models import User
import pytest

class SimplePagination(PageNumberPagination):
    page_size = 2

@pytest.mark.django_db
def test_pagination_returns_expected_count():
    for i in range(5):
        User.objects.create_user(email=f"user{i}@test.com", username=f"user{i}", password="1234")

    factory = APIRequestFactory()
    request = factory.get('/fake-url?page=1')
    drf_request = Request(request)
    queryset = User.objects.all().order_by('id')

    paginator = SimplePagination()
    page = paginator.paginate_queryset(queryset, request)
    response = paginator.get_paginated_response(page)

    assert isinstance(response, Response)
    assert response.data['count'] == 2
    assert len(response.data['results']) == 2