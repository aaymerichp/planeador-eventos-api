from rest_framework import serializers
from planeador_eventos_api.api.models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'uuid',
            'service',
            'name',
            'description',
            'price',
            'is_active',
            'image',
            'rate_type'
        )
