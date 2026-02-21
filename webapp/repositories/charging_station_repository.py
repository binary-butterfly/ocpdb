"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2026 binary butterfly GmbH

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

from sqlalchemy.orm import selectinload
from validataclass_search_queries.pagination import PaginatedResult
from validataclass_search_queries.search_queries import BaseSearchQuery

from webapp.common.sqlalchemy import Query
from webapp.models import Evse, Location
from webapp.models.charging_station import ChargingStation

from .base_repository import BaseRepository
from .exceptions import ObjectNotFoundException


class ChargingStationRepository(BaseRepository[ChargingStation]):
    model_cls = ChargingStation

    def fetch_charging_station_by_id(
        self, charging_station_id: int, *, include_children: bool = False
    ) -> ChargingStation:
        query = self.session.query(ChargingStation)

        if include_children:
            query = query.options(
                selectinload(ChargingStation.evses).selectinload(Evse.connectors),
                selectinload(ChargingStation.evses).selectinload(Evse.images),
                selectinload(ChargingStation.images),
            )

        result = query.filter(ChargingStation.id == charging_station_id).first()

        if result is None:
            raise ObjectNotFoundException(message=f'charging station with id {charging_station_id} not found')

        return result

    def fetch_charging_stations(self, search_query: BaseSearchQuery | None = None) -> PaginatedResult[ChargingStation]:
        options = [
            selectinload(ChargingStation.evses).selectinload(Evse.connectors),
            selectinload(ChargingStation.evses).selectinload(Evse.images),
            selectinload(ChargingStation.images),
        ]

        query = self.session.query(ChargingStation).options(*options)
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
                'location_id',
            ]:
                continue

            query = self._apply_bound_search_filter(query, bound_filter)

        if source_uid := getattr(search_query, 'source_uid', None):
            query = query.join(Location, Location.id == ChargingStation.location_id).filter(
                Location.source == source_uid
            )

        if source_uids := getattr(search_query, 'source_uids', None):
            query = query.join(Location, Location.id == ChargingStation.location_id).filter(
                Location.source.in_(source_uids)
            )

        if exclude_source_uid := getattr(search_query, 'exclude_source_uid', None):
            query = query.join(Location, Location.id == ChargingStation.location_id).filter(
                Location.source != exclude_source_uid
            )

        if exclude_source_uids := getattr(search_query, 'exclude_source_uids', None):
            query = query.join(Location, Location.id == ChargingStation.location_id).filter(
                Location.source.notin_(exclude_source_uids)
            )

        if location_id := getattr(search_query, 'location_id', None):
            query = query.filter(ChargingStation.location_id == location_id)

        return query
