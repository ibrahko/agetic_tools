from django.db import models
from core.models import TimeStampModel

# Create your models here.
class UserStory(TimeStampModel, models.Model):
    epics = models.ForeignKey('epics.epic', on_delete=models.CASCADE, related_name='user_stories')
    sprints = models.ForeignKey('sprints.sprint', on_delete=models.CASCADE, related_name='user_stories')
    title = models.CharField(max_length=100)
    description = models.TextField()
    users = models.ForeignKey('users.user', on_delete=models.CASCADE, related_name='user_stories')

    def __str__(self):
        return f"le titre du userStory est  {self.title}"