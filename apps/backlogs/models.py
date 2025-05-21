from django.db import models
from core.models import TimeStampModel

# Create your models here.
class Backlog(TimeStampModel, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey('projects.project', on_delete=models.CASCADE, related_name='backlogs')

    def __str__(self):
        return self.name