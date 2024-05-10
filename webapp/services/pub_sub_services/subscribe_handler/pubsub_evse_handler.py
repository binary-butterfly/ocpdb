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

from webapp.models.evse import EvseStatus
from webapp.repositories import ObjectNotFoundException, EvseRepository
from webapp.services.pub_sub_services.subscribe_handler.pubsub_base_handler import PubSubBaseHandler


class PubSubEvseHandler(PubSubBaseHandler):
    evse_repository: EvseRepository

    def __init__(self, *, evse_repository: EvseRepository, **kwargs):
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
