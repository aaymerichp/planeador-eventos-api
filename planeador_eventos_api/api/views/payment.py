from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from planeador_eventos_api.api.models.payment import Payment
from planeador_eventos_api.api.serializers.payment import PaymentSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_payments(request):
    payments = Payment.objects.all()
    serializer = PaymentSerializer(payments, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def post_payment(request):
    payment = JSONParser().parse(request)
    serializer = PaymentSerializer(data=payment)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_payment(request):
    try:
        payment = Payment.objects.get(pk=request.get('uuid'))
        payment.delete()
        return JsonResponse({'message': 'Payment was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    except Payment.DoesNotExist:
        return JsonResponse({'message': 'The payment does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def put_payment(request):
    payment = JSONParser().parse(request)
    serializer = PaymentSerializer(data=payment)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_payment(request):
    try:
        payment = Payment.objects.get(pk=request.get('uuid'))
        serializer = PaymentSerializer(payment)
        return JsonResponse(serializer.data)
    except Payment.DoesNotExist:
        return JsonResponse({'message': 'The payment does not exist'}, status=status.HTTP_404_NOT_FOUND)
