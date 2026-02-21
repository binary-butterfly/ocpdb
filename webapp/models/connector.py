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
from enum import Enum
from math import sqrt
from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, ForeignKey, Integer, String
from sqlalchemy import Enum as SqlalchemyEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utc import UtcDateTime

from .base import BaseModel

if TYPE_CHECKING:
    from .evse import Evse


class ConnectorType(Enum):
    CHADEMO = 'CHADEMO'
    DOMESTIC_A = 'DOMESTIC_A'
    DOMESTIC_B = 'DOMESTIC_B'
    DOMESTIC_C = 'DOMESTIC_C'
    DOMESTIC_D = 'DOMESTIC_D'
    DOMESTIC_E = 'DOMESTIC_E'
    DOMESTIC_F = 'DOMESTIC_F'
    DOMESTIC_G = 'DOMESTIC_G'
    DOMESTIC_H = 'DOMESTIC_H'
    DOMESTIC_I = 'DOMESTIC_I'
    DOMESTIC_J = 'DOMESTIC_J'
    DOMESTIC_K = 'DOMESTIC_K'
    DOMESTIC_L = 'DOMESTIC_L'
    IEC_60309_2_single_16 = 'IEC_60309_2_single_16'
    IEC_60309_2_three_16 = 'IEC_60309_2_three_16'
    IEC_60309_2_three_32 = 'IEC_60309_2_three_32'
    IEC_60309_2_three_64 = 'IEC_60309_2_three_64'
    IEC_62196_T1 = 'IEC_62196_T1'
    IEC_62196_T1_COMBO = 'IEC_62196_T1_COMBO'
    IEC_62196_T2 = 'IEC_62196_T2'
    IEC_62196_T2_COMBO = 'IEC_62196_T2_COMBO'
    IEC_62196_T3A = 'IEC_62196_T3A'
    IEC_62196_T3C = 'IEC_62196_T3C'
    PANTOGRAPH_BOTTOM_UP = 'PANTOGRAPH_BOTTOM_UP'
    PANTOGRAPH_TOP_DOWN = 'PANTOGRAPH_TOP_DOWN'
    TESLA_R = 'TESLA_R'
    TESLA_S = 'TESLA_S'
    MCS = 'MCS'
    SAE_J3400 = 'SAE_J3400'
    NEMA_5_20 = 'NEMA_5_20'
    NEMA_6_30 = 'NEMA_6_30'
    NEMA_6_50 = 'NEMA_6_50'
    NEMA_10_30 = 'NEMA_10_30'
    NEMA_10_50 = 'NEMA_10_50'
    NEMA_14_30 = 'NEMA_14_30'
    NEMA_14_50 = 'NEMA_14_50'
    GBT_AC = 'GBT_AC'
    GBT_DC = 'GBT_DC'


ac_1_phase_connector_types = [
    ConnectorType.DOMESTIC_A,
    ConnectorType.DOMESTIC_B,
    ConnectorType.DOMESTIC_C,
    ConnectorType.DOMESTIC_D,
    ConnectorType.DOMESTIC_E,
    ConnectorType.DOMESTIC_F,
    ConnectorType.DOMESTIC_G,
    ConnectorType.DOMESTIC_H,
    ConnectorType.DOMESTIC_I,
    ConnectorType.DOMESTIC_J,
    ConnectorType.DOMESTIC_K,
    ConnectorType.DOMESTIC_L,
    ConnectorType.IEC_60309_2_single_16,
]


class ConnectorFormat(Enum):
    SOCKET = 'SOCKET'
    CABLE = 'CABLE'


class ConnectorStatus(Enum):
    AVAILABLE = 'AVAILABLE'
    BLOCKED = 'BLOCKED'
    CHARGING = 'CHARGING'
    INOPERATIVE = 'INOPERATIVE'
    OUTOFORDER = 'OUTOFORDER'
    PLANNED = 'PLANNED'
    REMOVED = 'REMOVED'
    RESERVED = 'RESERVED'
    UNKNOWN = 'UNKNOWN'
    SUSPENDED_EVSE = 'SUSPENDED_EVSE'
    SUSPENDED_EV = 'SUSPENDED_EV'
    FINISHING = 'FINISHING'
    PREPARING = 'PREPARING'


class PowerType(Enum):
    AC_1_PHASE = 'AC_1_PHASE'
    AC_3_PHASE = 'AC_3_PHASE'
    DC = 'DC'


class Connector(BaseModel):
    __tablename__ = 'connector'

    evse: Mapped['Evse'] = relationship('Evse', back_populates='connectors')
    evse_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('evse.id', use_alter=True), nullable=False, index=True)

    uid: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    standard: Mapped[ConnectorType | None] = mapped_column(SqlalchemyEnum(ConnectorType), nullable=True)
    format: Mapped[ConnectorFormat | None] = mapped_column(SqlalchemyEnum(ConnectorFormat), nullable=True)
    power_type: Mapped[PowerType | None] = mapped_column(SqlalchemyEnum(PowerType), nullable=True)
    max_voltage: Mapped[int | None] = mapped_column(Integer, nullable=True)
    max_amperage: Mapped[int | None] = mapped_column(Integer, nullable=True)
    max_electric_power: Mapped[int | None] = mapped_column(Integer, nullable=True)
    last_updated: Mapped[datetime] = mapped_column(UtcDateTime(), nullable=False)
    terms_and_conditions: Mapped[str | None] = mapped_column(String(255), nullable=True)

    # tariff_ids TODO

    def guess_power_type(self):
        if self.power_type == PowerType.DC or not self.max_electric_power:
            return
        if self.max_electric_power < 10000 or self.standard in ac_1_phase_connector_types:
            self.power_type = PowerType.AC_1_PHASE
        self.power_type = PowerType.AC_3_PHASE

    def guess_voltage_amperage(self):
        if not self.max_electric_power or not self.power_type:
            return
        if self.power_type == PowerType.DC:
            if not self.max_voltage:
                self.max_voltage = 400
            self.max_amperage = int(round(self.max_electric_power / self.max_voltage))
        elif self.power_type == PowerType.AC_1_PHASE:
            if not self.max_voltage:
                self.max_voltage = 230
            self.max_amperage = int(round(self.max_electric_power / self.max_voltage))
        else:
            if not self.max_voltage:
                self.max_voltage = 400
            self.max_amperage = int(round(self.max_electric_power / self.max_voltage / sqrt(3)))

    def to_dict(self, *args, strict: bool = False, ignore: list[str] | None = None, **kwargs) -> dict:
        ignore = ignore or []
        ignore += ['uid', 'created', 'modified', 'evse_id']

        result = super().to_dict(*args, ignore=ignore, **kwargs)

        # OCPI id has to be a string
        result['id'] = str(self.id)

        if not strict:
            result['original_id'] = self.uid

        return result
