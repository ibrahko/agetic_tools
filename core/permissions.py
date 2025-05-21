from rest_framework.permissions import BasePermission

class IsScrumMaster(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'scrum_master'

class IsProductOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'product_owner'

class IsDeveloper(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'developer'
