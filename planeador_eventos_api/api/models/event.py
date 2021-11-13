from django.db import models
import uuid


class Event(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    start_time = models.DateTimeField(blank=True)
    finish_time = models.DateTimeField(blank=True)
    name = models.CharField(max_length=50, blank=True, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    image = models.CharField(max_length=200, blank=True, default='')
    user = models.UUIDField(blank=True)
    guest_count = models.IntegerField(blank=True)
    provincia = models.JSONField(blank=True)
    canton = models.JSONField(blank=True)
    area = models.JSONField(blank=True)
    services = models.JSONField(blank=True)
    is_active = models.BooleanField(default=True)
