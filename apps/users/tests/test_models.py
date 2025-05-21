import pytest
from apps.users.models import User, Profile

@pytest.mark.django_db
def test_user_model():
    user = User.objects.create_user(email="test@test.com", username="test", password="1234", role="developer")
    assert user.email == "test@test.com"
    assert user.role == "developer"
    assert user.check_password("1234")

@pytest.mark.django_db
def test_profile_created():
    user = User.objects.create_user(email="test@test.com", username="test", password="1234")
    assert Profile.objects.filter(user=user).exists()
