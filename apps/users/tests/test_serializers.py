import pytest
from apps.users.serializers import UserSerializer

@pytest.mark.django_db
def test_user_serializer_valid_data():
    data = {
        "email": "valid@test.com",
        "username": "validuser",
        "password": "strongpass123",
        "role": "developer"
    }
    serializer = UserSerializer(data=data)
    assert serializer.is_valid()
    user = serializer.save()
    assert user.email == "valid@test.com"

@pytest.mark.django_db
def test_user_serializer_missing_email():
    data = {
        "username": "nouser",
        "password": "pass1234"
    }
    serializer = UserSerializer(data=data)
    assert not serializer.is_valid()
    assert "email" in serializer.errors
