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
from abc import ABC

from butterfly_pubsub import PubSubMessage
from butterfly_pubsub.sync import PubSubSubscriber as PubSubSubscriberParent

from webapp.common.logger import Logger
from webapp.models.evse import EvseStatus
from webapp.repositories import ObjectNotFoundException
from webapp.dependencies import dependencies
from webapp.shared.evse.evse_mapper import EvseMapper


class PubSubSubscriber(PubSubSubscriberParent, ABC):
    logger: Logger
    evse_mapper: EvseMapper = EvseMapper()
    pattern = 'CONNECTOR.*.STATUS'

    def __init__(self):
        self.evse_repository = dependencies.get_evse_repository()

    def handle_message(self, message: PubSubMessage) -> None:
        self.logger = dependencies.get_logger()
        channel_fragments = message['channel'].decode().split('.')

        # ignore invalid messages
        if len(channel_fragments) != 3:
            return

        object_uid = channel_fragments[1]
        status = self.evse_mapper.map_charge_connector_status_to_evse_status(message['data'].decode().upper())
        try:

            evse = self.evse_repository.fetch_only_by_uid(uid=object_uid)
        except ObjectNotFoundException:
            self.logger.info('redis-pub-sub', f'unknown evse {object_uid} got status update to {status}')
            return

        try:
            evse_status: EvseStatus = status
        except KeyError:
            self.logger.info('redis-pub-sub', f' evse {object_uid} unknown status {status}')
            return
        self.logger.info(
            'redis-pub-sub',
            f'evse {object_uid} got status update from {object_uid} to {status}', )
        if status == evse.status:
            return
        evse.status = evse_status

        self.evse_repository.save_evse(evse)

