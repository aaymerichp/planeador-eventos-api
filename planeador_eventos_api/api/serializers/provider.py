from rest_framework import serializers
from planeador_eventos_api.api.models.provider import Provider


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = (
            'uuid',
            'user',
            'company_name',
            'subscription'
        )
