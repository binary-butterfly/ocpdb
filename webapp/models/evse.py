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
from enum import Enum
from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, Float, ForeignKey, Integer, String, Text
from sqlalchemy import Enum as SqlalchemyEnum
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utc import UtcDateTime

from webapp.common.json import DefaultJSONEncoder

from .base import BaseModel
from .evse_image import EvseImageAssociation

if TYPE_CHECKING:
    from .charging_station import ChargingStation
    from .connector import Connector
    from .image import Image


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


class PresenceStatus(Enum):
    PRESENT = 'PRESENT'
    PLANNED = 'PLANNED'
    REMOVED = 'REMOVED'


class ParkingRestriction(Enum):
    EV_ONLY = 'EV_ONLY'
    PLUGGED = 'PLUGGED'
    DISABLED = 'DISABLED'
    CUSTOMERS = 'CUSTOMERS'
    MOTORCYCLES = 'MOTORCYCLES'
    CARSHARING = 'CARSHARING'
    BICYCLE_ONLY = 'BICYCLE_ONLY'


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
    charging_station: Mapped['ChargingStation'] = relationship('ChargingStation', back_populates='evses')

    charging_station_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey('charging_station.id', use_alter=True),
        nullable=False,
        index=True,
    )

    uid: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    evse_id: Mapped[str | None] = mapped_column(String(64), nullable=True, index=True)
    status: Mapped[EvseStatus] = mapped_column(
        SqlalchemyEnum(EvseStatus, name='EvseStatus'),
        default=EvseStatus.UNKNOWN,
        nullable=False,
        index=True,
    )
    presence: Mapped[PresenceStatus] = mapped_column(
        SqlalchemyEnum(PresenceStatus, name='PresenceStatus'),
        default=PresenceStatus.PRESENT,
        nullable=False,
    )

    physical_reference: Mapped[str | None] = mapped_column(String(255), nullable=True)

    last_updated: Mapped[datetime] = mapped_column(UtcDateTime(), nullable=False, index=True)
    status_last_updated: Mapped[datetime | None] = mapped_column(UtcDateTime(), nullable=True)
    max_reservation: Mapped[float | None] = mapped_column(Float, nullable=True)
    _parking_restrictions: Mapped[int | None] = mapped_column('parking_restrictions', Integer, nullable=True)

    terms_and_conditions: Mapped[str | None] = mapped_column(String(255), nullable=True)
    calibration_info_url: Mapped[str | None] = mapped_column(String(255), nullable=True)

    _related_resources: Mapped[str | None] = mapped_column('related_resources', Text, nullable=True)

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
    def parking_restrictions(self, parking_restrictions: list[ParkingRestriction] | None) -> None:
        self._parking_restrictions = 0
        if parking_restrictions is None:
            return
        for parking_restriction in parking_restrictions:
            self._parking_restrictions = self._parking_restrictions | (
                1 << list(ParkingRestriction).index(parking_restriction)
            )

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
            'charging_station_id',
            'created',
            'modified',
            'id',
        ]

        result = super().to_dict(*args, ignore=ignore, **kwargs)

        result['uid'] = str(self.id)

        if not strict:
            result['original_uid'] = self.uid

        return result
