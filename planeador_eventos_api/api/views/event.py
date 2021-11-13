from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from planeador_eventos_api.api.models.event import Event
from planeador_eventos_api.api.serializers.event import EventSerializer
from planeador_eventos_api.api.controllers.event import EventController
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_events(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return JsonResponse(serializer.data, safe=False)




@api_view(['POST'])
def post_event(request):
    event = JSONParser().parse(request)
    serializer = EventSerializer(data=event)
    controller = EventController(event)
    if serializer.is_valid():
        serializer.save(services=controller.add_services_to_event())
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_event(request, event_uuid):
    try:
        event = Event.objects.get(pk=event_uuid)
        event.delete()
        return JsonResponse({'message': 'Event was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    except Event.DoesNotExist:
        return JsonResponse({'message': 'The event does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def put_event(request, event_uuid):
    previous_event = Event.objects.get(pk=event_uuid)
    event = JSONParser().parse(request)
    serializer = EventSerializer(data=event)
    controller = EventController(event)
    event['services'] = controller.add_services_to_event(previous_event)
    if serializer.is_valid():
        serializer.update(previous_event, event)
        return JsonResponse(serializer.data)

    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_event(request, event_uuid):
    print(event_uuid)

    try:
        event = Event.objects.get(pk=event_uuid)
        serializer = EventSerializer(event)
        return JsonResponse(serializer.data)
    except Event.DoesNotExist:
        return JsonResponse({'message': 'The event does not exist'}, status=status.HTTP_404_NOT_FOUND)
