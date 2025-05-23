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

from mercantile import LngLatBbox
from sqlalchemy import func, text
from sqlalchemy.orm import joinedload, selectinload
from validataclass_search_queries.pagination import PaginatedResult
from validataclass_search_queries.search_queries import BaseSearchQuery

from webapp.common.sqlalchemy import Query
from webapp.models import Business, Evse, Location

from .base_repository import BaseRepository
from .exceptions import ObjectNotFoundException


class LocationRepository(BaseRepository[Location]):
    model_cls = Location

    def fetch_locations_by_source(self, source: str, include_children: bool = True) -> list[Location]:
        query = self.session.query(Location)

        if include_children:
            query = query.options(
                selectinload(Location.evses).selectinload(Evse.connectors),
                selectinload(Location.operator),
            )

        return query.filter(Location.source == source).all()

    def fetch_location_ids_by_source(self, source: str) -> list[int]:
        items = self.session.query(Location.id).filter(Location.source == source).all()

        return [item.id for item in items]

    def fetch_location_by_id(self, location_id: int, *, include_children: bool = False) -> Location:
        location = self.session.query(Location)

        if include_children:
            location = location.options(
                selectinload(Location.evses).selectinload(Evse.connectors),
                selectinload(Location.operator),
            )

        location = location.get(location_id)

        if location is None:
            raise ObjectNotFoundException(message=f'location with id {location_id} not found')

        return location

    def fetch_location_by_uid(self, source: str, location_uid: str, *, include_children: bool = False) -> Location:
        query = self.session.query(Location)

        if include_children:
            query = query.options(
                selectinload(Location.evses).selectinload(Evse.connectors),
                selectinload(Location.operator).selectinload(Business.logo),
                selectinload(Location.suboperator).selectinload(Business.logo),
                selectinload(Location.owner).selectinload(Business.logo),
                selectinload(Location.images),
                selectinload(Location.evses).selectinload(Evse.images),
            )

        location = query.filter(Location.uid == location_uid).first()

        return self._or_raise(location, f'location with uid {location_uid} and source {source} not found')

    def save_location(self, location: Location, *, commit: bool = True):
        self._save_resources(location, commit=commit)

    def fetch_locations_summary_by_bounds(
        self,
        bbox: LngLatBbox,
        static: bool | None = None,
        filter_duplicates: bool = True,
    ) -> list:
        additional_where = ''
        if static is not None:
            additional_where += f'AND evse.status {"=" if static is True else "!="} "STATIC"'
        if filter_duplicates:
            additional_where += 'AND location.dynamic_location_id IS NULL'

        query = (
            'SELECT location.id, location.lat, location.lon, location.name, location.address, '
            '  COUNT(evse.id) as chargepoint_count, '
            "  SUM(CASE WHEN evse.status = 'AVAILABLE' THEN 1 ELSE 0 END) as chargepoint_available_count, "
            "  SUM(CASE WHEN evse.status = 'UNKNOWN' THEN 1 ELSE 0 END) as chargepoint_unknown_count, "
            "  SUM(CASE WHEN evse.status = 'STATIC' THEN 1 ELSE 0 END) as chargepoint_static_count, "
            '  SUM(CASE WHEN evse.parking_restrictions & 64 = 64 THEN 1 ELSE 0 END) as chargepoint_bike_count '
            'FROM location '
            'LEFT JOIN evse ON evse.location_id = location.id '
        )
        if self.session.connection().dialect.name == 'postgresql':
            query += (
                f'WHERE ST_Contains(ST_MakeEnvelope({self._get_postgre_envelope_bounds(bbox)}, '
                f'4326), location.geometry)'
            )
        else:
            query += f"WHERE MBRContains(GeomFromText('{self._get_linestring_bounds(bbox)}'), location.geometry) "

        query += f'{additional_where} GROUP BY location.id'

        return list(self.session.execute(text(query)))

    def fetch_locations_by_bounds(self, bbox: LngLatBbox) -> list[Location]:
        locations = self.session.query(Location)

        if self.session.connection().dialect.name == 'postgresql':
            locations = locations.filter(
                func.ST_Contains(
                    func.ST_MakeEnvelope(self._get_postgre_envelope_bounds(bbox), 4326), Location.geometry
                ),
            )
        else:
            locations = locations.filter(
                func.MBRContains(func.GeomFromText(self._get_linestring_bounds(bbox)), Location.geometry),
            )

        return locations.filter(Location.source != 'bnetza').all()

    @staticmethod
    def _get_linestring_bounds(bbox: LngLatBbox):
        return (
            f'LINESTRING({bbox[0] - (0.5 * (bbox[2] - bbox[0]))} {bbox[1] - (0.5 * (bbox[3] - bbox[1]))}, '
            f'{bbox[2] + (0.5 * (bbox[2] - bbox[0]))} {bbox[3] + (0.5 * (bbox[3] - bbox[1]))})'
        )

    @staticmethod
    def _get_postgre_envelope_bounds(bbox: LngLatBbox):
        return (
            f'{bbox[0] - (0.5 * (bbox[2] - bbox[0]))}, {bbox[1] - (0.5 * (bbox[3] - bbox[1]))}, '
            f'{bbox[2] + (0.5 * (bbox[2] - bbox[0]))}, {bbox[3] + (0.5 * (bbox[3] - bbox[1]))}'
        )

    def delete_location(self, location: Location, *, commit: bool = True):
        self.session.delete(location)
        if commit:
            self.session.commit()

    def fetch_locations(self, search_query: BaseSearchQuery | None = None) -> PaginatedResult[Location]:
        options = [
            selectinload(Location.images),
            selectinload(Location.evses).selectinload(Evse.connectors),
            selectinload(Location.evses).selectinload(Evse.images),
            joinedload(Location.operator).joinedload(Business.logo),
            joinedload(Location.suboperator).joinedload(Business.logo),
            joinedload(Location.owner).joinedload(Business.logo),
            selectinload(Location.evses).selectinload(Evse.related_resources),
            selectinload(Location.regular_hours),
            selectinload(Location.exceptional_closings),
            selectinload(Location.exceptional_openings),
        ]

        query = self.session.query(Location).options(*options)
        return self._search_and_paginate(query, search_query)

    def _filter_by_search_query(self, query: Query, search_query: BaseSearchQuery | None) -> Query:
        if search_query is None:
            return query

        for _param_name, bound_filter in search_query.get_search_filters():
            if _param_name in ['lat', 'lon', 'radius']:
                continue

            query = self._apply_bound_search_filter(query, bound_filter)

        if search_query.lat and search_query.lon and search_query.radius:
            if self.session.connection().dialect.name == 'postgresql':
                query = query.filter(
                    func.ST_DistanceSphere(
                        Location.geometry,
                        func.ST_GeomFromText(f'POINT({float(search_query.lon)} {float(search_query.lat)})'),
                    )
                    < search_query.radius
                )
            else:
                query = query.filter(
                    func.ST_Distance_Sphere(
                        Location.geometry,
                        func.ST_GeomFromText(f'POINT({float(search_query.lon)} {float(search_query.lat)})', 4326),
                    )
                    < search_query.radius
                )

        return query
