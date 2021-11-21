from django.db import models
from planeador_eventos_api.api.models.provider import Provider
import uuid

class Service(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    provider = models.UUIDField()
    name = models.CharField(max_length=200, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    type = models.CharField(max_length=200, blank=False, default='')
    image = models.CharField(max_length=200, blank=False, default='')
    provincia = models.CharField(max_length=200, blank=False, default='')
    canton = models.CharField(max_length=200, blank=False, default='')
    is_active = models.BooleanField(default=True)

