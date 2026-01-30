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

import json
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import TYPE_CHECKING, Optional

from sqlalchemy import (
    BigInteger,
    Boolean,
    Float,
    ForeignKey,
    Index,
    Numeric,
    String,
    Text,
    event,
    func,
)
from sqlalchemy import (
    Enum as SqlalchemyEnum,
)
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utc import UtcDateTime

from webapp.common.json import DefaultJSONEncoder
from webapp.extensions import db

from .base import BaseModel, Point
from .location_image import LocationImageAssociation

if TYPE_CHECKING:
    from .business import Business
    from .evse import Evse
    from .exceptional_closing_period import ExceptionalClosingPeriod
    from .exceptional_opening_period import ExceptionalOpeningPeriod
    from .image import Image
    from .regular_hours import RegularHours


class ParkingType(Enum):
    ALONG_MOTORWAY = 'ALONG_MOTORWAY'
    PARKING_GARAGE = 'PARKING_GARAGE'
    PARKING_LOT = 'PARKING_LOT'
    ON_DRIVEWAY = 'ON_DRIVEWAY'
    ON_STREET = 'ON_STREET'
    UNDERGROUND_GARAGE = 'UNDERGROUND_GARAGE'
    PRIVATE = 'PRIVATE'


class Facility(Enum):
    HOTEL = 'HOTEL'
    RESTAURANT = 'RESTAURANT'
    CAFE = 'CAFE'
    MALL = 'MALL'
    SUPERMARKET = 'SUPERMARKET'
    SPORT = 'SPORT'
    RECREATION_AREA = 'RECREATION_AREA'
    NATURE = 'NATURE'
    MUSEUM = 'MUSEUM'
    BIKE_SHARING = 'BIKE_SHARING'
    BUS_STOP = 'BUS_STOP'
    TAXI_STAND = 'TAXI_STAND'
    TRAM_STOP = 'TRAM_STOP'
    METRO_STATION = 'METRO_STATION'
    TRAIN_STATION = 'TRAIN_STATION'
    AIRPORT = 'AIRPORT'
    PARKING_LOT = 'PARKING_LOT'
    CARPOOL_PARKING = 'CARPOOL_PARKING'
    FUEL_STATION = 'FUEL_STATION'
    WIFI = 'WIFI'


class EnergySourceCategory(Enum):
    NUCLEAR = 'NUCLEAR'
    GENERAL_FOSSIL = 'GENERAL_FOSSIL'
    COAL = 'COAL'
    GAS = 'GAS'
    GENERAL_GREEN = 'GENERAL_GREEN'
    SOLAR = 'SOLAR'
    WIND = 'WIND'
    WATER = 'WATER'


class EnvironmentalImpactCategory(Enum):
    NUCLEAR_WASTE = 'NUCLEAR_WASTE'
    CARBON_DIOXIDE = 'CARBON_DIOXIDE'


# The TokenType Enum is just for documentation purposes, in public databases, this will never be set
class TokenType(Enum):
    AD_HOC_USER = 'AD_HOC_USER'
    APP_USER = 'APP_USER'
    OTHER = 'OTHER'
    RFID = 'RFID'


