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

from mercantile import LngLatBbox
from sqlalchemy import func
from webapp.models import Location, Evse, Business
from sqlalchemy.orm import selectinload
from .base_repository import BaseRepository, ObjectNotFoundException


class LocationRepository(BaseRepository):

    def fetch_locations_by_source(self, source: str, include_children: bool = True) -> List[Location]:
        locations = self.session.query(Location)

        if include_children:
            locations = locations.options([
                selectinload(Location.evses).selectinload(Evse.connectors),
                selectinload(Location.operator),
            ])

        return locations.filter(Location.source == source).all()

    def fetch_location_ids_by_source(self, source: str) -> List[int]:
        items = self.session.query(Location.id).filter(Location.source == source).all()

        return [item.id for item in items]

    def fetch_location_by_id(self, location_id: int, *, include_children: bool = False) -> Location:
        location = self.session.query(Location)

        if include_children:
            location = location.options([
                selectinload(Location.evses).selectinload(Evse.connectors),
                selectinload(Location.operator),

            ])

        location = location.get(location_id)

        if location is None:
            raise ObjectNotFoundException(message=f'location with id {location_id} not found')

        return location

    def fetch_location_by_uid(self, source: str, location_uid: str, *, include_children: bool = False) -> Location:
        location = self.session.query(Location)
        if include_children:
            location = location.options([
                selectinload(Location.evses).selectinload(Evse.connectors),
                selectinload(Location.operator).selectinload(Business.logo),
                selectinload(Location.suboperator).selectinload(Business.logo),
                selectinload(Location.owner).selectinload(Business.logo),
                selectinload(Location.images),
                selectinload(Location.evses).selectinload(Evse.images),
            ])

        location = location.filter(Location.uid == location_uid).first()

        if location is None:
            raise ObjectNotFoundException(message=f'location with uid {location_uid} and source {source} not found')

        return location

    def save_location(self, location: Location, *, commit: bool = True):
        self.session.add(location)
        if commit:
            self.session.commit()

    def fetch_locations_summary_by_bounds(self, bbox: LngLatBbox, static: bool = False):
        query = """
        SELECT location.id, location.lat, location.lon, location.name, location.address, 
            COUNT(evse.id) as chargepoint_count, 
            SUM(CASE WHEN evse.status = 'AVAILABLE' THEN 1 ELSE 0 END) as chargepoint_available_count, 
            SUM(CASE WHEN evse.status = 'UNKNOWN' THEN 1 ELSE 0 END) as chargepoint_unknown_count,
            SUM(CASE WHEN evse.status = 'STATIC' THEN 1 ELSE 0 END) as chargepoint_static_count,
            SUM(CASE WHEN evse.parking_restrictions & 64 = 64 THEN 1 ELSE 0 END) as chargepoint_bike_count
        FROM location 
        LEFT JOIN evse ON evse.location_id = location.id
        WHERE MBRContains(GeomFromText('LINESTRING(%s %s, %s %s)'), location.geometry)
            %s
        GROUP BY location.id
        """ % (
            bbox[1] - (0.5 * (bbox[3] - bbox[1])),
            bbox[0] - (0.5 * (bbox[2] - bbox[0])),
            bbox[3] + (0.5 * (bbox[3] - bbox[1])),
            bbox[2] + (0.5 * (bbox[2] - bbox[0])),
            '' if static is None else "AND evse.status %s 'STATIC'" % ('=' if static is True else '!=')
        )
        return self.session.execute(query)

    def fetch_locations_by_bounds(self, bbox: LngLatBbox) -> List[Location]:
        line_string = f'LINESTRING({bbox[1] - (0.5 * (bbox[3] - bbox[1]))} {bbox[0] - (0.5 * (bbox[2] - bbox[0]))}, ' \
                      f'{bbox[3] + (0.5 * (bbox[3] - bbox[1]))} {bbox[2] + (0.5 * (bbox[2] - bbox[0]))})'

        locations = self.session.query(Location)\
            .filter(func.MBRContains(func.GeomFromText(line_string), Location.geometry))\
            .filter(Location.source != 'bnetza')\
            .all()

        return locations

    def delete_location(self, location: Location, *, commit: bool = True):
        self.session.delete(location)
        if commit:
            self.session.commit()
