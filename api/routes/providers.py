from flask import request, jsonify, Response, make_response

from api.helper.json_encoder import JSONEncoder
from api.app import app, mongo_helper
from api.constants import API_ROUTE

OBJECT = 'provider'
COLLECTION = 'providers'


@app.route(f'/{API_ROUTE}/{OBJECT}/create', methods=['POST'])
def create_provider():
    return jsonify(mongo_helper.insert_one(COLLECTION, request.json))


@app.route(f'/{API_ROUTE}/{OBJECT}/update/<uuid:uuid>', methods=['PUT'])
def update_provider(uuid):
    return jsonify(mongo_helper.update_one(COLLECTION, request.json, uuid))


@app.route(f'/{API_ROUTE}/{OBJECT}/<uuid:uuid>')
def get_provider_by_uuid(uuid):
    match = mongo_helper.get_object_by_uuid(COLLECTION, uuid)
    if match:
        return jsonify(match[0])
    return make_response(jsonify({"message": "No match found"}), 404)


@app.route(f'/{API_ROUTE}/{COLLECTION}', methods=['GET'])
def get_providers():
    return jsonify(mongo_helper.get_all_in_collection(COLLECTION))


@app.route(f'/{API_ROUTE}/{OBJECT}/user_uuid/<string:user>')
def get_provider_by_user(user):
    match = mongo_helper.get_objects_by_attribute(COLLECTION, 'user', user)
    if match:
        return jsonify(match[0])
    return make_response(jsonify({"message": "No match found"}), 404)
