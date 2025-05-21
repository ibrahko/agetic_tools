from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from .permissions import IsSelf
from core.permissions import IsScrumMaster
from .filters import UserFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # Empêche de modifier un autre utilisateur
    permission_classes = [IsSelf]


class UsersListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter
    # Seul le Scrum Master peut voir tous les users
    permission_classes = [IsScrumMaster]  