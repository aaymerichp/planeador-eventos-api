from rest_framework import serializers
from planeador_eventos_api.api.models.service import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
            'uuid',
            'provider',
            'name',
            'description',
            'type',
            'image',
            'provincia',
            'canton',
            'is_active'
        )
