from django.db import models
from core.models import TimeStampModel

# Create your models here.
class Sprint(TimeStampModel, models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey('projects.project', on_delete=models.CASCADE, related_name='sprints')
    start_date = models.DateField()
    end_date = models.DateField()
    goal = models.TextField()

    def __str__(self):
        return self.name