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

from validataclass_search_queries.pagination import PaginatedResult
from validataclass_search_queries.search_queries import BaseSearchQuery

from webapp.common.sqlalchemy import Query
from webapp.models import Connector, Evse, Location
from webapp.models.charging_station import ChargingStation

from .base_repository import BaseRepository
from .exceptions import ObjectNotFoundException


class ConnectorRepository(BaseRepository[Connector]):
    model_cls = Connector

    def fetch_by_id(self, connector_id: int) -> Connector:
        return self.fetch_resource_by_id(connector_id)

    def fetch_connector_by_id(self, connector_id: int) -> Connector:
        result = self.session.query(Connector).filter(Connector.id == connector_id).first()

        if result is None:
            raise ObjectNotFoundException(message=f'connector with id {connector_id} not found')

        return result

    def fetch_connectors(self, search_query: BaseSearchQuery | None = None) -> PaginatedResult[Connector]:
        query = self.session.query(Connector)
        return self._search_and_paginate(query, search_query)

    def _filter_by_search_query(self, query: Query, search_query: BaseSearchQuery | None) -> Query:
        if search_query is None:
            return query

        for _param_name, bound_filter in search_query.get_search_filters():
            if _param_name in [
                'source_uid',
                'source_uids',
                'exclude_source_uid',
                'exclude_source_uids',
                'evse_id',
                'location_id',
            ]:
                continue

            query = self._apply_bound_search_filter(query, bound_filter)

        if source_uid := getattr(search_query, 'source_uid', None):
            query = (
                query
                .join(Evse, Evse.id == Connector.evse_id)
                .join(ChargingStation, ChargingStation.id == Evse.charging_station_id)
                .join(Location, Location.id == ChargingStation.location_id)
                .filter(Location.source == source_uid)
            )

        if source_uids := getattr(search_query, 'source_uids', None):
            query = (
                query
                .join(Evse, Evse.id == Connector.evse_id)
                .join(ChargingStation, ChargingStation.id == Evse.charging_station_id)
                .join(Location, Location.id == ChargingStation.location_id)
                .filter(Location.source.in_(source_uids))
            )

        if exclude_source_uid := getattr(search_query, 'exclude_source_uid', None):
            query = (
                query
                .join(Evse, Evse.id == Connector.evse_id)
                .join(ChargingStation, ChargingStation.id == Evse.charging_station_id)
                .join(Location, Location.id == ChargingStation.location_id)
                .filter(Location.source != exclude_source_uid)
            )

        if exclude_source_uids := getattr(search_query, 'exclude_source_uids', None):
            query = (
                query
                .join(Evse, Evse.id == Connector.evse_id)
                .join(ChargingStation, ChargingStation.id == Evse.charging_station_id)
                .join(Location, Location.id == ChargingStation.location_id)
                .filter(Location.source.notin_(exclude_source_uids))
            )

        if evse_id := getattr(search_query, 'evse_id', None):
            query = query.filter(Connector.evse_id == evse_id)

        if location_id := getattr(search_query, 'location_id', None):
            query = (
                query
                .join(Evse, Evse.id == Connector.evse_id)
                .join(ChargingStation, ChargingStation.id == Evse.charging_station_id)
                .filter(ChargingStation.location_id == location_id)
            )

        return query

    def fetch_connectors_by_ids(self, connector_ids: list[int]) -> list[Connector]:
        return self.session.query(Connector).filter(Connector.id.in_(connector_ids)).all()

    def fetch_by_uid(self, source: str, connector_uid: str) -> Connector:
        result = (
            self.session
            .query(Connector)
            .filter(Connector.uid == connector_uid)
            .join(Evse, Evse.id == Connector.evse_id)
            .join(ChargingStation, ChargingStation.id == Evse.charging_station_id)
            .join(Location, Location.id == ChargingStation.location_id)
            .filter(Location.source == source)
            .first()
        )

        return self._or_raise(result, f'connector with uid {connector_uid} and source {source} not found')
