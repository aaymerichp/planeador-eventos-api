from uuid import UUID

from api.app import mongo_helper

class ServicesController():
    def __init__(self, service):
        self.service = service

    def get_services_in_events_by_provider_uuid(self, provider_uuid):
        return_services = []
        events = mongo_helper.get_objects_by_attribute('events', 'services.provider', provider_uuid)
        for event in events:
            for service in event.get('services'):
                if service.get('provider') == provider_uuid:
                    if event.get('services'):
                        event.pop('services')
                    service['event'] = event
                    if event.get('user'):
                        service['user'] = mongo_helper.get_object_by_uuid('users', UUID(event.get('user')))
                    return_services.append(service)
        if return_services:
            return return_services