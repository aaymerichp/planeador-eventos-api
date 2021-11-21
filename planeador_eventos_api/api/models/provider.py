from django.db import models
import uuid


class Provider(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.UUIDField()
    company_name = models.CharField(max_length=200, blank=False, default='')
    subscription = models.JSONField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user'], name='provider_uniqueness')
        ]