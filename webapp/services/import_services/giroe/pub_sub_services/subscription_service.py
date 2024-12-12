"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2024 binary butterfly GmbH

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from butterfly_pubsub.sync import PubSubClient

from webapp.models.source import SourceStatus
from webapp.repositories import EvseRepository, ObjectNotFoundException, SourceRepository
from webapp.services.base_service import BaseService

from .subscription_handler import PubSubStatusSubscriptionHandler


class PubSubService(BaseService):
    source_repository: SourceRepository
    evse_repository: EvseRepository

    def __init__(
        self,
        pubsub_client: PubSubClient,
        source_repository: SourceRepository,
        evse_repository: EvseRepository,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.source_repository = source_repository
        self.pubsub_client = pubsub_client
        self.evse_repository = evse_repository

    def register(self):
        self.pubsub_client.register(
            PubSubStatusSubscriptionHandler(
                logger=self.logger,
                config_helper=self.config_helper,
                evse_repository=self.evse_repository,
            ),
        )

    def listen_for_updates(self):
        try:
            source = self.source_repository.fetch_source_by_uid('giroe')
        except ObjectNotFoundException:
            self.logger.warn('import-giroe', 'You cannot use the pubsub service before importing static data')
            return

        if source.static_status != SourceStatus.ACTIVE:
            self.logger.warn('import-giroe', f'Wrong source status {source.static_status} for importing realtime data')
            return

        # Set source realtime status active
        source.realtime_status = SourceStatus.ACTIVE
        self.source_repository.save_source(source)

        self.pubsub_client.process_messages()
