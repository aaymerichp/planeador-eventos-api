from django.urls import path

from planeador_eventos_api.api.views.event import get_events, get_event, post_event, put_event, delete_event
from planeador_eventos_api.api.views.payment import get_payments, get_payment, post_payment, put_payment, delete_payment
from planeador_eventos_api.api.views.product import get_products, get_product, post_product, put_product, delete_product
from planeador_eventos_api.api.views.provider import get_providers, get_provider, post_provider, put_provider, delete_provider
from planeador_eventos_api.api.views.service import get_services, get_service, post_service, put_service, delete_service
from planeador_eventos_api.api.views.subscription import get_subscriptions, get_subscription, post_subscription, put_subscription, delete_subscription
from planeador_eventos_api.api.views.user import get_users, get_user, post_user, put_user, delete_user

urlpatterns = [
    path('api/planeador_eventos_api/events', get_events),
    path('api/planeador_eventos_api/event/<uuid:event_uuid>/', get_event),
    path('api/planeador_eventos_api/event/create/', post_event),
    path('api/planeador_eventos_api/event/update/<uuid:event_uuid>', put_event),
    path('api/planeador_eventos_api/event/delete/<uuid:event_uuid>', delete_event),

    path('api/planeador_eventos_api/payments', get_payments),
    path('api/planeador_eventos_api/payment/<uuid:payment_uuid>', get_payment),
    path('api/planeador_eventos_api/payment/create/', post_payment),
    path('api/planeador_eventos_api/payment/update/<uuid:payment_uuid>', put_payment),
    path('api/planeador_eventos_api/payment/delete/<uuid:payment_uuid>', delete_payment),

    path('api/planeador_eventos_api/products', get_products),
    path('api/planeador_eventos_api/product/<uuid:product_uuid>', get_product),
    path('api/planeador_eventos_api/product/create/', post_product),
    path('api/planeador_eventos_api/product/update/<uuid:product_uuid>', put_product),
    path('api/planeador_eventos_api/product/delete/<uuid:product_uuid>', delete_product),

    path('api/planeador_eventos_api/providers', get_providers),
    path('api/planeador_eventos_api/provider/<uuid:provider_uuid>', get_provider),
    path('api/planeador_eventos_api/provider/create/', post_provider),
    path('api/planeador_eventos_api/provider/update/<uuid:provider_uuid>', put_provider),
    path('api/planeador_eventos_api/provider/delete/<uuid:provider_uuid>', delete_provider),

    path('api/planeador_eventos_api/services', get_services),
    path('api/planeador_eventos_api/service/<uuid:service_uuid>', get_service),
    path('api/planeador_eventos_api/service/create/', post_service),
    path('api/planeador_eventos_api/service/update/<uuid:service_uuid>', put_service),
    path('api/planeador_eventos_api/service/delete/<uuid:service_uuid>', delete_service),

    path('api/planeador_eventos_api/subscriptions', get_subscriptions),
    path('api/planeador_eventos_api/subscription/<uuid:subscription_uuid>', get_subscription),
    #path('api/planeador_eventos_api/subscription/<uuid:subscription_uuid>', get_subscription), TODO: getbyType
    path('api/planeador_eventos_api/subscription/create/', post_subscription),
    path('api/planeador_eventos_api/subscription/update/<uuid:subscription_uuid>', put_subscription),
    path('api/planeador_eventos_api/subscription/delete/<uuid:subscription_uuid>', delete_subscription),

    path('api/planeador_eventos_api/users', get_users),
    path('api/planeador_eventos_api/user/<uuid:user_uuid>', get_user),
    #path('api/planeador_eventos_api/user/<uuid:user_uuid>', get_user), TODO: getByEmail
    path('api/planeador_eventos_api/user/create/', post_user),
    path('api/planeador_eventos_api/user/update/<uuid:user_uuid>', put_user),
    path('api/planeador_eventos_api/user/delete/<uuid:user_uuid>', delete_user)
]
