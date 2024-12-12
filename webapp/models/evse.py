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
from typing import TYPE_CHECKING, List

from sqlalchemy_utc import UtcDateTime

from webapp.common.sqlalchemy import Mapped
from webapp.extensions import db

from .base import BaseModel

if TYPE_CHECKING:
    from .connector import Connector
    from .image import Image
    from .location import Location
    from .related_resource import RelatedResource


class EvseStatus(Enum):
    AVAILABLE = 'AVAILABLE'
    BLOCKED = 'BLOCKED'
    CHARGING = 'CHARGING'
    INOPERATIVE = 'INOPERATIVE'
    OUTOFORDER = 'OUTOFORDER'
    PLANNED = 'PLANNED'
    REMOVED = 'REMOVED'
    RESERVED = 'RESERVED'
    UNKNOWN = 'UNKNOWN'
    STATIC = 'STATIC'  # will never have any live data


class ParkingRestriction(Enum):
    EV_ONLY = 'EV_ONLY'
    PLUGGED = 'PLUGGED'
    DISABLED = 'DISABLED'
    CUSTOMERS = 'CUSTOMERS'
    MOTORCYCLES = 'MOTORCYCLES'
    CARSHARING = 'CARSHARING'
    BICYCLE_ONLY = 'BICYCLE_ONLY'


class Capability(Enum):
    CHARGING_PROFILE_CAPABLE = 'CHARGING_PROFILE_CAPABLE'
    CHARGING_PREFERENCES_CAPABLE = 'CHARGING_PREFERENCES_CAPABLE'
    CHIP_CARD_SUPPORT = 'CHIP_CARD_SUPPORT'
    CONTACTLESS_CARD_SUPPORT = 'CONTACTLESS_CARD_SUPPORT'
    CREDIT_CARD_PAYABLE = 'CREDIT_CARD_PAYABLE'
    DEBIT_CARD_PAYABLE = 'DEBIT_CARD_PAYABLE'
    PED_TERMINAL = 'PED_TERMINAL'
    REMOTE_START_STOP_CAPABLE = 'REMOTE_START_STOP_CAPABLE'
    RESERVABLE = 'RESERVABLE'
    RFID_READER = 'RFID_READER'
    TOKEN_GROUP_CAPABLE = 'TOKEN_GROUP_CAPABLE'  # noqa: S105
    UNLOCK_CAPABLE = 'UNLOCK_CAPABLE'
    PUBLIC = 'PUBLIC'
    LOCAL_KEY = 'LOCAL_KEY'
    CASH = 'CASH'
    IEC15118 = 'IEC15118'
    DIRECT_REMOTE = 'DIRECT_REMOTE'


evse_image = db.Table(
    'evse_image',
    db.Column('evse_id', db.BigInteger, db.ForeignKey('evse.id', use_alter=True), nullable=False),
    db.Column('image_id', db.BigInteger, db.ForeignKey('image.id', use_alter=True), nullable=False),
)


class Evse(db.Model, BaseModel):
    __tablename__ = 'evse'

    connectors: Mapped[List['Connector']] = db.relationship(
        'Connector',
        back_populates='evse',
        cascade='all, delete, delete-orphan',
    )
    images: Mapped[List['Image']] = db.relationship('Image', secondary=evse_image)
    related_resources: Mapped['RelatedResource'] = db.relationship(
        'RelatedResource',
        back_populates='evse',
        cascade='all, delete, delete-orphan',
    )
    location: Mapped['Location'] = db.relationship('Location', back_populates='evses')
    location_id: Mapped[int] = db.Column(db.BigInteger, db.ForeignKey('location.id', use_alter=True), nullable=False)

    uid: Mapped[str] = db.Column(db.String(64), nullable=False, index=True)
    status: Mapped[EvseStatus] = db.Column(
        db.Enum(EvseStatus, name='EvseStatus'),
        default=EvseStatus.UNKNOWN,
        nullable=False,
    )

    lat: Mapped[Decimal] = db.Column(db.Numeric(9, 7))
    lon: Mapped[Decimal] = db.Column(db.Numeric(10, 7))

    floor_level: Mapped[str] = db.Column(db.String(16))
    physical_reference: Mapped[str] = db.Column(db.String(255))
    directions: Mapped[str] = db.Column(db.Text)
    phone: Mapped[str] = db.Column(db.String(255))  # OCHP: telephoneNumber

    parking_uid: Mapped[str] = db.Column(db.String(255))  # OCHP: parkingSpot.parkingId
    parking_floor_level: Mapped[str] = db.Column(db.String(255))  # OCHP: parkingSpot.floorlevel
    parking_spot_number: Mapped[str] = db.Column(db.String(255))  # OCHP: parkingSpot.parkingSpotNumber

    last_updated: Mapped[datetime] = db.Column(UtcDateTime())
    max_reservation: Mapped[float] = db.Column(db.Float)  # OCHP maxReservation
    _capabilities: Mapped[int] = db.Column('capabilities', db.Integer)  # OCPI: capability
    # OCHP: RestrictionType     OCPI: parking_restrictions
    _parking_restrictions: Mapped[int] = db.Column('parking_restrictions', db.Integer)

    terms_and_conditions: Mapped[str] = db.Column(db.String(255))  # OCPI: terms_and_conditions

    # status_schedule TODO
    # user_interface_lang TODO                              # OCHP userInterfaceLang

    def _get_capabilities(self) -> List[Capability]:
        if self._capabilities is None:
            return []
        return sorted(
            [item for item in list(Capability) if (1 << list(Capability).index(item)) & self._capabilities],
            key=lambda item: 1 << list(Capability).index(item),
        )

    def _set_capabilities(self, capabilities: List[Capability]) -> None:
        self._capabilities = 0
        for capability in capabilities:
            self._capabilities = self._capabilities | (1 << list(Capability).index(capability))

    capabilities: List[Capability] = db.synonym(
        '_capabilities',
        descriptor=property(_get_capabilities, _set_capabilities),
    )

    def _get_parking_restrictions(self) -> List[ParkingRestriction]:
        if self._parking_restrictions is None:
            return []
        return sorted(
            [
                item
                for item in list(ParkingRestriction)
                if (1 << list(ParkingRestriction).index(item)) & self._parking_restrictions
            ],
            key=lambda item: 1 << list(ParkingRestriction).index(item),
        )

    def _set_parking_restrictions(self, parking_restrictions: List[ParkingRestriction]) -> None:
        self._parking_restrictions = 0
        for parking_restriction in parking_restrictions:
            self._parking_restrictions = self._parking_restrictions | (
                1 << list(ParkingRestriction).index(parking_restriction)
            )

    parking_restrictions = db.synonym(
        '_parking_restrictions', descriptor=property(_get_parking_restrictions, _set_parking_restrictions)
    )
