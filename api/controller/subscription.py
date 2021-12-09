from uuid import UUID

from api.app import mongo_helper

class SubscriptionController():
    def __init__(self, subscription):
        self.subscription = subscription

    def set_subscription_in_provider(self) -> dict:
        # TODO: TEST MORE
        provider_uuid = self.subscription.get('provider')
        provider = mongo_helper.get_object_by_uuid('providers', UUID(provider_uuid))
        print(provider)
        provider['subscription'] = self.subscription
        updated_provider = mongo_helper.update_one('providers', provider, UUID(provider_uuid))
        print(updated_provider)
        return(self.subscription)
