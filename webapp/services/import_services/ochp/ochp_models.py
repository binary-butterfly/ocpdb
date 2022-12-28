"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2022 binary butterfly GmbH

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


class OchpImageCategory(Enum):
    networkLogo = 'networkLogo'
    operatorLogo = 'operatorLogo'
    ownerLogo = 'ownerLogo'
    stationPhoto = 'stationPhoto'
    locationPhoto = 'locationPhoto'
    entrancePhoto = 'entrancePhoto'
    otherPhoto = 'otherPhoto'
    otherLogo = 'otherLogo'
    otherGraphic = 'otherGraphic'


class OchpImageType(Enum):
    gif = 'gif'
    jpeg = 'jpeg'
    png = 'png'
    svg = 'svg'


class OchpStaticStatus(Enum):
    Unknown = 'Unknown'
    Operative = 'Operative'
    Inoperative = 'Inoperative'
    Planned = 'Planned'
    Closed = 'Closed'


class OchpLocationType(Enum):
    on_street = 'on_street'
    parking_garage = 'parking_garage'
    underground_garage = 'underground_garage'
    parking_lot = 'parking_lot'
    private = 'private'
    other = 'other'
    unknown = 'unknown'


class OchpParkingRestrictionType(Enum):
    evonly = 'evonly'
    plugged = 'plugged'
    disabled = 'disabled'
    customers = 'customers'
    motorcycles = 'motorcycles'
    carsharing = 'carsharing'


class OchpAuthMethodType(Enum):
    Public = 'Public'
    LocalKey = 'LocalKey'
    DirectCash = 'DirectCash'
    DirectCreditcard = 'DirectCreditcard'
    DirectDebitcard = 'DirectDebitcard'
    RfidMifareCls = 'RfidMifareCls'
    RfidMifareDes = 'RfidMifareDes'
    RfidCalypso = 'RfidCalypso'
    Iec15118 = 'Iec15118'
    OchpDirectAuth = 'OchpDirectAuth'
    OperatorAuth = 'OperatorAuth'


class OchpChargePointType(Enum):
    AC = 'AC'
    DC = 'DC'


class OchpRelatedResourceType(Enum):
    operatorMap = 'operatorMap'
    operatorPayment = 'operatorPayment'
    stationInfo = 'stationInfo'
    surroundingInfo = 'surroundingInfo'
    ownerHomepage = 'ownerHomepage'
    feedbackForm = 'feedbackForm'
    openingTimes = 'openingTimes'


class OchpGeoType(Enum):
    entrance = 'entrance'
    exit = 'exit'
    access = 'access'
    ui = 'ui'
    other = 'other'


class OchpConnectorStandard(Enum):
    Chademo = 'Chademo'
    IEC_62196_T1 = 'IEC_62196_T1'
    IEC_62196_T1_COMBO = 'IEC_62196_T1_COMBO'
    IEC_62196_T2 = 'IEC_62196_T2'
    IEC_62196_T2_COMBO = 'IEC_62196_T2_COMBO'
    IEC_62196_T3A = 'IEC_62196_T3A'
    IEC_62196_T3C = 'IEC_62196_T3C'
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
    TESLA_R = 'TESLA_R'
    TESLA_S = 'TESLA_S'
    IEC_60309_2_single_16 = 'IEC_60309_2_single_16'
    IEC_60309_2_three_16 = 'IEC_60309_2_three_16'
    IEC_60309_2_three_32 = 'IEC_60309_2_three_32'
    IEC_60309_2_three_64 = 'IEC_60309_2_three_64'


class OchpConnectorFormat(Enum):
    Socket = 'Socket'
    Cable = 'Cable'


class OchpMajorStatus(Enum):
    unknown = 'unknown'
    available = 'available'
    not_available = 'not_available'


class OchpMinorStatus(Enum):
    available = 'available'
    reserved = 'reserved'
    charging = 'charging'
    blocked = 'blocked'
    outoforder = 'outoforder'
