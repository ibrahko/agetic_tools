from rest_framework import serializers
from .models import Project
from ..users.serializers import UserSerializer
from ..users.models import User
from django.contrib.auth import get_user_model


User = get_user_model()

class ProjectSerializer(serializers.ModelSerializer):
    product_owner = UserSerializer(read_only=True)
    team = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'product_owner', 'team', 'created_at', 'updated_at']

class ProjectCreateUpdateSerializer(serializers.ModelSerializer):
    product_owner_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='product_owner'
    )
    team_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all(), source='team'
    )

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'product_owner_id', 'team_ids']
