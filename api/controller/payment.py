from uuid import UUID

from api.app import mongo_helper

class PaymentController():
    def __init__(self, payment):
        self.payment = payment

    def pay_service_in_event(self) -> dict:
        new_payment_for_event_services = mongo_helper.insert_one('payments', self.payment)

        paid_event_uuid = self.payment.get('event')
        paid_service_in_event_uuid = self.payment.get('service')

        paid_event = mongo_helper.get_object_by_uuid('events', UUID(paid_event_uuid))

        if not paid_event:
            return {"message": "No match found for a certain event."}

        paid_service_in_event = next(
            item for item in paid_event.get('services') if item['uuid'] == paid_service_in_event_uuid)
        paid_service_in_event['payment_uuid'] = new_payment_for_event_services.get('uuid')
        paid_service_in_event['payment_status'] = 'PAID'
        updated_event = mongo_helper.update_one('events', paid_event, UUID(paid_event_uuid))
        print('updated_event', updated_event)

        return(new_payment_for_event_services)
