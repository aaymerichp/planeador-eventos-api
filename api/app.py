from flask import Flask
from flask_uuid import FlaskUUID
from flask_cors import CORS

from api.db.mongo_helper import MongoHelper
from api.constants import MONGO_URI

app = Flask(__name__)
CORS(app)

app.config["MONGO_URI"] = MONGO_URI
app.config['JSON_AS_ASCII'] = False

mongo_helper = MongoHelper(app)

flask_uuid = FlaskUUID()
flask_uuid.init_app(app)

import api.routes.events
import api.routes.invoices
import api.routes.payments
import api.routes.products
import api.routes.providers
import api.routes.reports
import api.routes.services
import api.routes.subscriptions
import api.routes.users

if __name__ == '__main__':
    app.run(host='0.0.0.0')
