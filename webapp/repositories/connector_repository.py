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

from webapp.models import Connector, Evse, Location

from .base_repository import BaseRepository


class ConnectorRepository(BaseRepository[Connector]):
    model_cls = Connector

    def fetch_by_id(self, connector_id: int) -> Connector:
        return self.fetch_resource_by_id(connector_id)

    def fetch_connectors_by_ids(self, connector_ids: list[int]) -> list[Connector]:
        return self.session.query(Connector).filter(Connector.id.in_(connector_ids)).all()

    def fetch_by_uid(self, source: str, connector_uid: str) -> Connector:
        result = (
            self.session.query(Connector)
            .filter(Connector.uid == connector_uid)
            .join(Evse, Evse.id == Connector.evse_id)
            .join(Location, Location.id == Evse.location_id)
            .filter(Location.source == source)
            .first()
        )

        return self._or_raise(result, f'connector with uid {connector_uid} and source {source} not found')
