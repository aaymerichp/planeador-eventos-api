from uuid import UUID

from api.app import mongo_helper

class ReportsController():
    def _get_all_events_matching_provider_uuid(self, provider_uuid):
        return

    def get_amount_for_services_in_events(self, provider_uuid,
                                          report_end_date, report_start_date=None):
        filter = {
            'services.provider': provider_uuid,
        }

        if report_start_date:
            filter['finish_time'] = {'$gt': report_start_date, '$lte': report_end_date}

        else:
            filter['finish_time'] = {'$lte': report_end_date}

        events = mongo_helper.get_objects_by_filter('events', filter)

        print(events)
        total_amount = 0
        for event in events:
            for service in event.get('services'):
                if service.get('provider') == provider_uuid:
                    total_amount += service.get('amount')

        return {'amount': total_amount}

    def get_count_services_in_events(self, provider_uuid):
        services = mongo_helper.get_objects_by_attribute('events', 'services.provider', provider_uuid)
        return {'services': len(services)}

    def get_count_pending_services_in_events(self, provider_uuid, current_date):
        filter = {
            'services.provider': provider_uuid,
            'services.payment_status': 'PAID',
            'finish_time': {'$lte': current_date}
        }
        pending_services  = mongo_helper.get_objects_by_filter('events', filter)

        return {'services': len(pending_services)}
