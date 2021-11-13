from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from planeador_eventos_api.api.models.user import User
from planeador_eventos_api.api.serializers.user import UserSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def post_user(request):
    user = JSONParser().parse(request)
    serializer = UserSerializer(data=user)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_user(request):
    try:
        user = User.objects.get(pk=request.get('uuid'))
        user.delete()
        return JsonResponse({'message': 'user was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    except User.DoesNotExist:
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def put_user(request, user_uuid):
    previous_user = User.objects.get(pk=user_uuid)
    user = JSONParser().parse(request)
    serializer = UserSerializer(data=user)

    if serializer.is_valid():
        serializer.update(previous_user, user)
        return JsonResponse(serializer.data)

    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_user(request, user_uuid):
    try:
        user = User.objects.get(pk=user_uuid)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)
    except User.DoesNotExist:
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)