class Location(BaseModel):
    __tablename__ = 'location'
    __table_args__ = (
        Index('uid_source', 'uid', 'source'),
        Index('geometry_index', 'geometry', postgresql_using='gist'),
    )

    evses: Mapped[list['Evse']] = relationship(
        'Evse',
        back_populates='location',
        cascade='all, delete, delete-orphan',
    )
    images: Mapped[list['Image']] = relationship(
        'Image',
        secondary=LocationImageAssociation.__table__,
        back_populates='locations',
    )

    exceptional_openings: Mapped[list['ExceptionalOpeningPeriod']] = relationship(
        'ExceptionalOpeningPeriod',
        back_populates='location',
        cascade='all, delete, delete-orphan',
    )
    exceptional_closings: Mapped[list['ExceptionalClosingPeriod']] = relationship(
        'ExceptionalClosingPeriod',
        back_populates='location',
        cascade='all, delete, delete-orphan',
    )
    regular_hours: Mapped[list['RegularHours']] = relationship(
        'RegularHours',
        back_populates='location',
        cascade='all, delete, delete-orphan',
    )

    operator_id: Mapped[int | None] = mapped_column(
        BigInteger,
        ForeignKey('business.id', use_alter=True),
        nullable=True,
        index=True,
    )
    suboperator_id: Mapped[int | None] = mapped_column(
        BigInteger,
        ForeignKey('business.id', use_alter=True),
        nullable=True,
        index=True,
    )
    owner_id: Mapped[int | None] = mapped_column(
        BigInteger,
        ForeignKey('business.id', use_alter=True),
        nullable=True,
        index=True,
    )

    operator: Mapped[Optional['Business']] = relationship('Business', foreign_keys=[operator_id])
    suboperator: Mapped[Optional['Business']] = relationship('Business', foreign_keys=[suboperator_id])
    owner: Mapped[Optional['Business']] = relationship('Business', foreign_keys=[owner_id])

    uid: Mapped[str] = mapped_column(String(255), index=True, nullable=False)  # OCHP: locationId   OCPI: id
    source: Mapped[str] = mapped_column(String(64), index=True, nullable=False)

    dynamic_location_id: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    dynamic_location_probability: Mapped[float | None] = mapped_column(Float, nullable=True)

    name: Mapped[str | None] = mapped_column(String(255), nullable=True)  # OCHP: locationName, OCPI: name
    # OCHP: chargePointAddress.address, OCPI: address
    address: Mapped[str | None] = mapped_column(String(255), nullable=True)
    # OCHP: chargePointAddress.zipCode, OCPI: postal_code
    postal_code: Mapped[str | None] = mapped_column(String(255), nullable=True)
    city: Mapped[str | None] = mapped_column(String(255), nullable=True)  # OCHP: chargePointAddress.city, OCPI: city
    state: Mapped[str | None] = mapped_column(String(255), nullable=True)  # OCPI: state
    # OCHP: chargePointAddress.country, OCPI: country
    country: Mapped[str | None] = mapped_column(String(3), nullable=True)
    # OCHP: chargePointLocation.lat, OCPI: coordinates.latitude
    lat: Mapped[Decimal | None] = mapped_column(Numeric(9, 7), nullable=True)
    # OCHP: chargePointLocation.lon, OCPI: coordinates.longitude
    lon: Mapped[Decimal | None] = mapped_column(Numeric(10, 7), nullable=True)

    _directions: Mapped[str | None] = mapped_column('directions', Text, nullable=True)  # OCPI: directions
    parking_type: Mapped[ParkingType | None] = mapped_column(SqlalchemyEnum(ParkingType), nullable=True)
    time_zone: Mapped[str | None] = mapped_column(String(32), nullable=True)  # OCHP: timeZone, OCPI: time_zone

    last_updated: Mapped[datetime | None] = mapped_column(UtcDateTime(), nullable=True, index=True)  # OCHP: timestamp

    terms_and_conditions: Mapped[str | None] = mapped_column(String(255), nullable=True)  # OCPI: terms_and_conditions
    # OCHP: openingTimes.twentyfourseven    OCPI: opening_times.twentyfourseven
    twentyfourseven: Mapped[bool | None] = mapped_column(Boolean, nullable=True)

    geometry: Mapped[Point] = mapped_column(Point(), nullable=False)

    @hybrid_property
    def directions(self) -> list[dict[str, str]] | None:
        if self._directions is None:
            return None

        return json.loads(self._directions)

    @directions.setter
    def directions(self, directions: list[dict[str, str]] | None) -> None:
        if directions is None:
            self._directions = None
            return
        self._directions = json.dumps(directions, cls=DefaultJSONEncoder)

    def to_dict(self, *args, strict: bool = False, ignore: list[str] | None = None, **kwargs) -> dict:
        ignore = ignore or []

        ignore += [
            'id',
            'uid',
            'giroe_id',
            'source',
            'operator_id',
            'owner_id',
            'suboperator_id',
            'created',
            'modified',
            'geometry',
            'lat',
            'lon',
            'twentyfourseven',
            'directions',
            'created',
            'modified',
            'dynamic_location_id',
            'dynamic_location_probability',
        ]

        result = super().to_dict(ignore=ignore, **kwargs)

        # OCPI id has to be a string
        result['id'] = str(self.id)

        # We just handle public locations
        result['publish'] = True

        if not strict:
            result['original_id'] = self.uid
            result['source'] = self.source

        # Additional fields which are not automatically in our result
        result['directions'] = self.directions

        if self.twentyfourseven is not None:
            result['opening_times'] = {'twentyfourseven': self.twentyfourseven}

        result['coordinates'] = {
            'latitude': self.lat,
            'longitude': self.lon,
        }

        # TODO: remove this after migration period
        if not strict:
            result['coordinates']['lat'] = self.lat
            result['coordinates']['lon'] = self.lon

        return result


@event.listens_for(Location, 'before_insert')
@event.listens_for(Location, 'before_update')
def set_geometry(mapper, connection, location):
    lat_history = db.inspect(location).attrs.lat.history
    lon_history = db.inspect(location).attrs.lon.history

    # just update when there are changes in lat or lon
    if (
        (lat_history[0] and len(lat_history[0]))
        or (lat_history[2] and len(lat_history[2]))
        or (lon_history[0] and len(lon_history[0]))
        or (lon_history[2] and len(lon_history[2]))
    ):
        if connection.dialect.name == 'postgresql':
            location.geometry = func.ST_SetSRID(func.ST_MakePoint(float(location.lon), float(location.lat)), 4326)
        else:
            location.geometry = func.GeomFromText('POINT(%s %s)' % (float(location.lon), float(location.lat)))
