from flask import request, jsonify, Response, make_response

from api.helper.json_encoder import JSONEncoder
from api.app import app, mongo_helper
from api.constants import API_ROUTE
from api.controller.event import EventController

OBJECT = 'event'
COLLECTION = 'events'


@app.route(f'/{API_ROUTE}/{OBJECT}/create', methods=['POST'])
def create_event():
    event_controller = EventController(request.json)
    new_event = request.json
    calculated_services = event_controller.add_services_to_event()
    if not calculated_services:
        return make_response(jsonify({"message": "No match found for a certain product"}), 404)
    new_event['services'] = calculated_services
    inserted = mongo_helper.insert_one(COLLECTION, new_event)
    json_response = JSONEncoder(ensure_ascii=False).encode(inserted)
    return Response(json_response, status=200, mimetype="application/json")


@app.route(f'/{API_ROUTE}/{OBJECT}/update/<uuid:uuid>', methods=['PUT'])
def update_event(uuid):
    event_controller = EventController(request.json)
    new_event = request.json
    calculated_services = event_controller.add_services_to_event(uuid)
    if not calculated_services:
        return make_response(jsonify({"message": "No match found for a certain product"}), 404)
    new_event['services'] = calculated_services
    inserted = mongo_helper.insert_one(COLLECTION, new_event)
    json_response = JSONEncoder(ensure_ascii=False).encode(inserted)
    return Response(json_response, status=200, mimetype="application/json")


@app.route(f'/{API_ROUTE}/{OBJECT}/<uuid:uuid>')
def get_event_by_uuid(uuid):
    match = mongo_helper.get_object_by_uuid(COLLECTION, uuid)
    if match:
        return jsonify(match[0])
    return make_response(jsonify({"message": "No match found"}), 404)


@app.route(f'/{API_ROUTE}/{COLLECTION}', methods=['GET'])
def get_events():
    return jsonify(mongo_helper.get_all_in_collection(COLLECTION))


@app.route(f'/{API_ROUTE}/{COLLECTION}/user/<string:user>')
def get_events_by_user(user):
    return jsonify(mongo_helper.get_objects_by_attribute(COLLECTION, 'user', user))


