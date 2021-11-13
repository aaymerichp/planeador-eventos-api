from planeador_eventos_api.api.models.provider import Provider
from planeador_eventos_api.api.models.product import Product


class EventController():
    def __init__(self, request):
        self.request = request


    def add_services_to_event(self, previous_event=None):
        services = self.request.get('services')
        merged_services = []
        if previous_event:
            print('p_e_s:', previous_event.services)
            print('s:', services)
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