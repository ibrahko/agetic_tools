from django.urls import path
from .views import test_post

urlpatterns = [
    path('post-test/', test_post),
]
