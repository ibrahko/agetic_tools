from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer, ProjectCreateUpdateSerializer
from .permissions import IsProductOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated, IsProductOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProjectCreateUpdateSerializer
        return ProjectSerializer
    
    def perform_create(self, serializer):
        # Forcer product_owner à l'utilisateur connecté si besoin
        serializer.save(product_owner=self.request.user)

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    permission_classes = [IsProductOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method in ('PUT', 'PATCH'):
            return ProjectCreateUpdateSerializer
        return ProjectSerializer
