import pytest
from apps.users.models import User, Profile

@pytest.mark.django_db
def test_profile_created_on_user_creation():
    user = User.objects.create_user(email="test@TEST.com", username="john", password="1234")
    profile = Profile.objects.get(user=user)
    assert profile is not None

@pytest.mark.django_db
def test_user_email_lowercase_and_username_capitalized():
    user = User.objects.create_user(email="TEST@EMAIL.com", username="john", password="1234")
    assert user.email == "test@email.com"
    assert user.username == "John"
