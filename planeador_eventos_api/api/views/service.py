from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from planeador_eventos_api.api.models.service import Service
from planeador_eventos_api.api.serializers.service import ServiceSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_services(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def post_service(request):
    service = JSONParser().parse(request)
    print(service)
    serializer = ServiceSerializer(data=service)
    if serializer.is_valid():
        serializer.save()
        saved = serializer.data
        return JsonResponse({'uuid': saved.get('uuid')}, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_service(request, service_uuid):
    try:
        service = Service.objects.get(pk=service_uuid)
        service.delete()
        return JsonResponse({'message': 'service was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    except Service.DoesNotExist:
        return JsonResponse({'message': 'The service does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def put_service(request, service_uuid):
    previous_service = Service.objects.get(pk=service_uuid)
    service = JSONParser().parse(request)
    serializer = ServiceSerializer(data=service)
    if serializer.is_valid():
        serializer.update(previous_service, service)
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_service(request, service_uuid):
    try:
        service = Service.objects.get(pk=service_uuid)
        serializer = ServiceSerializer(service)
        return JsonResponse(serializer.data)
    except Service.DoesNotExist:
        return JsonResponse({'message': 'The service does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_services_by_type(request, service_type):
    try:
        services = Service.objects.filter(type=service_type)
        serializer = ServiceSerializer(services, many=True)
        return JsonResponse(serializer.data, safe=False)
    except Service.DoesNotExist:
        return JsonResponse({'message': f'No service with such type "{service_type}" found'}, status=status.HTTP_404_NOT_FOUND)

# @api_view(['GET'])
# def get_services_by_lat_long(request, lat, long):
#     try:
#         services = Service.object.filter()
