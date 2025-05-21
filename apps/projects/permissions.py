from rest_framework.permissions import BasePermission

class IsProductOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Tout le monde peut lire
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return request.user in obj.team.all() or request.user == obj.product_owner
        # Modifier seulement si product_owner
        return obj.product_owner == request.user
