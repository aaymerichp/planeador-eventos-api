from flask import request, jsonify, Response, make_response
from uuid import UUID

from api.app import app, mongo_helper
from api.constants import API_ROUTE
from api.controller.payment import PaymentController

OBJECT = 'payment'
COLLECTION = 'payments'


@app.route(f'/{API_ROUTE}/{OBJECT}/create', methods=['POST'])
def create_payment():
    if request.json.get('event') and request.json.get('service'):
        payment_controller = PaymentController(request.json)
        new_payment = payment_controller.pay_service_in_event()
        return jsonify(new_payment)
    else:
        return jsonify(mongo_helper.insert_one(COLLECTION, request.json))


@app.route(f'/{API_ROUTE}/{OBJECT}/update/<uuid:uuid>', methods=['PUT'])
def update_payment(uuid):
    return jsonify(mongo_helper.update_one(COLLECTION, request.json, uuid))


@app.route(f'/{API_ROUTE}/{OBJECT}/<uuid:uuid>', methods=['GET'])
def get_payment_by_uuid(uuid):
    match = mongo_helper.get_object_by_uuid(COLLECTION, uuid)
    if match:
        return jsonify(match)
    return make_response(jsonify({"message": "No match found"}), 404)


@app.route(f'/{API_ROUTE}/{COLLECTION}', methods=['GET'])
def get_payments():
    return jsonify(mongo_helper.get_all_in_collection(COLLECTION))

@app.route(f'/{API_ROUTE}/{COLLECTION}/user/<string:user>')
def get_payments_by_user(user):
    print("user", user)
    return jsonify(mongo_helper.get_objects_by_attribute(COLLECTION, 'user.uuid', user))

