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
from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, Float, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy import Enum as SqlalchemyEnum
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utc import UtcDateTime

from webapp.common.json import DefaultJSONEncoder

from .base import BaseModel
from .evse_image import EvseImageAssociation

if TYPE_CHECKING:
    from .connector import Connector
    from .image import Image
    from .location import Location


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


class Evse(BaseModel):
    __tablename__ = 'evse'

    connectors: Mapped[list['Connector']] = relationship(
        'Connector',
        back_populates='evse',
        cascade='all, delete, delete-orphan',
    )
    images: Mapped[list['Image']] = relationship(
        'Image',
        secondary=EvseImageAssociation.__table__,
        back_populates='evses',
    )
    location: Mapped['Location'] = relationship('Location', back_populates='evses')

    location_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey('location.id', use_alter=True), nullable=False, index=True
    )

    uid: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    evse_id: Mapped[str | None] = mapped_column(String(64), nullable=True, index=True)
    status: Mapped[EvseStatus] = mapped_column(
        SqlalchemyEnum(EvseStatus, name='EvseStatus'),
        default=EvseStatus.UNKNOWN,
        nullable=False,
        index=True,
    )

    lat: Mapped[Decimal | None] = mapped_column(Numeric(9, 7), nullable=True)
    lon: Mapped[Decimal | None] = mapped_column(Numeric(10, 7), nullable=True)

    floor_level: Mapped[str | None] = mapped_column(String(16), nullable=True)
    physical_reference: Mapped[str | None] = mapped_column(String(255), nullable=True)
    _directions: Mapped[str | None] = mapped_column('directions', Text, nullable=True)
    phone: Mapped[str | None] = mapped_column(String(255), nullable=True)  # OCHP: telephoneNumber

    parking_uid: Mapped[str | None] = mapped_column(String(255), nullable=True)  # OCHP: parkingSpot.parkingId
    parking_floor_level: Mapped[str | None] = mapped_column(String(255), nullable=True)  # OCHP: parkingSpot.floorlevel
    # OCHP: parkingSpot.parkingSpotNumber
    parking_spot_number: Mapped[str | None] = mapped_column(String(255), nullable=True)

    last_updated: Mapped[datetime | None] = mapped_column(UtcDateTime(), nullable=True, index=True)
    max_reservation: Mapped[float | None] = mapped_column(Float, nullable=True)  # OCHP maxReservation
    _capabilities: Mapped[int | None] = mapped_column('capabilities', Integer, nullable=True)  # OCPI: capability
    # OCHP: RestrictionType     OCPI: parking_restrictions
    _parking_restrictions: Mapped[int | None] = mapped_column('parking_restrictions', Integer, nullable=True)

    terms_and_conditions: Mapped[str | None] = mapped_column(String(255), nullable=True)  # OCPI: terms_and_conditions

    _related_resources: Mapped[str | None] = mapped_column('related_resources', Text, nullable=True)

    # status_schedule TODO
    # user_interface_lang TODO                              # OCHP userInterfaceLang

    @hybrid_property
    def capabilities(self) -> list[Capability]:
        if self._capabilities is None:
            return []
        return sorted(
            [item for item in list(Capability) if (1 << list(Capability).index(item)) & self._capabilities],
            key=lambda item: 1 << list(Capability).index(item),
        )

    @capabilities.setter
    def capabilities(self, capabilities: list[Capability]) -> None:
        self._capabilities = 0
        for capability in capabilities:
            self._capabilities = self._capabilities | (1 << list(Capability).index(capability))

    @hybrid_property
    def parking_restrictions(self) -> list[ParkingRestriction]:
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

    @parking_restrictions.setter
    def parking_restrictions(self, parking_restrictions: list[ParkingRestriction]) -> None:
        self._parking_restrictions = 0
        for parking_restriction in parking_restrictions:
            self._parking_restrictions = self._parking_restrictions | (
                1 << list(ParkingRestriction).index(parking_restriction)
            )

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

    @hybrid_property
    def related_resources(self) -> list[dict] | None:
        if self._related_resources is None:
            return None

        return json.loads(self._related_resources)

    @related_resources.setter
    def related_resources(self, related_resources: list[dict] | None) -> None:
        if related_resources is None:
            self._related_resources = None
            return
        self._related_resources = json.dumps(related_resources, cls=DefaultJSONEncoder)

    def to_dict(self, *args, ignore: list[str] | None = None, strict: bool = False, **kwargs) -> dict:
        ignore = ignore or []
        ignore += [
            'external_id',
            'giroe_id',
            'location_id',
            'created',
            'modified',
            'id',
            'lat',
            'lon',
            'parking_spot_number',
            'parking_floor_level',
            'parking_uid',
            'phone',
        ]

        result = super().to_dict(*args, ignore=ignore, **kwargs)

        result['uid'] = str(self.id)

        if not strict:
            result['original_uid'] = self.uid
            result['parking_spot_number'] = self.parking_spot_number
            result['parking_floor_level'] = self.parking_floor_level
            result['parking_uid'] = self.parking_uid
            result['phone'] = self.phone

        if self.lat is not None and self.lon is not None:
            result['coordinates'] = {
                'latitude': self.lat,
                'longitude': self.lon,
            }

        return result
