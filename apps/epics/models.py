from django.db import models
from core.models import TimeStampModel

# Create your models here.
class Epic(TimeStampModel, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey('projects.project', on_delete=models.CASCADE, related_name='epics')
    backlog = models.ForeignKey('backlogs.backlog', on_delete=models.CASCADE, related_name='epics')

    def __str__(self):
        return self.name