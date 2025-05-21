import django_filters
from .models  import User

class UserFilter(django_filters.FilterSet):
    role = django_filters.CharFilter(method='filter_roles')
    
    def filter_roles(self, queryset, name, value):
        roles = value.split(',')
        return queryset.filter(role__in=roles)
    
    class Meta:
        model = User
        fields = {
            'email': ['exact', 'icontains'],
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'icontains'],
            'is_active': ['exact'],
            'is_staff': ['exact'],
        }
    

    