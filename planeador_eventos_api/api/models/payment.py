from django.db import models
from planeador_eventos_api.api.models.user import User
from planeador_eventos_api.api.models.event import Event
from planeador_eventos_api.api.models.service import Service
import uuid

class Payment(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = User().uuid
    event = Event().uuid
    service = Service().uuid
    amount = models.IntegerField()
    payment_date = models.DateField()

