import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from apps.users.models import User

@pytest.mark.django_db
def test_user_workflow():
    client = APIClient()

    # 1. Inscription d'un utilisateur
    register_url = reverse('register')
    register_data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "Password1234!",
        "confirm_password": "Password1234!",
    }
    response = client.post(register_url, register_data, format='json')
    assert response.status_code == 201
    assert User.objects.filter(email="testuser@example.com").exists()

    # 2. Connexion pour obtenir les tokens JWT
    login_url = reverse('token_obtain_pair')
    login_data = {
        "email": "testuser@example.com",
        "password": "Password1234!"
    }
    response = client.post(login_url, login_data, format='json')
    assert response.status_code == 200
    tokens = response.json()
    assert "access" in tokens and "refresh" in tokens

    # 3. Vérification du token
    verify_url = reverse('token_verify')
    response = client.post(verify_url, {"token": tokens["access"]}, format='json')
    assert response.status_code == 200

    # 4. Accès aux détails de l'utilisateur connecté
    user = User.objects.get(email="testuser@example.com")
    detail_url = reverse('user-detail', kwargs={'pk': user.pk})
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + tokens["access"])
    response = client.get(detail_url)
    assert response.status_code == 200
    assert response.data["email"] == "testuser@example.com"

    # 5. Accès à la liste des utilisateurs (si permissions OK)
    list_url = reverse('users-list')
    response = client.get(list_url)
    assert response.status_code in [200, 403]  # dépend si rôle/permission checkée
