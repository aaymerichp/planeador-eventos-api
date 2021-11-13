from rest_framework import serializers
from planeador_eventos_api.api.models.payment import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'user',
            'event',
            'service',
            'amount',
            'payment_date'
        )
