from uuid import UUID

from api.app import mongo_helper

class ServicesController():
    def __init__(self, service):
        self.service = service

    def get_services_in_events_by_provider_uuid(self, provider):
        return_events = []
        events = mongo_helper.get_all_in_collection('events')
        for event in events:
            for service in event.get('services'):
                if service.get('provider') == provider:
                    return_events.append(service)
        if return_events:
            return return_events