from flask import request, jsonify, Response, make_response

from api.helper.json_encoder import JSONEncoder
from api.app import app, mongo_helper
from api.constants import API_ROUTE
from api.controller.event import EventController


OBJECT = 'invoice'


@app.route(f'/{API_ROUTE}/{OBJECT}/event/<uuid:event_uuid>', methods=['GET'])
def get_invoice_by_event_uuid(event_uuid):
    invoice_paid_services = []
    event = mongo_helper.get_object_by_uuid('events', event_uuid)
    for service in event.get('services'):
        if service.get('payment_status') == 'PAID':
            service['payment'] = mongo_helper.get_object_by_uuid('payments', service.get('payment_uuid'))
            invoice_paid_services.append(service)
    if invoice_paid_services:
        return jsonify(invoice_paid_services)
    return make_response(jsonify({"message": "No match found"}), 404)
