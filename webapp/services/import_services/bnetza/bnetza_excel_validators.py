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
from typing import List, Optional

from validataclass.dataclasses import validataclass
from validataclass.validators import EnumValidator, IntegerValidator, ListValidator, StringValidator

from webapp.common.validation import (
    CommaStringToDecimalValidator,
    DateTimeToUtcDateTimeValidator,
    EmptystringToNoneable,
    IntegerToStringValidator,
    PrintableStringValidator,
)


class BnetzaConnectorType(Enum):
    CHADEMO = 'DC CHAdeMO'
    DOMESTIC_F = 'AC Schuko'
    IEC_60309_2_single_16 = 'AC CEE 3 polig'
    IEC_60309_2_three_any = 'AC CEE 5 polig'
    IEC_62196_T1 = 'AC Typ 1 Steckdose'
    IEC_62196_T2 = 'AC Typ 2 Steckdose'
    IEC_62196_T1_WIRED = 'AC Typ 1 Fahrzeugkupplung'
    IEC_62196_T2_WIRED = 'AC Typ 2 Fahrzeugkupplung'
    IEC_62196_T2_COMBO = 'DC Fahrzeugkupplung Typ Combo 2 (CCS)'
    IEC_62196_T3A = 'Typ 3'
    TESLA_S_1 = 'Typ 2 / Tesla'
    TESLA_S_2 = 'Tesla'


class BnetzaChargestationType(Enum):
    Normalladeeinrichtung = 'Normalladeeinrichtung'
    Schnellladeeinrichtung = 'Schnellladeeinrichtung'


@validataclass
class BnetzaRowInput:
    operator: str = PrintableStringValidator()
    address: str = PrintableStringValidator()
    housenumber: str = IntegerToStringValidator()
    postcode: str = StringValidator()
    locality: str = StringValidator()
    land: str = StringValidator()
    district: str = StringValidator()
    lat: Decimal = CommaStringToDecimalValidator()
    lon: Decimal = CommaStringToDecimalValidator()
    launch_date: datetime = DateTimeToUtcDateTimeValidator()
    connection_power: float = CommaStringToDecimalValidator()
    chargestation_type: BnetzaChargestationType = EnumValidator(BnetzaChargestationType)
    connector_count: int = IntegerValidator()
    connector_1_type: List[BnetzaConnectorType] = ListValidator(EnumValidator(BnetzaConnectorType))
    connector_1_power: Optional[float] = EmptystringToNoneable(CommaStringToDecimalValidator())
    connector_1_public_key: Optional[str] = EmptystringToNoneable(IntegerToStringValidator(multiline=True))
    connector_2_type: List[BnetzaConnectorType] = ListValidator(EnumValidator(BnetzaConnectorType))
    connector_2_power: Optional[float] = EmptystringToNoneable(CommaStringToDecimalValidator())
    connector_2_public_key: Optional[str] = EmptystringToNoneable(IntegerToStringValidator(multiline=True))
    connector_3_type: List[BnetzaConnectorType] = ListValidator(EnumValidator(BnetzaConnectorType))
    connector_3_power: Optional[float] = EmptystringToNoneable(CommaStringToDecimalValidator())
    connector_3_public_key: Optional[str] = EmptystringToNoneable(IntegerToStringValidator(multiline=True))
    connector_4_type: List[BnetzaConnectorType] = ListValidator(EnumValidator(BnetzaConnectorType))
    connector_4_power: Optional[float] = EmptystringToNoneable(CommaStringToDecimalValidator())
    connector_4_public_key: Optional[str] = EmptystringToNoneable(IntegerToStringValidator(multiline=True))
    connector_5_type: List[BnetzaConnectorType] = ListValidator(EnumValidator(BnetzaConnectorType))
    connector_5_power: Optional[float] = EmptystringToNoneable(CommaStringToDecimalValidator())
    connector_5_public_key: Optional[str] = EmptystringToNoneable(IntegerToStringValidator(multiline=True))
    connector_6_type: List[BnetzaConnectorType] = ListValidator(EnumValidator(BnetzaConnectorType))
    connector_6_power: Optional[float] = EmptystringToNoneable(CommaStringToDecimalValidator())
    connector_6_public_key: Optional[str] = EmptystringToNoneable(IntegerToStringValidator(multiline=True))
