from rest_framework import serializers
from planeador_eventos_api.api.models.service import Service

from rest_framework_mongoengine.serializers import DocumentSerializer

class ServiceSerializer(DocumentSerializer):
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
            'is_active',
            'long_lat'
        )
