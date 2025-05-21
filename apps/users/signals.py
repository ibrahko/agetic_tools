from django.db.models.signals import post_save, pre_save
from django.db import models
from django.dispatch import receiver
from .models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(pre_save, sender=User)
def format_user_data(sender, instance, **kwargs):
    # Forcer l’email en minuscules
    if instance.email:
        instance.email = instance.email.lower()

    # Capitaliser le prénom si fourni
    if instance.username:
        instance.username = instance.username.capitalize()