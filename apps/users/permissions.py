from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSelf(BasePermission):

    # L'utilisateur ne peut et ne doit modifier que ses propres infos.

    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsAdminUserOrReadOnly(BasePermission):
    # Les admins peuvent tout faire, les autres seulement lire.
    
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_staff
