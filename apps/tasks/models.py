from django.db import models
from core.models import TimeStampModel

# Create your models here.
class Task(TimeStampModel, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_done =  models.BooleanField(default=False)
    assigned_to = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='tasks')
    story = models.ForeignKey('userStories.UserStory', on_delete=models.CASCADE, related_name='tasks')