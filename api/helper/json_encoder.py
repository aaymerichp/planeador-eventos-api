import json
from bson import ObjectId
from uuid import UUID

class JSONEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, UUID):
            return str(o)
        return json.JSONEncoder.default(self, o)

