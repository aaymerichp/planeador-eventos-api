from flask import Flask
from flask_uuid import FlaskUUID


from api.db.mongo_helper import MongoHelper
from api.db.constants import MONGO_URI

app = Flask(__name__)
API_ROUTE = 'planeador_eventos_api'

app.config["MONGO_URI"] = MONGO_URI
app.config['JSON_AS_ASCII'] = False

mongo_helper = MongoHelper(app)
flask_uuid = FlaskUUID()
flask_uuid.init_app(app)

import api.routes.services

if __name__ == '__main__':
    app.run(host='0.0.0.0')
