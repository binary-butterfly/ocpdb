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

from datetime import datetime

from mercantile import LngLatBbox
from sqlalchemy import Row, func, select, text, union
from sqlalchemy.orm import aliased, joinedload, selectinload
from sqlalchemy.orm.interfaces import LoaderOption
from validataclass_search_queries.filters import BoundSearchFilter
from validataclass_search_queries.pagination import AbstractPaginationMixin, PaginatedResult
from validataclass_search_queries.search_queries import BaseSearchQuery

from webapp.common.sqlalchemy import Query
from webapp.models import Business, Connector, Evse, Location, Tariff, TariffAssociation
from webapp.models.charging_station import ChargingStation
from webapp.models.evse import PARKING_RESTRICTION_BIT_BY_MEMBER, EvseStatus, ParkingRestriction

from .base_repository import BaseRepository

# location id, location uid, location last_updated, charging station id, charging station uid,
# charging station last_updated, EVSE uid, EVSE status, EVSE last_updated, EVSE status_last_updated
RealtimeEvseRow = Row[tuple[int, str, datetime, int, str, datetime, str, EvseStatus, datetime, datetime | None]]


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
            # The OCPI location mappers render operator/suboperator/owner and walk the whole
            # charging_pool -> evses -> connectors/images tree plus charging_station images. Eager-load all of it so a
            # single location response does not fan out into N+1 queries across its stations, EVSEs and images.
            cs_load = selectinload(Location.charging_pool)
            evse_load = cs_load.selectinload(ChargingStation.evses)
            load_options += [
                joinedload(Location.operator),
                joinedload(Location.suboperator),
                joinedload(Location.owner),
                cs_load.selectinload(ChargingStation.images),
                evse_load.selectinload(Evse.connectors),
                evse_load.selectinload(Evse.images),
                # Connectors render the uids of their tariffs, falling back to the ones of their EVSE. Just the uid is
                # needed, so the large JSON columns of the tariffs are not loaded.
                evse_load
                .selectinload(Evse.tariff_associations)
                .joinedload(TariffAssociation.tariff)
                .load_only(Tariff.uid),
                evse_load
                .selectinload(Evse.connectors)
                .selectinload(Connector.tariff_associations)
                .joinedload(TariffAssociation.tariff)
                .load_only(Tariff.uid),
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

        location = query.filter(Location.source == source, Location.uid == location_uid).first()

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
            # Bound parameter instead of a literal: in PostgreSQL, "STATIC" in double quotes is a column reference.
            additional_where += f' AND evse.status {"=" if static is True else "!="} :static_status'
        if filter_duplicates:
            additional_where += ' AND location.dynamic_location_id IS NULL'

        query = (
            'SELECT location.id, location.lat, location.lon, location.name, location.address, '
            '  COUNT(evse.id) as chargepoint_count, '
            "  SUM(CASE WHEN evse.status = 'AVAILABLE' THEN 1 ELSE 0 END) as chargepoint_available_count, "
            "  SUM(CASE WHEN evse.status = 'UNKNOWN' THEN 1 ELSE 0 END) as chargepoint_unknown_count, "
            "  SUM(CASE WHEN evse.status = 'STATIC' THEN 1 ELSE 0 END) as chargepoint_static_count, "
            '  SUM(CASE WHEN evse.parking_restrictions & :bicycle_only_bit = :bicycle_only_bit THEN 1 ELSE 0 END) '
            '    as chargepoint_bike_count '
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

        return list(
            self.session.execute(
                text(query),
                {
                    'bicycle_only_bit': PARKING_RESTRICTION_BIT_BY_MEMBER[ParkingRestriction.BICYCLE_ONLY],
                    'static_status': EvseStatus.STATIC.name,
                },
            )
        )

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

    def fetch_locations(
        self,
        *,
        search_query: BaseSearchQuery | None = None,
        include_operators: bool = False,
        include_logos: bool = False,
        include_location_images: bool = False,
        include_charging_stations: bool = False,
        include_charging_station_images: bool = False,
        include_evses: bool = False,
        include_evse_images: bool = False,
        include_connectors: bool = False,
        include_evse_tariffs: bool = False,
        include_tariffs: bool = False,
    ) -> PaginatedResult[Location]:
        """
        include_evse_tariffs just loads the tariffs of the EVSEs, include_tariffs additionally loads the ones of the
        connectors, which are needed for Connector.tariff_uids.
        """

        options: list[LoaderOption] = []
        if include_logos:
            options.append(joinedload(Location.operator).joinedload(Business.logo))
            options.append(joinedload(Location.suboperator).joinedload(Business.logo))
            options.append(joinedload(Location.owner).joinedload(Business.logo))
        elif include_operators:
            options.append(joinedload(Location.operator))
            options.append(joinedload(Location.suboperator))
            options.append(joinedload(Location.owner))

        if include_connectors:
            options.append(
                selectinload(Location.charging_pool).selectinload(ChargingStation.evses).selectinload(Evse.connectors)
            )
        evse_load = selectinload(Location.charging_pool).selectinload(ChargingStation.evses)
        if include_tariffs:
            # Connectors render the uids of their own tariffs before falling back to the ones of their EVSE. Just the
            # uid is needed, so the large JSON columns of the tariffs are not loaded.
            options.append(
                evse_load
                .selectinload(Evse.tariff_associations)
                .selectinload(TariffAssociation.tariff)
                .load_only(Tariff.uid)
            )
            options.append(
                evse_load
                .selectinload(Evse.connectors)
                .selectinload(Connector.tariff_associations)
                .selectinload(TariffAssociation.tariff)
                .load_only(Tariff.uid)
            )
        elif include_evse_tariffs:
            options.append(evse_load.selectinload(Evse.tariff_associations).selectinload(TariffAssociation.tariff))

        if include_evses:
            options.append(selectinload(Location.charging_pool).selectinload(ChargingStation.evses))
        if include_charging_stations:
            options.append(selectinload(Location.charging_pool))

        if include_location_images:
            options.append(selectinload(Location.images))
        if include_charging_station_images:
            options.append(selectinload(Location.charging_pool).selectinload(ChargingStation.images))

        if include_evse_images:
            options.append(
                selectinload(Location.charging_pool).selectinload(ChargingStation.evses).selectinload(Evse.images)
            )

        query = self.session.query(Location).options(*options)
        return self._search_and_paginate(query, search_query)

    def fetch_realtime_evse_rows(self, *, search_query: BaseSearchQuery | None = None) -> list[RealtimeEvseRow]:
        """
        Fetches the data of realtime exports as plain rows instead of ORM objects. Building ORM objects for a full export
        of >100k EVSEs takes several seconds, while realtime exports just need a few columns:
        - Search filters, sorting and pagination apply to the locations, just like in fetch_locations(), but without the
          total count query, which would repeat the whole filter query.
        - EVSEs excluded by search_query.exclude_evse_status are not part of the result.
        - Locations without EVSEs in the result are not part of the result either.
        - The rows are ordered by location (in search query order), charging station and EVSE, so all rows of a location
          and of a charging station are consecutive.
        """
        location_id_query = self.session.query(Location.id)
        location_id_query = self._filter_by_search_query(location_id_query, search_query)
        # The id as tie-breaker, so pages are stable if the sorting column has duplicates
        location_id_query = self._order_by_search_query(location_id_query, search_query).order_by(Location.id)
        if isinstance(search_query, AbstractPaginationMixin):
            location_id_query = search_query.apply_pagination_to_query(location_id_query, self.model_cls)
        location_ids = location_id_query.subquery()

        query = (
            self.session
            .query(
                Location.id,
                Location.uid,
                Location.last_updated,
                ChargingStation.id,
                ChargingStation.uid,
                ChargingStation.last_updated,
                Evse.uid,
                Evse.status,
                Evse.last_updated,
                Evse.status_last_updated,
            )
            .join(location_ids, location_ids.c.id == Location.id)
            .join(ChargingStation, ChargingStation.location_id == Location.id)
            .join(Evse, Evse.charging_station_id == ChargingStation.id)
        )

        exclude_evse_status: list[EvseStatus] | None = getattr(search_query, 'exclude_evse_status', None)
        if exclude_evse_status:
            query = query.filter(Evse.status.notin_(exclude_evse_status))

        # Same location order as the paginated location ids, the ids keep the rows of a location together.
        query = self._order_by_search_query(query, search_query)
        query = query.order_by(Location.id, ChargingStation.id, Evse.id)

        return query.all()

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
                'evse_status',
                'exclude_evse_status',
                'evse_status_last_updated_since',
                'last_updated_since',
            ]:
                continue

            query = self._apply_bound_search_filter(query, bound_filter)

        last_updated_since = getattr(search_query, 'last_updated_since', None)
        evse_status_last_updated = getattr(search_query, 'evse_status_last_updated_since', None)
        evse_status = getattr(search_query, 'evse_status', None)
        exclude_evse_status = getattr(search_query, 'exclude_evse_status', None)

        evse_filters = []
        if evse_status_last_updated:
            evse_filters.append(Evse.status_last_updated >= evse_status_last_updated)
        if evse_status:
            evse_filters.append(Evse.status.in_(evse_status))
        if exclude_evse_status:
            evse_filters.append(Evse.status.notin_(exclude_evse_status))

        if evse_filters or last_updated_since:
            # EXISTS instead of JOIN + DISTINCT: DISTINCT had to sort the full join over all location columns (including
            # geometry and large text columns) before LIMIT could apply. As a semi-join, the planner can walk the
            # location primary key in order and stop at the limit.
            matching_evses = (
                select(Evse.id)
                .join(Evse.charging_station)
                .where(ChargingStation.location_id == Location.id, *evse_filters)
            )
            query = query.filter(matching_evses.exists())

        if last_updated_since:
            # Either the location or one of its matching EVSEs has been updated. As a UNION of two ID lists, both
            # parts can use their last_updated index, which is impossible for an OR across both tables.
            updated_location = aliased(Location)
            updated_location_ids = union(
                select(updated_location.id).where(updated_location.last_updated >= last_updated_since),
                select(ChargingStation.location_id)
                .join(ChargingStation.evses)
                .where(
                    # ChargingStation.last_updated >= last_updated_since,  # TODO: reactivate
                    Evse.last_updated >= last_updated_since,
                    *evse_filters,
                ),
            )
            query = query.filter(Location.id.in_(updated_location_ids))

        if (
            getattr(search_query, 'lat', None)
            and getattr(search_query, 'lon', None)
            and getattr(search_query, 'radius', None)
        ):
            if self.session.connection().dialect.name == 'postgresql':
                # ST_DWithin on geography instead of ST_DistanceSphere(...) < radius: the latter is a plain function
                # comparison the planner cannot index, so it seq-scanned every location. ST_DWithin adds the bounding
                # box operator that hits the gist index on (geometry::geography), see geography_index.
                # use_spheroid=False keeps this a sphere calculation, i.e. exactly the ST_DistanceSphere result.
                query = query.filter(
                    func.ST_DWithin(
                        func.geography(Location.geometry),
                        func.geography(
                            func.ST_SetSRID(
                                func.ST_MakePoint(float(search_query.lon), float(search_query.lat)),
                                4326,
                            ),
                        ),
                        search_query.radius,
                        False,
                    )
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
