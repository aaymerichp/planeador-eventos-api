from django.db import models
import uuid
from planeador_eventos_api.api.models.service import Service

class Product(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    service = models.UUIDField()
    name = models.CharField(max_length=50, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)
    image = models.CharField(max_length=200, blank=False, default='')
    rate_type = models.CharField(max_length=200, blank=False, default='')