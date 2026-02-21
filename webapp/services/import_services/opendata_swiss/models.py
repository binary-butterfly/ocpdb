"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2025 binary butterfly GmbH

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

from webapp.models.charging_station import Capability
from webapp.models.connector import ConnectorFormat, ConnectorType, PowerType
from webapp.models.evse import EvseStatus
from webapp.models.location import ParkingType

TIME_ZONE_MAPPING: dict[str, str] = {
    'ARG': 'America/Argentina/Buenos_Aires',
    'AUS': 'Australia/Sydney',
    'AUT': 'Europe/Vienna',
    'BEL': 'Europe/Brussels',
    'BGR': 'Europe/Sofia',
    'CHE': 'Europe/Zurich',
    'CYP': 'Europe/Nicosia',
    'CZE': 'Europe/Prague',
    'DEU': 'Europe/Berlin',
    'EST': 'Europe/Tallinn',
    'FIN': 'Europe/Helsinki',
    'FRA': 'Europe/Paris',
    'ISR': 'Asia/Jerusalem',
    'LAO': 'Asia/Vientiane',
    'ITA': 'Europe/Rome',
    'LIE': 'Europe/Vaduz',
    'LTU': 'Europe/Vilnius',
    'NLD': 'Europe/Amsterdam',
    'POL': 'Europe/Warsaw',
    'SVK': 'Europe/Bratislava',
}


class AccessibilityLocationType(Enum):
    PARKING_GARAGE = 'ParkingGarage'
    ON_STREET = 'OnStreet'
    PARKING_LOT = 'ParkingLot'
    UNDERGROUND_GARAGE = 'UndergroundParkingGarage'

    def to_parking_type(self) -> ParkingType:
        return {
            self.PARKING_GARAGE: ParkingType.PARKING_GARAGE,
            self.ON_STREET: ParkingType.ON_STREET,
            self.PARKING_LOT: ParkingType.PARKING_LOT,
            self.UNDERGROUND_GARAGE: ParkingType.UNDERGROUND_GARAGE,
        }.get(self)


class AuthenticationMode(Enum):
    RFID_READER_DESFIRE = 'NFC RFID DESFire'
    REMOTE_START_STOP_CAPABLE = 'REMOTE'
    RFID_READER_CLASSIC = 'NFC RFID Classic'
    DIRECT_PAYMENT = 'Direct Payment'
    PLUG_AND_CHARGE = 'PnC'

    def to_capability(self) -> Capability | None:
        return {
            self.RFID_READER_DESFIRE: Capability.RFID_READER,
            self.REMOTE_START_STOP_CAPABLE: Capability.REMOTE_START_STOP_CAPABLE,
            self.RFID_READER_CLASSIC: Capability.RFID_READER,
        }.get(self)


class SwissPowerType(Enum):
    DC = 'DC'
    AC_1_PHASE = 'AC_1_PHASE'
    AC_3_PHASE = 'AC_3_PHASE'

    def to_power_type(self) -> PowerType:
        return {
            self.DC: PowerType.DC,
            self.AC_1_PHASE: PowerType.AC_1_PHASE,
            self.AC_3_PHASE: PowerType.AC_3_PHASE,
        }.get(self)


class Plug(Enum):
    DOMESTIC_J_SOCKET = 'Type J Swiss Standard'
    IEC_62196_T2_SOCKET = 'Type 2 Outlet'
    TESLA_S_CABLE = 'Tesla Connector'
    IEC_62196_T1_CABLE = 'Type 1 Connector (Cable Attached)'
    DOMESTIC_F_SOCKET = 'Type F Schuko'
    IEC_62196_T1_COMBO_CABLE = 'CCS Combo 1 Plug (Cable Attached)'
    IEC_62196_T2_CABLE = 'Type 2 Connector (Cable Attached)'
    CHADEMO = 'CHAdeMO'
    DOMESTIC_G_SOCKET = 'Type G British Standard'
    IEC_62196_T2_COMBO_CABLE = 'CCS Combo 2 Plug (Cable Attached)'

    def to_standard(self) -> ConnectorType:
        return {
            self.DOMESTIC_J_SOCKET: ConnectorType.IEC_62196_T2,
            self.IEC_62196_T2_SOCKET: ConnectorType.IEC_62196_T2,
            self.TESLA_S_CABLE: ConnectorType.TESLA_S,
            self.IEC_62196_T1_CABLE: ConnectorType.IEC_62196_T1,
            self.DOMESTIC_F_SOCKET: ConnectorType.IEC_62196_T2,
            self.IEC_62196_T1_COMBO_CABLE: ConnectorType.IEC_62196_T1,
            self.IEC_62196_T2_CABLE: ConnectorType.IEC_62196_T2,
            self.CHADEMO: ConnectorType.TESLA_S,
            self.DOMESTIC_G_SOCKET: ConnectorType.DOMESTIC_G,
            self.IEC_62196_T2_COMBO_CABLE: ConnectorType.IEC_62196_T2_COMBO,
        }.get(self)

    def to_format(self) -> ConnectorFormat:
        return {
            self.DOMESTIC_J_SOCKET: ConnectorFormat.SOCKET,
            self.IEC_62196_T2_SOCKET: ConnectorFormat.SOCKET,
            self.TESLA_S_CABLE: ConnectorFormat.CABLE,
            self.IEC_62196_T1_CABLE: ConnectorFormat.CABLE,
            self.DOMESTIC_F_SOCKET: ConnectorFormat.SOCKET,
            self.IEC_62196_T1_COMBO_CABLE: ConnectorFormat.CABLE,
            self.IEC_62196_T2_CABLE: ConnectorFormat.CABLE,
            self.CHADEMO: ConnectorFormat.CABLE,
            self.DOMESTIC_G_SOCKET: ConnectorFormat.SOCKET,
            self.IEC_62196_T2_COMBO_CABLE: ConnectorFormat.CABLE,
        }.get(self)


class Weekday(Enum):
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'
    WORKDAYS = 'Workdays'

    def to_weekday(self) -> int:
        return {
            self.MONDAY: 1,
            self.TUESDAY: 2,
            self.WEDNESDAY: 3,
            self.THURSDAY: 4,
            self.FRIDAY: 5,
            self.SATURDAY: 6,
            self.SUNDAY: 7,
        }.get(self)


class SwissEvseStatus(Enum):
    AVAILABLE = 'Available'
    UNKNOWN = 'Unknown'
    OUT_OF_SERVICE = 'OutOfService'
    OCCUPIED = 'Occupied'
    RESERVED = 'Reserved'

    def to_evse_status(self) -> EvseStatus:
        return {
            self.AVAILABLE: EvseStatus.AVAILABLE,
            self.UNKNOWN: EvseStatus.UNKNOWN,
            self.OUT_OF_SERVICE: EvseStatus.OUTOFORDER,
            self.OCCUPIED: EvseStatus.CHARGING,
            self.RESERVED: EvseStatus.RESERVED,
        }.get(self)


class DynamicInfoAvailable(Enum):
    TRUE = 'true'
    FALSE = 'false'
    AUTO = 'auto'
