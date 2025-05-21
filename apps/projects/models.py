from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Product Owner qui crée le projet
    product_owner = models.ForeignKey(
        'users.user', 
        on_delete=models.CASCADE, 
        related_name='owned_projects'
    )
    
    # Équipe de projet (scrum team)
    team = models.ManyToManyField(
        'users.user', 
        related_name='projects'
    )
    
    def __str__(self):
        return self.name
