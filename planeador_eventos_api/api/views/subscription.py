from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from planeador_eventos_api.api.models.subscription import Subscription
from planeador_eventos_api.api.serializers.subscription import SubscriptionSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_subscriptions(request):
    subscriptions = Subscription.objects.all()
    serializer = SubscriptionSerializer(subscriptions, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def post_subscription(request):
    subscription = JSONParser().parse(request)
    serializer = SubscriptionSerializer(data=subscription)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_subscription(request, subscription_uuid):
    try:
        subscription = Subscription.objects.get(pk=subscription_uuid)
        subscription.delete()
        return JsonResponse({'message': 'subscription was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    except Subscription.DoesNotExist:
        return JsonResponse({'message': 'The subscription does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def put_subscription(request, subscription_uuid):
    previous_subscription = Subscription.objects.get(pk=subscription_uuid)
    subscription = JSONParser().parse(request)
    serializer = SubscriptionSerializer(data=subscription)
    if serializer.is_valid():
        serializer.update(previous_subscription, subscription)
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_subscription(request, subscription_uuid):
    try:
        subscription = Subscription.objects.get(pk=subscription_uuid)
        serializer = SubscriptionSerializer(subscription)
        return JsonResponse(serializer.data)
    except Subscription.DoesNotExist:
        return JsonResponse({'message': 'The subscription does not exist'}, status=status.HTTP_404_NOT_FOUND)
