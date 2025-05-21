import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from apps.users.models import User

@pytest.mark.django_db
def test_register_view():
    client = APIClient()
    url = reverse("register")  # change si besoin
    data = {
        "email": "new@test.com",
        "username": "newuser",
        "password": "pass1234"
    }
    response = client.post(url, data)
    assert response.status_code == 201
    assert User.objects.filter(email="new@test.com").exists()

@pytest.mark.django_db
def test_user_detail_permission_is_self():
    user1 = User.objects.create_user(email="a@a.com", username="a", password="1234")
    user2 = User.objects.create_user(email="b@b.com", username="b", password="1234")

    client = APIClient()
    client.force_authenticate(user=user1)  # ✅ force l'authentification

    # Cas 1 : user1 essaie de voir les infos de user2
    url_other = reverse("user-detail", kwargs={"pk": user2.pk})
    res = client.get(url_other)
    assert res.status_code == 403  # Interdit

    # Cas 2 : user1 voit ses propres infos
    url_self = reverse("user-detail", kwargs={"pk": user1.pk})
    res = client.get(url_self)
    assert res.status_code == 200  # Autorisé
