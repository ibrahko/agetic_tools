from django.db import models

class BlacklistedClient(models.Model):
    ip_address = models.GenericIPAddressField()
    mac_address = models.CharField(max_length=100, null=True, blank=True)
    reason = models.TextField()
    user_agent = models.TextField(null=True, blank=True)
    location_country = models.CharField(max_length=100, null=True, blank=True)
    location_city = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    attempts = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
