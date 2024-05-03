"""
Giro-e creditcard connect
Copyright (c) 2023, binary butterfly GmbH
All rights reserved.
"""

from butterfly_pubsub.asyncio import PubSubClient

from webapp.repositories import EvseRepository
from webapp.services.base_service import BaseService
from .subscriber import PubSubSubscriber
from webapp.dependencies import dependencies
from ...common.config import ConfigHelper
from ...common.events import EventHelper, event_helper
from ...common.logger import Logger


class PubSubService(BaseService):

    def __init__(
        self,
        evse_repository: EvseRepository,
        pubsub_client: PubSubClient,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.event_helper = dependencies.get_event_helper()
        self.pubsub_client = pubsub_client
        self.subscriber = PubSubSubscriber(
            logger=self.logger,
            config_helper=self.config_helper,
            event_helper=self.event_helper,
            evse_repository=evse_repository,
        )

    def register(self):
        self.pubsub_client.register(self.subscriber)

    def listen_for_updates(self):
        self.pubsub_client.process_messages()
