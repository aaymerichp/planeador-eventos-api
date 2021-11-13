from rest_framework import serializers
from planeador_eventos_api.api.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'uuid',
            'email',
            'name',
            'type',
            'phone',
            'image',
            'is_active'
        )
