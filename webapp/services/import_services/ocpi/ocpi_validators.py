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

from datetime import datetime, time, timezone
from decimal import Decimal
from typing import List

from validataclass.dataclasses import validataclass, DefaultUnset, ValidataclassMixin
from validataclass.helpers import OptionalUnset
from validataclass.validators import StringValidator, DecimalValidator, DataclassValidator, IntegerValidator, ListValidator, \
    BooleanValidator, TimeValidator, DateTimeValidator, EnumValidator, TimeFormat, DateTimeFormat, UrlValidator, FloatValidator

from webapp.common.validation import UnvalidatedDictValidator
from webapp.models.connector import ConnectorType, ConnectorFormat, PowerType
from webapp.models.evse import Capability, ParkingRestriction, EvseStatus
from webapp.models.image import ImageCategory
from webapp.models.location import ParkingType, Facility, EnergySourceCategory, EnvironmentalImpactCategory


@validataclass
class ConnectorInput(ValidataclassMixin):
    id: str = StringValidator(max_length=36)
    standard: ConnectorType = EnumValidator(ConnectorType)
    format: ConnectorFormat = EnumValidator(ConnectorFormat)
    power_type: PowerType = EnumValidator(PowerType)
    max_voltage: int = IntegerValidator()
    max_amperage: int = IntegerValidator()
    max_electric_power: OptionalUnset[int] = IntegerValidator(), DefaultUnset
    tariff_ids: OptionalUnset[List[str]] = ListValidator(StringValidator(max_length=36)), DefaultUnset
    terms_and_conditions: OptionalUnset[str] = UrlValidator(max_length=255), DefaultUnset
    last_updated: OptionalUnset[datetime] = DateTimeValidator(
        DateTimeFormat.LOCAL_OR_UTC,
        local_timezone=timezone.utc,
        target_timezone=timezone.utc,
    ), DefaultUnset


@validataclass
class RegularHoursInput(ValidataclassMixin):
    weekday: int = IntegerValidator(min_value=1, max_value=7)
    period_begin: time = TimeValidator(time_format=TimeFormat.NO_SECONDS)
    period_end: time = TimeValidator(time_format=TimeFormat.NO_SECONDS)

    def to_dict(self, *args, **kwargs) -> dict:
        result = super().to_dict(*args, **kwargs)
        result['period_begin'] = self.period_begin.hour * 3600 + self.period_begin.minute * 60
        result['period_end'] = self.period_end.hour * 3600 + self.period_end.minute * 60
        return result


@validataclass
class ExceptionalPeriodInput(ValidataclassMixin):
    period_begin: datetime = DateTimeValidator(
        DateTimeFormat.LOCAL_OR_UTC,
        local_timezone=timezone.utc,
        target_timezone=timezone.utc,
    ), DefaultUnset
    period_end: datetime = DateTimeValidator(
        DateTimeFormat.LOCAL_OR_UTC,
        local_timezone=timezone.utc,
        target_timezone=timezone.utc,
    )


@validataclass
class HoursInput(ValidataclassMixin):
    twentyfourseven: bool = BooleanValidator()
    regular_hours: OptionalUnset[List[RegularHoursInput]] \
        = ListValidator(DataclassValidator(RegularHoursInput)), DefaultUnset
    exceptional_openings: OptionalUnset[List[ExceptionalPeriodInput]] \
        = ListValidator(DataclassValidator(ExceptionalPeriodInput)), DefaultUnset
    exceptional_closings: OptionalUnset[List[ExceptionalPeriodInput]] \
        = ListValidator(DataclassValidator(ExceptionalPeriodInput)), DefaultUnset


@validataclass
class StatusScheduleInput(ValidataclassMixin):
    period_begin: datetime = DateTimeValidator(
        DateTimeFormat.LOCAL_OR_UTC,
        local_timezone=timezone.utc,
        target_timezone=timezone.utc,
    )
    period_end: OptionalUnset[datetime] = DateTimeValidator(
        DateTimeFormat.LOCAL_OR_UTC,
        local_timezone=timezone.utc,
        target_timezone=timezone.utc,
    ), DefaultUnset
    status: EvseStatus = EnumValidator(EvseStatus)


@validataclass
class GeoLocationInput(ValidataclassMixin):
    latitude: Decimal = DecimalValidator()
    longitude: Decimal = DecimalValidator()


@validataclass
class DisplayTextInput(ValidataclassMixin):
    language: str = StringValidator(min_length=2, max_length=2)
    text: str = StringValidator(max_length=512)


@validataclass
class AdditionalGeoLocationInput(ValidataclassMixin):
    name: OptionalUnset[DisplayTextInput] = DataclassValidator(DisplayTextInput), DefaultUnset
    latitude: Decimal = DecimalValidator()
    longitude: Decimal = DecimalValidator()


@validataclass
class ImageInput(ValidataclassMixin):
    url: str = StringValidator(max_length=255)
    thumbnail: OptionalUnset[str] = StringValidator(max_length=255), DefaultUnset
    category: ImageCategory = EnumValidator(ImageCategory)
    type: str = StringValidator(max_length=4)
    width: OptionalUnset[int] = IntegerValidator(), DefaultUnset
    height: OptionalUnset[int] = IntegerValidator(), DefaultUnset


@validataclass
class BusinessDetailsInput(ValidataclassMixin):
    name: str = StringValidator(max_length=100)
    website: OptionalUnset[str] = UrlValidator(), DefaultUnset
    logo: OptionalUnset[ImageInput] = DataclassValidator(ImageInput), DefaultUnset


