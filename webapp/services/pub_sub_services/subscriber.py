"""
Giro-e OCPI
Copyright (c) 2024, binary butterfly GmbH
All rights reserved.
"""

from typing import Dict

from butterfly_pubsub import PubSubMessage
from butterfly_pubsub.sync import PubSubSubscriber as PubSubSubscriberParent

from webapp.common.config import ConfigHelper
from webapp.common.events import EventHelper
from webapp.common.logger import Logger
from webapp.models.evse import EvseStatus
from webapp.repositories import EvseRepository, ObjectNotFoundException, evse_repository
from webapp.services.pub_sub_services.subscribe_handler.pubsub_base_handler import PubSubBaseHandler
from webapp.services.pub_sub_services.subscribe_handler.pubsub_evse_handler import PubSubEvseHandler


class PubSubSubscriber(PubSubSubscriberParent):
    evse_repository: EvseRepository
    event_helper: EventHelper
    logger: Logger
    handler: Dict[str, PubSubBaseHandler]

    pattern = '*.*.STATUS'

    def __init__(
            self,
            logger: Logger,
            event_helper: EventHelper,
            config_helper: ConfigHelper,
    ):
        self.handler = {
            'CONNECTOR': PubSubEvseHandler(
                event_helper=event_helper,
                logger=logger,
                config_helper=config_helper,
                evse_repository=evse_repository,
            ),
        }

    def handle_message(self, message: PubSubMessage) -> None:
        channel_fragments = message['channel'].decode().split('.')

        # ignore invalid messages
        if len(channel_fragments) != 3:
            return

        message_type = channel_fragments[0]
        object_uid = channel_fragments[1]
        value = message['data'].decode().upper()
        try:
            evse = self.evse_repository.fetch_evse_uids()
        except ObjectNotFoundException:
            self.logger.info('redis-pub-sub', f'unknown evse {object_uid} got status update to {value}')
            return

        try:
            evse_status: EvseStatus = EvseStatus[value]
        except KeyError:
            self.logger.info('redis-pub-sub', f' evse {object_uid} unknown status {value}')
            return
        self.logger.info(
            'redis-pub-sub',
            f'evse {object_uid} got status update from {evse.status.name} to {value}', )
        if evse_status == evse.status:
            return
        evse.status = evse_status
        self.evse_repository.save_evse(evse)

        # Discard unsupported message types
        if message_type not in self.handler:
            return

        self.handler[message_type].handle(object_uid, value)
