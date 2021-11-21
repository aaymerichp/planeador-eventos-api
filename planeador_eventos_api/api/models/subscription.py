from django.db import models


class Subscription(models.Model):
    initial_date = models.DateField()
    rate = models.IntegerField()
    plan_name = models.CharField(max_length=200, blank=False, default='')
    allowed_services_count = models.IntegerField()
    is_active = models.BooleanField(default=True)