@validataclass
class EnergySourceInput(ValidataclassMixin):
    source: EnergySourceCategory = EnumValidator(EnergySourceCategory)
    percentage: float = FloatValidator()


@validataclass
class EnvironmentalImpactInput(ValidataclassMixin):
    category: EnvironmentalImpactCategory = EnumValidator(EnvironmentalImpactCategory), DefaultUnset
    amount: float = FloatValidator()


@validataclass
class EnergyMixInput(ValidataclassMixin):
    is_green_energy: bool = BooleanValidator()
    energy_sources: OptionalUnset[List[EnergySourceInput]] = ListValidator(DataclassValidator(EnergySourceInput)), DefaultUnset
    environ_impact: OptionalUnset[List[EnvironmentalImpactInput]] \
        = ListValidator(DataclassValidator(EnvironmentalImpactInput)), DefaultUnset
    supplier_name: OptionalUnset[str] = StringValidator(max_length=64), DefaultUnset
    energy_product_name: OptionalUnset[str] = StringValidator(max_length=64), DefaultUnset


@validataclass
class EvseInput(ValidataclassMixin):
    id: str = StringValidator(max_length=36)
    evse_id: str = StringValidator(max_length=36)
    status: EvseStatus = EnumValidator(EvseStatus)
    status_schedule: OptionalUnset[List[StatusScheduleInput]] = ListValidator(DataclassValidator(StatusScheduleInput)), DefaultUnset
    capabilities: OptionalUnset[List[Capability]] = ListValidator(EnumValidator(Capability)), DefaultUnset
    connectors: List[ConnectorInput] = ListValidator(DataclassValidator(ConnectorInput), min_length=1), DefaultUnset
    floor_level: OptionalUnset[str] = StringValidator(max_length=4), DefaultUnset
    coordinates: OptionalUnset[GeoLocationInput] = DataclassValidator(GeoLocationInput), DefaultUnset
    physical_reference: OptionalUnset[str] = StringValidator(max_length=16), DefaultUnset
    directions: OptionalUnset[List[DisplayTextInput]] = ListValidator(DataclassValidator(DisplayTextInput)), DefaultUnset
    parking_restrictions: OptionalUnset[List[ParkingRestriction]] = ListValidator(EnumValidator(ParkingRestriction)), DefaultUnset
    images: OptionalUnset[List[ImageInput]] = ListValidator(DataclassValidator(ImageInput)), DefaultUnset
    last_updated: OptionalUnset[datetime] = DateTimeValidator(
        DateTimeFormat.LOCAL_OR_UTC,
        local_timezone=timezone.utc,
        target_timezone=timezone.utc,
    ), DefaultUnset


@validataclass
class LocationInput(ValidataclassMixin):
    id: str = StringValidator(max_length=36)
    name: OptionalUnset[str] = StringValidator(max_length=100), DefaultUnset
    address: str = StringValidator(max_length=45)
    city: str = StringValidator(max_length=45)
    postal_code: OptionalUnset[str] = StringValidator(max_length=10), DefaultUnset
    state: OptionalUnset[str] = StringValidator(max_length=20), DefaultUnset
    country: str = StringValidator(min_length=3, max_length=3)
    coordinates: GeoLocationInput = DataclassValidator(GeoLocationInput)
    related_locations: OptionalUnset[List[AdditionalGeoLocationInput]]\
        = ListValidator(DataclassValidator(AdditionalGeoLocationInput)), DefaultUnset
    parking_type: OptionalUnset[ParkingType] = EnumValidator(ParkingType), DefaultUnset
    evses: OptionalUnset[List[EvseInput]] = ListValidator(DataclassValidator(EvseInput)), DefaultUnset
    directions: OptionalUnset[List[DisplayTextInput]] = ListValidator(DataclassValidator(DisplayTextInput)), DefaultUnset
    operator: OptionalUnset[BusinessDetailsInput] = DataclassValidator(BusinessDetailsInput), DefaultUnset
    suboperator: OptionalUnset[BusinessDetailsInput] = DataclassValidator(BusinessDetailsInput), DefaultUnset
    owner: OptionalUnset[BusinessDetailsInput] = DataclassValidator(BusinessDetailsInput), DefaultUnset
    facilities: OptionalUnset[List[Facility]] = ListValidator(EnumValidator(Facility)), DefaultUnset
    time_zone: str = StringValidator(max_length=255)
    opening_times: OptionalUnset[HoursInput] = DataclassValidator(HoursInput), DefaultUnset
    charging_when_closed: OptionalUnset[bool] = BooleanValidator(), DefaultUnset
    images: OptionalUnset[List[ImageInput]] = ListValidator(DataclassValidator(ImageInput)), DefaultUnset
    energy_mix: OptionalUnset[EnergyMixInput] = DataclassValidator(EnergyMixInput), DefaultUnset
    last_updated: OptionalUnset[datetime] = DateTimeValidator(
        DateTimeFormat.LOCAL_OR_UTC,
        local_timezone=timezone.utc,
        target_timezone=timezone.utc,
    ), DefaultUnset


@validataclass
class OcpiInput(ValidataclassMixin):
    status_code: int = IntegerValidator()
    timestamp: datetime = DateTimeValidator()
    data: List[LocationInput] = ListValidator(UnvalidatedDictValidator())
