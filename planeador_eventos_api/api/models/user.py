from django.db import models
import uuid

class User(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.CharField(max_length=200, blank=False, default='')
    name = models.CharField(max_length=200, blank=False, default='')
    type = models.CharField(max_length=200, blank=False, default='')
    phone = models.CharField(max_length=200, blank=False, default='')
    image = models.CharField(max_length=200, blank=False, default='')
    is_active = models.BooleanField(default=True)