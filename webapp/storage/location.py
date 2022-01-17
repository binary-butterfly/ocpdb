# encoding: utf-8

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

from enum import Enum
from sqlalchemy import event, func, Index
from sqlalchemy_utc import UtcDateTime
from datetime import datetime, timezone
from typing import Union, Optional, List
from .base import BaseModel, Point
from webapp.extensions import db


class ParkingType(Enum):
    ALONG_MOTORWAY = 1 << 0
    PARKING_GARAGE = 1 << 1
    PARKING_LOT = 1 << 2
    ON_DRIVEWAY = 1 << 3
    ON_STREET = 1 << 4
    UNDERGROUND_GARAGE = 1 << 5


location_image = db.Table(
    'location_image',
    db.Column('location_id', db.BigInteger, db.ForeignKey('location.id')),
    db.Column('image_id', db.BigInteger, db.ForeignKey('image.id'))
)


class Location(db.Model, BaseModel):
    __tablename__ = "location"
    __table_args__ = (
        Index('uid_source', 'uid', 'source'),
    )

    uid = db.Column(db.String(255))            # OCHP: locationId                      OCPI: id
    source = db.Column(db.String(64), index=True)

    exceptional_openings = db.relationship(
        'ExceptionalPeriod',
        lazy='dynamic',
        primaryjoin="and_(Location.id==ExceptionalPeriod.location_id, ExceptionalPeriod.type=='opening')",
        cascade="all, delete-orphan",
    )
    exceptional_closings = db.relationship(
        'ExceptionalPeriod',
        lazy='dynamic',
        primaryjoin="and_(Location.id==ExceptionalPeriod.location_id, ExceptionalPeriod.type=='closing')",
        overlaps='exceptional_openings',
        cascade="all, delete-orphan",
    )
    regular_hours = db.relationship(
        'RegularHours',
        backref='chargepoint',
        lazy='dynamic',
        cascade="all, delete-orphan",
    )

    chargepoints = db.relationship(
        'Chargepoint',
        backref='location',
        lazy='dynamic',
        cascade="all, delete-orphan",
    )
    images = db.relationship("Image", secondary=location_image, backref=db.backref('locations', lazy='dynamic'))
    operator_id = db.Column(db.BigInteger, db.ForeignKey('business.id'))
    suboperator_id = db.Column(db.BigInteger, db.ForeignKey('business.id'))
    owner_id = db.Column(db.BigInteger, db.ForeignKey('business.id'))

    name = db.Column(db.String(255))                        # OCHP: locationName, OCPI: name
    address = db.Column(db.String(255))                     # OCHP: chargePointAddress.address      OCPI: address
    postal_code = db.Column(db.String(255))                 # OCHP: chargePointAddress.zipCode      OCPI: postal_code
    city = db.Column(db.String(255))                        # OCHP: chargePointAddress.city         OCPI: city
    state = db.Column(db.String(255))                       #                                       OCPI: state
    country = db.Column(db.String(2))                       # OCHP: chargePointAddress.country      OCPI: country_code
    lat = db.Column(db.Numeric(9, 7))                       # OCHP: chargePointLocation.lat         OCPI: coordinates.latitude
    lon = db.Column(db.Numeric(10, 7))                      # OCHP: chargePointLocation.lon         OCPI: coordinates.longitude

    directions = db.Column(db.Text)                         #                                       OCPI: directions
    parking_type = db.Column(db.Enum(ParkingType, name='ParkingType'))
    time_zone = db.Column(db.String(32))                    # OCHP: timeZone                        OCPI: time_zone

    _last_updated = db.Column('last_updated', UtcDateTime(timezone=True))    # OCHP: timestamp

    terms_and_conditions = db.Column(db.String(255))        #                                       OCPI: terms_and_conditions
    twentyfourseven = db.Column(db.Boolean)                 # OCHP: openingTimes.twentyfourseven    OCPI: opening_times.twentyfourseven

    geometry = db.Column(Point(), nullable=False)

    def _get_last_updated(self) -> Union[datetime, None]:
        if not self._last_updated:
            return None
        return self._last_updated.replace(tzinfo=timezone.utc)

    def _set_last_updated(self, last_updated: Optional[datetime] = None) -> None:
        self._last_updated = last_updated

    last_updated = db.synonym('_last_updated', descriptor=property(_get_last_updated, _set_last_updated))

    def to_dict(self,
                fields: Optional[List[str]] = None,
                ignore: Optional[List[str]] = None,
                transform_ocpi: bool = False) -> dict:
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
        return result


@event.listens_for(Location, 'before_insert')
@event.listens_for(Location, 'before_update')
def set_geometry(mapper, connection, location):
    location.geometry = func.GeomFromText('POINT(%s %s)' % (float(location.lat), float(location.lon)))

