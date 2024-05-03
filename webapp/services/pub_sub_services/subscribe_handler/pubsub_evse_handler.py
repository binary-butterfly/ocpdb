"""
Giro-e OCPI
Copyright (c) 2024, binary butterfly GmbH
All rights reserved.
"""
from webapp.common.events import EventHelper
from webapp.models.evse import EvseStatus
from webapp.repositories import ObjectNotFoundException, EvseRepository
from webapp.services.pub_sub_services.subscribe_handler.pubsub_base_handler import PubSubBaseHandler


class PubSubEvseHandler(PubSubBaseHandler):
    evse_repository: EvseRepository

    def __init__(self, *, evse_repository: EvseRepository, event_helper: EventHelper, **kwargs):
        super().__init__(**kwargs)
        self.evse_repository = evse_repository

    def handle(self, object_uid: str, value: str):
        try:
            evse = self.evse_repository.fetch_by_id(object_uid)
        except ObjectNotFoundException:
            # If connector is not known to our system just do nothing
            self.logger.info('redis-pub-sub', f'unknown evse {object_uid} got status update to {value}')
            return

        try:
            evse_status = EvseStatus[value]
        except KeyError:
            # if connector status is not known in creditcard connect: do nothing
            self.logger.info('redis-pub-sub', f'evse {object_uid} got invalid status {value}')
            return

        self.logger.info(
            'redis-pub-sub',
            f'evse {object_uid} got status update from {evse.status.name} to {value}',
        )

        # if the connector status did not change: do nothing
        if evse_status == evse.status:
            return

        evse.status = evse_status
        self.evse_repository.save_evse(evse)
