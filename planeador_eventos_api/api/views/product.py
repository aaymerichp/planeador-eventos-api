from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from planeador_eventos_api.api.models.product import Product
from planeador_eventos_api.api.serializers.product import ProductSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def post_product(request):
    product = JSONParser().parse(request)
    serializer = ProductSerializer(data=product)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_product(request):
    try:
        product = Product.objects.get(pk=request.get('uuid'))
        product.delete()
        return JsonResponse({'message': 'Product was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    except Product.DoesNotExist:
        return JsonResponse({'message': 'The product does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def put_product(request):
    product = JSONParser().parse(request)
    serializer = ProductSerializer(data=product)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_product(request):
    try:
        product = Product.objects.get(pk=request.get('uuid'))
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)
    except Product.DoesNotExist:
        return JsonResponse({'message': 'The product does not exist'}, status=status.HTTP_404_NOT_FOUND)
