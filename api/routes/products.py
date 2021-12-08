from flask import request, jsonify, Response, make_response

from api.helper.json_encoder import JSONEncoder
from api.app import app, mongo_helper
from api.constants import API_ROUTE

OBJECT = 'product'
COLLECTION = 'products'


@app.route(f'/{API_ROUTE}/{OBJECT}/create', methods=['POST'])
def create_product():
    return jsonify(mongo_helper.insert_one(COLLECTION, request.json))

@app.route(f'/{API_ROUTE}/{OBJECT}/update/<uuid:uuid>', methods=['PUT'])
def update_product(uuid):
    return jsonify(mongo_helper.update_one(COLLECTION, request.json, uuid))


@app.route(f'/{API_ROUTE}/{OBJECT}/<uuid:uuid>')
def get_product_by_uuid(uuid):
    match = mongo_helper.get_object_by_uuid(COLLECTION, uuid)
    if match:
        return jsonify(match[0])
    return make_response(jsonify({"message": "No match found"}), 404)


@app.route(f'/{API_ROUTE}/{COLLECTION}', methods=['GET'])
def get_products():
    return jsonify(mongo_helper.get_all_in_collection(COLLECTION))


@app.route(f'/{API_ROUTE}/{COLLECTION}/type/<string:type>')
def get_products_by_type(type):
    return jsonify(mongo_helper.get_objects_by_attribute(COLLECTION, 'type', type))


@app.route(f'/{API_ROUTE}/{COLLECTION}/provider/<string:provider>')
def get_products_by_provider(provider):
    return jsonify(mongo_helper.get_objects_by_attribute(COLLECTION, 'provider', provider))


