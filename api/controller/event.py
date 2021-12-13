from uuid import UUID

from api.app import mongo_helper

class EventController():
    def __init__(self, event):
        self.event = event

    def query_services(self):
        services = self.event.get('services')
        for service in services:
            service_from_db = mongo_helper.get_object_by_uuid('services', UUID(service.get('uuid')))
            if service_from_db:
                service['name'] = service_from_db.get('name')
                service['type'] = service_from_db.get('type')
        return services

    def add_services_to_event(self, previous_event=None):
        previous_event = mongo_helper.get_object_by_uuid('events', previous_event)
        services = self.event.get('services')
        merged_services = []
        if previous_event:
            for new_service in services:
                merged_services = previous_event.get('services')
                merged_services.append(new_service)

        if merged_services:
            services = merged_services

        for service in services:
            total_services_amount, products = self.__calculate_amount_for_service(service)
            if not total_services_amount:
                return None
            service["amount"] = total_services_amount
            service["payment_due_date"] = "2021/12/01"
            service["payment_status"] = "PENDING"
            service["payment_uuid"] = None
            service["products"] = products

        return services


    def __calculate_amount_for_service(self, service):
        amount = 0
        products = []
        for product in service.get('products'):
            product_payment_amount = 0
            product_obj = mongo_helper.get_object_by_uuid('products', UUID(product.get('uuid')))
            if not product_obj:
                return None
            product["name"] = product_obj.get('name')
            product["price"] =  product_obj.get('price')
            product["image"] = product_obj.get('image')
            product["rate_type"] = product_obj.get('rate_type')
            product_payment_amount += product_obj.get('price') * product.get('rate_quantity')
            amount += product_payment_amount
            products.append(product)
        return amount, products