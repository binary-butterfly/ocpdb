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
from sqlalchemy import func, or_, text
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.orm.interfaces import LoaderOption
from validataclass_search_queries.filters import BoundSearchFilter
from validataclass_search_queries.pagination import PaginatedResult
from validataclass_search_queries.search_queries import BaseSearchQuery

from webapp.common.sqlalchemy import Query
from webapp.models import Business, Evse, Location
from webapp.models.charging_station import ChargingStation

from .base_repository import BaseRepository


class LocationRepository(BaseRepository[Location]):
    model_cls = Location

    def fetch_locations_by_source(self, source: str, include_children: bool = True) -> list[Location]:
        query = self.session.query(Location)

        if include_children:
            query = query.options(
                selectinload(Location.charging_pool).selectinload(ChargingStation.evses).selectinload(Evse.connectors),
                selectinload(Location.operator),
            )

        return query.filter(Location.source == source).all()

    def fetch_location_ids_by_source(self, source: str) -> list[int]:
        items = self.session.query(Location.id).filter(Location.source == source).all()

        return [item.id for item in items]

    def fetch_location_by_id(self, location_id: int, *, include_children: bool = False) -> Location:
        load_options: list[LoaderOption] = []
        if include_children:
            load_options += [
                joinedload(Location.operator),
                selectinload(Location.charging_pool).selectinload(ChargingStation.evses).selectinload(Evse.connectors),
            ]

        return self.fetch_resource_by_id(location_id, load_options=load_options)

    def fetch_location_by_uid(self, source: str, location_uid: str, *, include_children: bool = False) -> Location:
        query = self.session.query(Location)

        if include_children:
            cs_load = selectinload(Location.charging_pool)
            query = query.options(
                cs_load.selectinload(ChargingStation.evses).selectinload(Evse.connectors),
                selectinload(Location.operator).selectinload(Business.logo),
                selectinload(Location.suboperator).selectinload(Business.logo),
                selectinload(Location.owner).selectinload(Business.logo),
                selectinload(Location.images),
                cs_load.selectinload(ChargingStation.evses).selectinload(Evse.images),
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
            'LEFT JOIN charging_station ON charging_station.location_id = location.id '
            'LEFT JOIN evse ON evse.charging_station_id = charging_station.id '
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
        cs_load = selectinload(Location.charging_pool)
        options = [
            joinedload(Location.operator).joinedload(Business.logo),
            joinedload(Location.suboperator).joinedload(Business.logo),
            joinedload(Location.owner).joinedload(Business.logo),
            selectinload(Location.images),
            cs_load.selectinload(ChargingStation.evses).selectinload(Evse.connectors),
            cs_load.selectinload(ChargingStation.evses).selectinload(Evse.images),
        ]

        query = self.session.query(Location).options(*options)
        return self._search_and_paginate(query, search_query)

    def _filter_by_search_query(self, query: Query, search_query: BaseSearchQuery | None) -> Query:
        if search_query is None:
            return query

        for _param_name, bound_filter in search_query.get_search_filters():
            if _param_name in [
                'lat',
                'lon',
                'radius',
                'lat_min',
                'lat_max',
                'lon_min',
                'lon_max',
                'last_updated_since',
            ]:
                continue

            query = self._apply_bound_search_filter(query, bound_filter)

        if last_updated_since := getattr(search_query, 'last_updated_since', None):
            query = (
                query
                .join(Location.charging_pool)
                .join(ChargingStation.evses)
                .filter(or_(Location.last_updated >= last_updated_since, Evse.last_updated >= last_updated_since))
                .distinct()
            )

        if (
            getattr(search_query, 'lat', None)
            and getattr(search_query, 'lon', None)
            and getattr(search_query, 'radius', None)
        ):
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

        if (
            getattr(search_query, 'lat_min', None)
            and getattr(search_query, 'lat_max', None)
            and getattr(search_query, 'lon_min', None)
            and getattr(search_query, 'lon_max', None)
        ):
            query = query.filter(
                func.ST_Within(
                    Location.geometry,
                    func.ST_MakeEnvelope(
                        getattr(search_query, 'lon_min'),
                        getattr(search_query, 'lat_min'),
                        getattr(search_query, 'lon_max'),
                        getattr(search_query, 'lat_max'),
                        4326,
                    ),
                ),
            )

        return query

    def _apply_bound_search_filter(self, query: Query, bound_filter: BoundSearchFilter) -> Query:
        """
        Extends the base _apply_bound_search_filter() method to implement model specific search filters.
        """
        if bound_filter.param_name == 'operator_name':
            return query.join(Location.operator).filter(Business.name.like(f'%{bound_filter.value}%'))

        return super()._apply_bound_search_filter(query, bound_filter)
