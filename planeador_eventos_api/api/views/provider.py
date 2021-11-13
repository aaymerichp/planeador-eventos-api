from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from planeador_eventos_api.api.models.provider import Provider
from planeador_eventos_api.api.serializers.provider import ProviderSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_providers(request):
    providers = Provider.objects.all()
    serializer = ProviderSerializer(providers, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def post_provider(request):
    provider = JSONParser().parse(request)
    serializer = ProviderSerializer(data=provider)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_provider(request, provider_uuid):
    try:
        provider = Provider.objects.get(pk=request.get('event_uuid'))
        provider.delete()
        return JsonResponse({'message': 'provider was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    except Provider.DoesNotExist:
        return JsonResponse({'message': 'The provider does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def put_provider(request, provider_uuid):
    previous_provider = Provider.objects.get(pk=provider_uuid)
    provider  = JSONParser().parse(request)
    serializer = ProviderSerializer(data=provider)

    if serializer.is_valid():
        serializer.update(previous_provider, provider)
        return JsonResponse(serializer.data)

    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_provider(request):
    try:
        provider = Provider.objects.get(pk=request.get('uuid'))
        serializer = ProviderSerializer(provider)
        return JsonResponse(serializer.data)
    except Provider.DoesNotExist:
        return JsonResponse({'message': 'The provider does not exist'}, status=status.HTTP_404_NOT_FOUND)
