"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2026 binary butterfly GmbH

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
from datetime import date, datetime
from decimal import Decimal
from enum import Enum
from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, Date, Float, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy import Enum as SqlalchemyEnum
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utc import UtcDateTime

from webapp.common.json import DefaultJSONEncoder

from .base import BaseModel
from .charging_station_image import ChargingStationImageAssociation
from .enums import ChargingRateUnit

if TYPE_CHECKING:
    from .evse import Evse
    from .image import Image
    from .location import Location


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


class ChargingStation(BaseModel):
    __tablename__ = 'charging_station'

    location_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey('location.id', use_alter=True),
        nullable=False,
        index=True,
    )
    location: Mapped['Location'] = relationship('Location', back_populates='charging_pool')

    evses: Mapped[list['Evse']] = relationship(
        'Evse',
        back_populates='charging_station',
        cascade='all, delete, delete-orphan',
    )
    images: Mapped[list['Image']] = relationship(
        'Image',
        secondary=ChargingStationImageAssociation.__table__,
        back_populates='charging_pool',
    )

    uid: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    _capabilities: Mapped[int | None] = mapped_column('capabilities', Integer, nullable=True)
    floor_level: Mapped[str | None] = mapped_column(String(16), nullable=True)
    physical_reference: Mapped[str | None] = mapped_column(String(255), nullable=True)
    last_updated: Mapped[datetime] = mapped_column(UtcDateTime(), nullable=False, index=True)
    go_live_date: Mapped[date | None] = mapped_column(Date(), nullable=True)

    lat: Mapped[Decimal | None] = mapped_column(Numeric(9, 7), nullable=True)
    lon: Mapped[Decimal | None] = mapped_column(Numeric(10, 7), nullable=True)
    _directions: Mapped[str | None] = mapped_column('directions', Text, nullable=True)

    max_power_unit: Mapped[ChargingRateUnit | None] = mapped_column(SqlalchemyEnum(ChargingRateUnit), nullable=True)
    max_power_value: Mapped[float | None] = mapped_column(Float, nullable=True)

    @hybrid_property
    def capabilities(self) -> list[Capability]:
        if self._capabilities is None:
            return []
        return sorted(
            [item for item in list(Capability) if (1 << list(Capability).index(item)) & self._capabilities],
            key=lambda item: 1 << list(Capability).index(item),
        )

    @capabilities.setter
    def capabilities(self, capabilities: list[Capability] | None) -> None:
        self._capabilities = 0
        if capabilities is None:
            return
        for capability in capabilities:
            self._capabilities = self._capabilities | (1 << list(Capability).index(capability))

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

    def to_dict(self, *args, ignore: list[str] | None = None, strict: bool = False, **kwargs) -> dict:
        ignore = ignore or []
        ignore += [
            'id',
            'location_id',
            'created',
            'modified',
            'lat',
            'lon',
        ]

        result = super().to_dict(*args, ignore=ignore, **kwargs)

        if self.lat is not None and self.lon is not None:
            result['coordinates'] = {
                'latitude': self.lat,
                'longitude': self.lon,
            }

        return result
