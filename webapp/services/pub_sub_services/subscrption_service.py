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

from webapp.services.base_service import BaseService
from .subscriber import PubSubSubscriber


class PubSubService(BaseService):

    def __init__(
        self,
        pubsub_client: PubSubClient,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.pubsub_client = pubsub_client
        self.subscriber = PubSubSubscriber()

    def register(self):
        self.pubsub_client.register(self.subscriber)

    def listen_for_updates(self):
        self.pubsub_client.process_messages()
