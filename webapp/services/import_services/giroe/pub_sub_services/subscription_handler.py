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

from datetime import datetime, timezone

from butterfly_pubsub import PubSubMessage
from butterfly_pubsub.giroe import ChargeConnectorStatus
from butterfly_pubsub.sync import PubSubSubscriber

from webapp.common.config import ConfigHelper
from webapp.common.logger import Logger
from webapp.dependencies import dependencies
from webapp.repositories import EvseRepository, ObjectNotFoundException
from webapp.services.import_services.giroe.giroe_mapper import GiroeMapper


class PubSubStatusSubscriptionHandler(PubSubSubscriber):
    logger: Logger
    giroe_mapper: GiroeMapper
    evse_repository: EvseRepository
    pattern = 'CONNECTOR.*.STATUS'

    def __init__(self, logger: Logger, config_helper: ConfigHelper, evse_repository: EvseRepository):
        self.logger = logger
        self.config_helper = config_helper
        self.evse_repository = evse_repository
        self.giroe_mapper = GiroeMapper(config_helper=config_helper)

    def handle_message(self, message: PubSubMessage) -> None:
        self.logger = dependencies.get_logger()
        channel_fragments = message['channel'].decode().split('.')

        # ignore invalid messages
        if len(channel_fragments) != 3:
            return

        object_uid = channel_fragments[1]
        connector_status_string = message['data'].decode().upper()

        if connector_status_string not in ChargeConnectorStatus.__members__:
            self.logger.info(
                'import-giroe',
                f'Got invalid status {connector_status_string} for evse {object_uid}',
            )
            return

        evse_status = self.giroe_mapper.map_charge_connector_status_to_evse_status(
            ChargeConnectorStatus[connector_status_string],
        )
        # We need to reset the session to remove cached EVSE ORM data. In SQLAlchemy 2.0, this can be done using
        # `session.reset()`.
        self.evse_repository.session.expunge_all()
        self.evse_repository.session.close()

        try:
            evse = self.evse_repository.fetch_by_uid('giroe', uid=object_uid)
        except ObjectNotFoundException:
            # There are a lot of EVSEs which are either not public or not part of the TCC
            return

        # No status update required if it's the same status
        if evse_status == evse.status:
            return

        self.logger.info(
            'import-giroe',
            f'evse {object_uid} got status update from {evse.status.name} to {evse_status.name}'
        )

        evse.status = evse_status
        evse.last_updated = datetime.now(tz=timezone.utc)

        self.evse_repository.save_evse(evse)
