import mongoengine
from planeador_eventos_api.settings import DATABASES

mongoengine.connect('default', username='root', password='password', host='mongodb://mongodb_container:27017/admin', alias='default')