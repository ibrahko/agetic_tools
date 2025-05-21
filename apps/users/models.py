from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # Ajout du role
    ROLE_CHOICES = (
        ('scrum_master', 'Scrum master'),
        ('product_owner', 'Product owner'),
        ('developer', 'Developer'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='developer')

    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'  # Authentification par email
    REQUIRED_FIELDS = ['username']  
   
    def __str__(self):
        return f"{self.email} ({self.role})"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f"Profil de {self.user.username}"