import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from apps.users.models import User

@pytest.mark.django_db
def test_only_scrum_master_can_list_users():
    # Création de deux utilisateurs avec rôles différents
    dev = User.objects.create_user(email="dev@test.com", username="dev", password="1234", role="developer")
    scrum = User.objects.create_user(email="scrum@test.com", username="scrum", password="1234", role="scrum_master")   

    url = reverse("users-list")  # Le nom de la route pour UsersListView

    # Cas 1 : un développeur essaie d'accéder à la liste
    client = APIClient()
    client.force_authenticate(user=dev)  # Authentification manuelle
    response = client.get(url)
    assert response.status_code == 403  # Refusé car ce n’est pas un Scrum Master

    # Cas 2 : le Scrum Master accède à la liste
    client.force_authenticate(user=scrum)
    response = client.get(url)
    assert response.status_code == 200  # Autorisé
