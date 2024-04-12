"""
Giro-e creditcard connect
Copyright (c) 2023, binary butterfly GmbH
All rights reserved.
"""

from butterfly_pubsub.asyncio import PubSubClient

from webapp.repositories import EvseRepository
from webapp.services.base_service import BaseService
from .subscriber import PubSubSubscriber
from ...common.config import ConfigHelper
from ...common.events import EventHelper


class PubSubService(BaseService):
    subscriber: PubSubSubscriber
    pubsub_client: PubSubClient
    evse_repository: EvseRepository

    def __init__(
        self,
        evse_repository: EvseRepository,
        pubsub_client: PubSubClient,
        event_helper: EventHelper,
        config_helper: ConfigHelper,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.pubsub_client = pubsub_client
        self.subscriber = PubSubSubscriber(
            logger=self.logger,
            event_helper=event_helper,
            config_helper=config_helper,
            evse_repository=evse_repository,
        )

    def register(self):
        self.pubsub_client.register(self.subscriber)

    def listen_for_updates(self):
        self.pubsub_client.process_messages()
