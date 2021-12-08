from flask import request, jsonify, Response

from api.helper.json_encoder import JSONEncoder
from api.app import API_ROUTE, app, mongo_helper

OBJECT = 'service'
COLLECTION = 'services'


@app.route(f'/{API_ROUTE}/{OBJECT}/create', methods=['POST'])
def create_service():
    inserted = mongo_helper.insert_one(COLLECTION, request.json)
    json_response = JSONEncoder(ensure_ascii=False).encode(inserted)
    return Response(json_response, status=200, mimetype="application/json")


@app.route(f'/{API_ROUTE}/{OBJECT}/update/<uuid:uuid>', methods=['PUT'])
def update_service(uuid):
    return jsonify(mongo_helper.update_one(COLLECTION, request.json, uuid))


@app.route(f'/{API_ROUTE}/{OBJECT}/<uuid:uuid>')
def get_service_by_uuid(uuid):
    return jsonify(mongo_helper.get_object_by_uuid(COLLECTION, uuid))


@app.route(f'/{API_ROUTE}/{COLLECTION}', methods=['GET'])
def get_services():
    return jsonify(mongo_helper.get_all_in_collection(COLLECTION))


@app.route(f'/{API_ROUTE}/{COLLECTION}/type/<string:type>')
def get_services_by_type(type):
    return jsonify(mongo_helper.get_objects_by_attribute(COLLECTION, 'type', type))


@app.route(f'/{API_ROUTE}/{COLLECTION}/provider/<string:provider>')
def get_services_by_provider(provider):
    return jsonify(mongo_helper.get_objects_by_attribute(COLLECTION, 'provider', provider))


@app.route(f'/{API_ROUTE}/{COLLECTION}/nearby/<string:long>/<string:lat>')
def get_services_nearby(long, lat):
    long = float(long)
    lat = float(lat)
    services = mongo_helper.get_collection('services')
    results = list(services.find(
        {'long_lat': {'$near': {'$geometry': {'type': "Point", 'coordinates': [long, lat]}, '$maxDistance': 15000}}}))
    for service in results:
        service.pop('_id')
    return jsonify(results)
