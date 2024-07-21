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
from decimal import Decimal
from enum import Enum
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import Index, event, func
from sqlalchemy_utc import UtcDateTime

from webapp.common.sqlalchemy import Mapped
from webapp.extensions import db

from .base import BaseModel, Point

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


location_image = db.Table(
    'location_image',
    db.Column('location_id', db.BigInteger, db.ForeignKey('location.id', use_alter=True), nullable=False),
    db.Column('image_id', db.BigInteger, db.ForeignKey('image.id', use_alter=True), nullable=False)
)


class Location(db.Model, BaseModel):
    __tablename__ = 'location'
    __table_args__ = (
        Index('uid', 'source'),
    )

    uid: Mapped[str] = db.Column(db.String(255), index=True,
                              nullable=False)  # OCHP: locationId                      OCPI: id
    source: Mapped[str] = db.Column(db.String(64), index=True, nullable=False)

    evses: Mapped[List['Evse']] = db.relationship('Evse', back_populates='location', cascade='all, delete, delete-orphan')
    images: Mapped[List['Image']] = db.relationship('Image', secondary=location_image)

    exceptional_openings: Mapped[List['ExceptionalOpeningPeriod']] = db.relationship(
        'ExceptionalOpeningPeriod',
        back_populates='location',
        cascade='all, delete, delete-orphan',
    )
    exceptional_closings: Mapped[List['ExceptionalClosingPeriod']] = db.relationship(
        'ExceptionalClosingPeriod',
        back_populates='location',
        cascade='all, delete, delete-orphan',
    )
    regular_hours: Mapped[List['RegularHours']] = db.relationship(
        'RegularHours',
        back_populates='location',
        cascade='all, delete, delete-orphan',
    )

    operator_id: Mapped[int] = db.Column(db.BigInteger, db.ForeignKey('business.id', use_alter=True))
    suboperator_id: Mapped[int] = db.Column(db.BigInteger, db.ForeignKey('business.id', use_alter=True))
    owner_id: Mapped[int] = db.Column(db.BigInteger, db.ForeignKey('business.id', use_alter=True))

    operator: Mapped['Business'] = db.relationship('Business', foreign_keys=[operator_id])
    suboperator: Mapped['Business'] = db.relationship('Business', foreign_keys=[suboperator_id])
    owner: Mapped['Business'] = db.relationship('Business', foreign_keys=[owner_id])

    dynamic_location_id: Mapped[int] = db.Column(db.BigInteger)  # TODO: relation?
    dynamic_location_probability: Mapped[int] = db.Column(db.Float)

    name: Mapped[str] = db.Column(db.String(255))  # OCHP: locationName, OCPI: name
    address: Mapped[str] = db.Column(db.String(255))  # OCHP: chargePointAddress.address      OCPI: address
    postal_code: Mapped[str] = db.Column(db.String(255))  # OCHP: chargePointAddress.zipCode      OCPI: postal_code
    city: Mapped[str] = db.Column(db.String(255))  # OCHP: chargePointAddress.city         OCPI: city
    state: Mapped[str] = db.Column(db.String(255))  # OCPI: state
    country: Mapped[str] = db.Column(db.String(2))  # OCHP: chargePointAddress.country      OCPI: country_code
    lat: Mapped[Decimal] = db.Column(db.Numeric(9, 7))  # OCHP: chargePointLocation.lat         OCPI: coordinates.latitude
    lon: Mapped[Decimal] = db.Column(db.Numeric(10, 7))  # OCHP: chargePointLocation.lon         OCPI: coordinates.longitude

    directions: Mapped[str] = db.Column(db.Text)  # OCPI: directions
    parking_type: Mapped[ParkingType] = db.Column(db.Enum(ParkingType))
    time_zone: Mapped[str] = db.Column(db.String(32))  # OCHP: timeZone                        OCPI: time_zone

    last_updated: Mapped[datetime] = db.Column(UtcDateTime())  # OCHP: timestamp

    terms_and_conditions: Mapped[str] = db.Column(db.String(255))  # OCPI: terms_and_conditions
    twentyfourseven: Mapped[bool] = db.Column(db.Boolean)  # OCHP: openingTimes.twentyfourseven    OCPI: opening_times.twentyfourseven

    geometry = db.Column(Point(), nullable=False)

    def to_dict(
        self,
        fields: Optional[List[str]] = None,
        ignore: Optional[List[str]] = None,
        transform_ocpi: bool = False,
    ) -> dict:
        result = super().to_dict(fields, ignore)

        if 'geometry' in result:
            del result['geometry']

        if transform_ocpi:
            del result['lat']
            del result['lon']
            del result['twentyfourseven']

            if self.twentyfourseven is not None:
                result['opening_times'] = {'twentyfourseven': self.twentyfourseven}

            result['coordinates'] = {
                'lat': self.lat,
                'lon': self.lon
            }
        return result


@event.listens_for(Location, 'before_insert')
@event.listens_for(Location, 'before_update')
def set_geometry(mapper, connection, location):
    lat_history = db.inspect(location).attrs.lat.history
    lon_history = db.inspect(location).attrs.lon.history

    # just update when there are changes in lat or lon
    if (lat_history[0] and len(lat_history[0])) \
            or (lat_history[2] and len(lat_history[2])) \
            or (lon_history[0] and len(lon_history[0])) \
            or (lon_history[2] and len(lon_history[2])):
        if connection.dialect.name == 'postgresql':
            location.geometry = func.ST_SetSRID(func.ST_MakePoint(float(location.lon), float(location.lat)), 4326)
        else:
            location.geometry = func.GeomFromText('POINT(%s %s)' % (float(location.lon), float(location.lat)))
