"""
Giro-e creditcard connect
Copyright (c) 2023, binary butterfly GmbH
All rights reserved.
"""

from butterfly_pubsub.asyncio import PubSubClient

from webapp.repositories import EvseRepository
from webapp.services.base_service import BaseService
from .subscriber import PubSubSubscriber


class PubSubService(BaseService):
    subscriber: PubSubSubscriber
    pubsub_client: PubSubClient

    def __init__(
        self,
        evse_repository: EvseRepository,
        pubsub_client: PubSubClient,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.pubsub_client = pubsub_client
        self.subscriber = PubSubSubscriber(
            logger=self.logger,
            event_helper=self.event_helper,
            evse_repository=evse_repository,
        )

    def register(self):
        self.pubsub_client.register(self.subscriber)

    def listen_for_updates(self):
        self.pubsub_client.process_messages()
