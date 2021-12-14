from typing import Union
from flask import Flask
from flask_pymongo import PyMongo
from pymongo.collection import Collection
from uuid import uuid4

class MongoHelper():
    def __init__(self, app: Flask):
        mongodb_client = PyMongo(app)
        self.db = mongodb_client.db

    def get_collection(self, collection: str) -> Collection:
        return getattr(self.db, collection)

    def get_all_in_collection(self, collection: str) -> list:
        services = self.get_collection(collection)
        results = list(services.find({}))
        for service in results:
            service.pop('_id')
        return results

    def get_object_by_uuid(self, collection: str, uuid: str) -> dict:
        collection = self.get_collection(collection)
        result = collection.find_one({'uuid': uuid})
        if result:
            result.pop('_id')
            return result

    def get_objects_by_attribute(self, collection: str, attribute: str, filter: Union[str, list]) -> list:
        collection = self.get_collection(collection)
        results = list(collection.find({attribute: filter}))
        for service in results:
            service.pop('_id')
        return results

    def insert_one(self, collection: str, object: dict) -> dict:
        collection = self.get_collection(collection)
        content = {'uuid': uuid4()}
        content.update(object)
        inserted = collection.insert_one(content)
        if inserted:
            content.pop('_id')
            return content

    def update_one(self, collection: str, object: dict, uuid: str):
        collection = self.get_collection(collection)
        new_values = {"$set": object}
        updated = collection.update_one({'uuid': uuid}, new_values)
        if updated:
            print(uuid)
            result = collection.find_one({'uuid': uuid})
            if result:
                result.pop('_id')
                return result
