import uuid
from mongoengine import Document, StringField, UUIDField, BooleanField
from rest_framework_mongoengine.fields import GeoJSONField

class Service(Document):
    uuid = UUIDField(primary_key=True, default=uuid.uuid4)
    provider = UUIDField()
    name = StringField(max_length=200, blank=False, default='')
    description = StringField(max_length=200, blank=False, default='')
    type = StringField(max_length=200, blank=False, default='')
    image = StringField(max_length=200, blank=False, default='')
    provincia = StringField(max_length=200, blank=False, default='')
    canton = StringField(max_length=200, blank=False, default='')
    is_active = BooleanField(default=True)
    long_lat = GeoJSONField(geo_type="Point")

