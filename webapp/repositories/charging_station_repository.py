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
from sqlalchemy.orm.interfaces import LoaderOption
from validataclass_search_queries.pagination import PaginatedResult
from validataclass_search_queries.search_queries import BaseSearchQuery

from webapp.common.sqlalchemy import Query
from webapp.models import Connector, Evse, Location, Tariff, TariffAssociation
from webapp.models.charging_station import ChargingStation

from .base_repository import BaseRepository
from .exceptions import ObjectNotFoundException


class ChargingStationRepository(BaseRepository[ChargingStation]):
    model_cls = ChargingStation

    @staticmethod
    def _children_options() -> list[LoaderOption]:
        """
        Eager-loads everything the charging station mapper renders. Connectors render the uids of their tariffs,
        falling back to the ones of their EVSE, so both tariff chains are loaded too: otherwise every connector would
        lazy-load its tariff associations, its EVSE's tariff associations and each tariff separately. Just the uid of
        the tariffs is needed, so their large JSON columns are not loaded.
        """
        evse_load = selectinload(ChargingStation.evses)
        return [
            evse_load.selectinload(Evse.connectors),
            evse_load.selectinload(Evse.images),
            evse_load.selectinload(Evse.tariff_associations).joinedload(TariffAssociation.tariff).load_only(Tariff.uid),
            evse_load
            .selectinload(Evse.connectors)
            .selectinload(Connector.tariff_associations)
            .joinedload(TariffAssociation.tariff)
            .load_only(Tariff.uid),
            selectinload(ChargingStation.images),
        ]

    def fetch_charging_station_by_id(
        self, charging_station_id: int, *, include_children: bool = False
    ) -> ChargingStation:
        query = self.session.query(ChargingStation)

        if include_children:
            query = query.options(*self._children_options())

        result = query.filter(ChargingStation.id == charging_station_id).first()

        if result is None:
            raise ObjectNotFoundException(message=f'charging station with id {charging_station_id} not found')

        return result

    def fetch_charging_stations(self, search_query: BaseSearchQuery | None = None) -> PaginatedResult[ChargingStation]:
        query = self.session.query(ChargingStation).options(*self._children_options())
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

        location_filters = []
        if source_uid := getattr(search_query, 'source_uid', None):
            location_filters.append(Location.source == source_uid)
        if source_uids := getattr(search_query, 'source_uids', None):
            location_filters.append(Location.source.in_(source_uids))
        if exclude_source_uid := getattr(search_query, 'exclude_source_uid', None):
            location_filters.append(Location.source != exclude_source_uid)
        if exclude_source_uids := getattr(search_query, 'exclude_source_uids', None):
            location_filters.append(Location.source.notin_(exclude_source_uids))
        location_id = getattr(search_query, 'location_id', None)

        # Join the location just once, however many filters need it: joining the same table twice fails. As this is a
        # many-to-one join, it doesn't multiply the charging station rows.
        if location_filters:
            query = query.join(Location, Location.id == ChargingStation.location_id).filter(*location_filters)
        if location_id:
            query = query.filter(ChargingStation.location_id == location_id)

        return query
