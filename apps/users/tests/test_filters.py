# apps/users/tests/test_filters.py
import pytest
from apps.users.models import User
from apps.users.filters import UserFilter
from django.test import RequestFactory

@pytest.mark.django_db
def test_user_filter_by_role():
    User.objects.create_user(email="a@test.com", username="a", password="1234", role="admin")
    User.objects.create_user(email="b@test.com", username="b", password="1234", role="user")

    data = {'role': 'admin'}
    qs = User.objects.all()
    filtered_qs = UserFilter(data=data, queryset=qs).qs
    assert filtered_qs.count() == 1
    assert filtered_qs.first().role == "admin"
