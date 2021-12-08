from flask_pymongo import PyMongo
from uuid import uuid4

class MongoHelper():
    def __init__(self, app):
        mongodb_client = PyMongo(app)
        self.db = mongodb_client.db

    def get_collection(self, collection):
        return getattr(self.db, collection)

    def get_all_in_collection(self, collection):
        services = self.get_collection(collection)
        results = list(services.find({}))
        for service in results:
            service.pop('_id')
        return results

    def get_object_by_uuid(self, collection, uuid):
        collection = self.get_collection(collection)
        results = list(collection.find({'uuid': uuid}))
        for service in results:
            service.pop('_id')
        return results[0]

    def get_objects_by_attribute(self, collection, attribute, filter):
        collection = self.get_collection(collection)
        results = list(collection.find({attribute: filter}))
        for service in results:
            service.pop('_id')
        return results

    def insert_one(self, collection, object):
        collection = self.get_collection(collection)
        content = {'uuid': uuid4()}
        content.update(object)
        inserted = collection.insert_one(content)
        if inserted:
            content.pop('_id')
            return content

    def update_one(self, collection, object, uuid):
        collection = self.get_collection(collection)
        new_values = {"$set": object}
        updated = collection.update_one({'uuid': uuid}, new_values)
        if updated:
            return object