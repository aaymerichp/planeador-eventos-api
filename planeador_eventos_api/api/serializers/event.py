from rest_framework import serializers
from planeador_eventos_api.api.models.event import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'uuid',
            'start_time',
            'finish_time',
            'name',
            'type',
            'description',
            'image',
            'user',
            'guest_count',
            'provincia',
            'canton',
            'area',
            'services',
            'is_active',
        )
