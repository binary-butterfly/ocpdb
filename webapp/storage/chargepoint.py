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
from datetime import datetime, timezone
from typing import List, Union, Optional
from .base import BaseModel
from ..extensions import db


class ChargepointStatus(Enum):
    AVAILABLE = 'AVAILABLE'
    BLOCKED = 'BLOCKED'
    CHARGING = 'CHARGING'
    INOPERATIVE = 'INOPERATIVE'
    OUTOFORDER = 'OUTOFORDER'
    PLANNED = 'PLANNED'
    REMOVED = 'REMOVED'
    RESERVED = 'RESERVED'
    UNKNOWN = 'UNKNOWN'


class ParkingRestriction(Enum):
    EV_ONLY = 1 << 0
    PLUGGED = 1 << 1
    DISABLED = 1 << 2
    CUSTOMERS = 1 << 3
    MOTORCYCLES = 1 << 4
    CARSHARING = 1 << 5
    BICYCLE_ONLY = 1 << 6


class Capability(Enum):
    CHARGING_PROFILE_CAPABLE = 1 << 0
    CHARGING_PREFERENCES_CAPABLE = 1 << 1
    CHIP_CARD_SUPPORT = 1 << 2
    CONTACTLESS_CARD_SUPPORT = 1 << 3
    CREDIT_CARD_PAYABLE = 1 << 4
    DEBIT_CARD_PAYABLE = 1 << 5
    PED_TERMINAL = 1 << 6
    REMOTE_START_STOP_CAPABLE = 1 << 7
    RESERVABLE = 1 << 8
    RFID_READER = 1 << 9
    TOKEN_GROUP_CAPABLE = 1 << 10
    UNLOCK_CAPABLE = 1 << 11
    PUBLIC = 1 << 12
    LOCAL_KEY = 1 << 13
    CASH = 1 << 14
    IEC15118 = 1 << 15
    DIRECT_REMOTE = 1 << 16


chargepoint_image = db.Table(
    'chargepoint_image',
    db.Column('chargepoint_id', db.BigInteger, db.ForeignKey('chargepoint.id')),
    db.Column('image_id', db.BigInteger, db.ForeignKey('image.id'))
)


class Chargepoint(db.Model, BaseModel):
    __tablename__ = "chargepoint"

    connectors = db.relationship('Connector', backref='chargepoint', lazy='dynamic')
    images = db.relationship("Image", secondary=chargepoint_image, backref=db.backref('chargepoint', lazy='dynamic'))
    related_resource = db.relationship('RelatedResource', backref='chargepoint', lazy='dynamic')
    location_id = db.Column(db.BigInteger, db.ForeignKey('location.id'))
    external_id = db.Column(db.BigInteger)
    uid = db.Column(db.String(64))
    giroe_id = db.Column(db.BigInteger)

    evse_id = db.Column(db.String(64))

    status = db.Column(db.Enum(ChargepointStatus, name='ChargepointStatus'))

    lat = db.Column(db.Numeric(9, 7))
    lon = db.Column(db.Numeric(10, 7))

    floor_level = db.Column(db.String(16))
    physical_reference = db.Column(db.String(255))
    directions = db.Column(db.Text)
    phone = db.Column(db.String(255))                       # OCHP: telephoneNumber

    parking_uid = db.Column(db.String(255))                 # OCHP: parkingSpot.parkingId
    parking_floor_level = db.Column(db.String(255))         # OCHP: parkingSpot.floorlevel
    parking_spot_number = db.Column(db.String(255))         # OCHP: parkingSpot.parkingSpotNumber

    _last_updated = db.Column('last_updated', db.DateTime(timezone=True))
    max_reservation = db.Column(db.Float)                   # OCHP maxReservation
    _capabilities = db.Column('capabilities', db.Integer)   #                                           OCPI: capability
    _parking_restrictions = db.Column('parking_restrictions', db.Integer)   # OCHP: RestrictionType     OCPI: parking_restrictions

    terms_and_conditions = db.Column(db.String(255))        #                                           OCPI: terms_and_conditions

    # status_schedule TODO
    # user_interface_lang TODO                              # OCHP userInterfaceLang

    def _get_capabilities(self) -> List[Capability]:
        if not self._capabilities:
            return []
        return sorted(
            [item for item in list(Capability) if item.value & self._capabilities],
            key=lambda item: item.value
        )

    def _set_capabilities(self, capabilities: List[Capability]) -> None:
        self._capabilities = 0
        for capability in capabilities:
            self._capabilities = self._capabilities | capability.value

    capabilities = db.synonym('_capabilities', descriptor=property(_get_capabilities, _set_capabilities))

    def _get_last_updated(self) -> Union[datetime, None]:
        if not self._last_updated:
            return None
        return self._last_updated.replace(tzinfo=timezone.utc)

    def _set_last_updated(self, last_updated: Optional[datetime] = None) -> None:
        self._last_updated = last_updated

    last_updated = db.synonym('_last_updated', descriptor=property(_get_last_updated, _set_last_updated))

    def _get_parking_restrictions(self) -> List[ParkingRestriction]:
        if not self._parking_restrictions:
            return []
        return sorted(
            [item for item in list(ParkingRestriction) if item.value & self._parking_restrictions],
            key=lambda item: item.value
        )

    def _set_parking_restrictions(self, parking_restrictions: List[ParkingRestriction]) -> None:
        self._parking_restrictions = 0
        for parking_restriction in parking_restrictions:
            self._parking_restrictions = self._parking_restrictions | parking_restriction.value

    parking_restrictions = db.synonym(
        '_parking_restrictions',
        descriptor=property(_get_parking_restrictions, _set_parking_restrictions)
    )

    def to_dict(self,
                fields: Optional[List[str]] = None,
                ignore: Optional[List[str]] = None,
                transform_ocpi: bool = False) -> dict:
        result = super().to_dict(fields, ignore)
        return result
