"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2021 binary butterfly GmbH

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

from typing import List

from webapp.models import Connector, Evse, Location
from .base_repository import BaseRepository, ObjectNotFoundException


class ConnectorRepository(BaseRepository[Connector]):
    model_cls = Connector

    def fetch_by_id(self, connector_id: int) -> Connector:
        result = self.session.query(Connector).get(connector_id)
        if result is None:
            raise ObjectNotFoundException(f'connector with id {connector_id} not found')
        return result

    def fetch_connectors_by_ids(self, connector_ids: List[int]) -> List[Connector]:
        return self.session.query(Connector)\
            .filter(Connector.id.in_(connector_ids))\
            .all()

    def fetch_connectors_by_evse_ids(self, evse_ids: List[int]) -> List[Connector]:
        return self.session.query(Connector)\
            .filter(Connector.chargepoint_id.in_(evse_ids))\
            .all()

    def fetch_by_uid(self, source: str, connector_uid: str) -> Connector:
        result = self.session.query(Connector)\
            .filter(Connector.uid == connector_uid)\
            .join(Evse, Evse.id == Connector.evse_id)\
            .join(Location, Location.id == Evse.location_id)\
            .filter(Location.source == source)\
            .first()

        if result is None:
            raise ObjectNotFoundException(message=f'connector with uid {connector_uid} and source {source} not found')

        return result

    def delete_connector_by_id(self, connector_ids: List[int]):
        self.session.query(Connector)\
            .filter(Connector.id.in_(connector_ids))\
            .delete(synchronize_session=False)

    def delete_connector_by_ids(self, connector_id: int):
        self.session.query(Connector)\
            .filter(Connector.id == connector_id)\
            .delete(synchronize_session=False)
