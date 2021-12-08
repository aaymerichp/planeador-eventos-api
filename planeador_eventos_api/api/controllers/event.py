from uuid import UUID

from planeador_eventos_api.api.models.provider import Provider
from planeador_eventos_api.api.models.product import Product
from planeador_eventos_api.api.models.service import Service
from planeador_eventos_api.api.models.event import Event


class EventController():
    def __init__(self, event):
        self.event = event

    def query_services(self):
        services = self.event.services
        services_uuids = [service.get('uuid') for service in self.event.services]
        services_from_db = list(Service.objects.filter(uuid__in=services_uuids).values())
        print('services_from_db', services_from_db)
        for service in services:
            print('service', service)
            service_from_db = next((item for item in services_from_db if item['uuid'] == UUID(service['uuid'])), None)
            if service_from_db:
                service['name'] = service_from_db.get('name')
                service['type'] = service_from_db.get('type')
        return services

    def add_services_to_event(self, previous_event=None):
        services = self.event.get('services')
        merged_services = []
        if previous_event:
            for new_service in services:
                merged_services = previous_event.services
                merged_services.append(new_service)

        if merged_services:
            services = merged_services

        for service in services:
            total_services_amount, products = self.calculate_amount_for_service(service)
            service["amount"] = total_services_amount
            service["payment_due_date"] = "2021/12/01"
            service["payment_status"] = "PENDING"
            service["payment_uuid"] = None
            service["products"] = products

        return services

    def calculate_amount_for_service(self, service):
        amount = 0
        products = []
        for product in service.get('products'):
            product_payment_amount = 0
            product_obj = Product.objects.get(pk=product.get('uuid'))
            product["name"] = product_obj.name
            product["price"] =  product_obj.price
            product["image"] = product_obj.image
            product["rate_type"] = product_obj.rate_type
            product_payment_amount += product_obj.price * product.get('rate_quantity')
            amount += product_payment_amount
            products.append(product)

        return amount, products