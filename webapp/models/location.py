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
from typing import Optional, List, TYPE_CHECKING

from sqlalchemy import event, func, Index
from sqlalchemy_utc import UtcDateTime

from webapp.common.sqlalchemy import Col, Rel
from webapp.extensions import db
from .base import BaseModel, Point

if TYPE_CHECKING:
    from .evse import Evse
    from .image import Image
    from .regular_hours import RegularHours
    from .exceptional_opening_period import ExceptionalOpeningPeriod
    from .exceptional_closing_period import ExceptionalClosingPeriod
    from .business import Business


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


location_image = db.Table(
    'location_image',
    db.Column('location_id', db.BigInteger, db.ForeignKey('location.id', use_alter=True), nullable=False),
    db.Column('image_id', db.BigInteger, db.ForeignKey('image.id', use_alter=True), nullable=False)
)


class Location(db.Model, BaseModel):
    __tablename__ = "location"
    __table_args__ = (
        Index('uid', 'source'),
    )

    uid: Col[str] = db.Column(db.String(255), index=True,
                              nullable=False)  # OCHP: locationId                      OCPI: id
    source: Col[str] = db.Column(db.String(64), index=True, nullable=False)

    evses: Rel[List['Evse']] = db.relationship('Evse', back_populates='location', cascade="all, delete, delete-orphan")
    images: Rel[List['Image']] = db.relationship("Image", secondary=location_image)

    exceptional_openings: Rel[List['ExceptionalOpeningPeriod']] = db.relationship(
        'ExceptionalOpeningPeriod',
        back_populates='location',
        cascade="all, delete, delete-orphan",
    )
    exceptional_closings: Rel[List['ExceptionalClosingPeriod']] = db.relationship(
        'ExceptionalClosingPeriod',
        back_populates='location',
        cascade="all, delete, delete-orphan",
    )
    regular_hours: Rel[List['RegularHours']] = db.relationship(
        'RegularHours',
        back_populates='location',
        cascade="all, delete, delete-orphan",
    )

    operator_id: Col[int] = db.Column(db.BigInteger, db.ForeignKey('business.id', use_alter=True))
    suboperator_id: Col[int] = db.Column(db.BigInteger, db.ForeignKey('business.id', use_alter=True))
    owner_id: Col[int] = db.Column(db.BigInteger, db.ForeignKey('business.id', use_alter=True))

    operator: Rel['Business'] = db.relationship('Business', foreign_keys=[operator_id])
    suboperator: Rel['Business'] = db.relationship('Business', foreign_keys=[suboperator_id])
    owner: Rel['Business'] = db.relationship('Business', foreign_keys=[owner_id])

    dynamic_location_id: Col[int] = db.Column(db.BigInteger)  # TODO: relation?
    dynamic_location_probability: Col[int] = db.Column(db.Float)

    name: Col[str] = db.Column(db.String(255))  # OCHP: locationName, OCPI: name
    address: Col[str] = db.Column(db.String(255))  # OCHP: chargePointAddress.address      OCPI: address
    postal_code: Col[str] = db.Column(db.String(255))  # OCHP: chargePointAddress.zipCode      OCPI: postal_code
    city: Col[str] = db.Column(db.String(255))  # OCHP: chargePointAddress.city         OCPI: city
    state: Col[str] = db.Column(db.String(255))  # OCPI: state
    country: Col[str] = db.Column(db.String(2))  # OCHP: chargePointAddress.country      OCPI: country_code
    lat: Col[Decimal] = db.Column(db.Numeric(9, 7))  # OCHP: chargePointLocation.lat         OCPI: coordinates.latitude
    lon: Col[Decimal] = db.Column(
        db.Numeric(10, 7))  # OCHP: chargePointLocation.lon         OCPI: coordinates.longitude

    directions: Col[str] = db.Column(db.Text)  # OCPI: directions
    parking_type: Col[ParkingType] = db.Column(db.Enum(ParkingType))
    time_zone: Col[str] = db.Column(db.String(32))  # OCHP: timeZone                        OCPI: time_zone

    last_updated: Col[datetime] = db.Column(UtcDateTime())  # OCHP: timestamp

    terms_and_conditions: Col[str] = db.Column(db.String(255))  # OCPI: terms_and_conditions
    twentyfourseven: Col[bool] = db.Column(
        db.Boolean)  # OCHP: openingTimes.twentyfourseven    OCPI: opening_times.twentyfourseven

    geometry = db.Column(Point(), nullable=False)

    def to_dict(
            self,
            fields: Optional[List[str]] = None,
            ignore: Optional[List[str]] = None,
            search_result: Optional[bool] = True,
            transform_ocpi: bool = False,

    ) -> dict:
        result = super().to_dict(fields, ignore)
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
        if search_result:
            del result['geometry']
            result['images'] = self.images
            result['operator'] = self.operator
            result['evses'] = self.evses
            result['exceptional_openings'] = self.exceptional_openings
            result['exceptional_closings'] = self.exceptional_closings
            result['regular_hours'] = self.regular_hours
            result['operator'] = self.operator
            if self.operator is not None:
                result['operator_logo'] = self.operator.logo
            result['suboperator'] = self.suboperator
            if self.suboperator is not None:
                result['suboperator_logo'] = self.suboperator.logo
            result['owner'] = self.owner
            if self.owner is not None:
                result['owner_logo'] = self.owner.logo
            result['connectors'] = [connector for evse in self.evses for connector in evse.connectors]
            result['evse_images'] = [image for evse in self.evses for image in evse.evse_images]
            result['related_resources'] = [related for evse in self.evses for related in evse.related_resources]

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
        location.geometry = func.GeomFromText('POINT(%s %s)' % (float(location.lat), float(location.lon)))
