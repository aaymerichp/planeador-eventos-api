from rest_framework import serializers
from planeador_eventos_api.api.models.subscription import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = (
            'initial_date',
            'rate',
            'plan_name',
            'allowed_services_count',
            'is_active'
        )
