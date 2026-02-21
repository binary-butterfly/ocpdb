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

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.validators import (
    AnythingValidator,
    BooleanValidator,
    DataclassValidator,
    DateTimeFormat,
    DateTimeValidator,
    DecimalValidator,
    EnumValidator,
    FloatValidator,
    IntegerValidator,
    ListValidator,
    Noneable,
    StringValidator,
    TimeFormat,
    TimeValidator,
    UrlValidator,
)

from webapp.common.validation import EmptystringToNoneable
from webapp.common.validation.replacing_string_validator import ReplacingStringValidator
from webapp.models.charging_station import Capability
from webapp.models.connector import ConnectorFormat, ConnectorType, PowerType
from webapp.models.evse import EvseStatus, ParkingRestriction
from webapp.models.image import ImageCategory
from webapp.models.location import EnergySourceCategory, EnvironmentalImpactCategory, Facility, ParkingType


@validataclass
class ConnectorInput(ValidataclassMixin):
    id: str = StringValidator(max_length=36)
    standard: ConnectorType = EnumValidator(ConnectorType)
    format: ConnectorFormat = EnumValidator(ConnectorFormat)
    power_type: PowerType = EnumValidator(PowerType)
    max_voltage: int = IntegerValidator()
    max_amperage: int = IntegerValidator()
    max_electric_power: int | None = IntegerValidator(), Default(None)
    tariff_ids: list[str] | None = ListValidator(StringValidator(max_length=36)), Default(None)
    terms_and_conditions: str | None = UrlValidator(max_length=255), Default(None)
    last_updated: datetime = DateTimeValidator(
        DateTimeFormat.LOCAL_OR_UTC,
        local_timezone=timezone.utc,
        target_timezone=timezone.utc,
    )


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
    period_begin: datetime = (
        DateTimeValidator(
            DateTimeFormat.LOCAL_OR_UTC,
            local_timezone=timezone.utc,
            target_timezone=timezone.utc,
        ),
        Default(None),
    )
    period_end: datetime = DateTimeValidator(
        DateTimeFormat.LOCAL_OR_UTC,
        local_timezone=timezone.utc,
        target_timezone=timezone.utc,
    )


@validataclass
class HoursInput(ValidataclassMixin):
    twentyfourseven: bool = BooleanValidator()
    regular_hours: list[RegularHoursInput] | None = (
        ListValidator(DataclassValidator(RegularHoursInput)),
        Default(None),
    )
    exceptional_openings: list[ExceptionalPeriodInput] | None = (
        ListValidator(DataclassValidator(ExceptionalPeriodInput)),
        Default(None),
    )
    exceptional_closings: list[ExceptionalPeriodInput] | None = (
        ListValidator(DataclassValidator(ExceptionalPeriodInput)),
        Default(None),
    )


@validataclass
class StatusScheduleInput(ValidataclassMixin):
    period_begin: datetime = DateTimeValidator(
        DateTimeFormat.LOCAL_OR_UTC,
        local_timezone=timezone.utc,
        target_timezone=timezone.utc,
    )
    period_end: datetime | None = (
        DateTimeValidator(
            DateTimeFormat.LOCAL_OR_UTC,
            local_timezone=timezone.utc,
            target_timezone=timezone.utc,
        ),
        Default(None),
    )
    status: EvseStatus = EnumValidator(EvseStatus)


@validataclass
class GeoLocationInput(ValidataclassMixin):
    latitude: Decimal = DecimalValidator()
    longitude: Decimal = DecimalValidator()


@validataclass
class DisplayTextInput(ValidataclassMixin):
    language: str = StringValidator(min_length=2, max_length=2)
    text: str = ReplacingStringValidator(
        mapping={'\r': '', '\n': ' ', '\xa0': ' '},
        normalize_spaces=True,
        max_length=512,
    )


@validataclass
class AdditionalGeoLocationInput(ValidataclassMixin):
    name: DisplayTextInput | None = DataclassValidator(DisplayTextInput), Default(None)
    latitude: Decimal = DecimalValidator()
    longitude: Decimal = DecimalValidator()


@validataclass
class ImageInput(ValidataclassMixin):
    url: str = StringValidator(max_length=255)
    thumbnail: str | None = StringValidator(max_length=255), Default(None)
    category: ImageCategory = EnumValidator(ImageCategory)
    type: str = StringValidator(max_length=4)
    width: int | None = IntegerValidator(), Default(None)
    height: int | None = IntegerValidator(), Default(None)


@validataclass
class BusinessDetailsInput(ValidataclassMixin):
    name: str = StringValidator(max_length=100)
    # From OCPI perspective, emptystring would be invalid, but many sources fail at this, and it's clear what is meant
    website: str | None = EmptystringToNoneable(UrlValidator()), Default(None)
    logo: ImageInput | None = DataclassValidator(ImageInput), Default(None)


@validataclass
class EnergySourceInput(ValidataclassMixin):
    source: EnergySourceCategory = EnumValidator(EnergySourceCategory)
    percentage: float = FloatValidator()


@validataclass
class EnvironmentalImpactInput(ValidataclassMixin):
    category: EnvironmentalImpactCategory = EnumValidator(EnvironmentalImpactCategory), Default(None)
    amount: float = FloatValidator()


@validataclass
class EnergyMixInput(ValidataclassMixin):
    is_green_energy: bool = BooleanValidator()
    energy_sources: list[EnergySourceInput] | None = (
        ListValidator(DataclassValidator(EnergySourceInput)),
        Default(None),
    )
    environ_impact: list[EnvironmentalImpactInput] | None = (
        ListValidator(DataclassValidator(EnvironmentalImpactInput)),
        Default(None),
    )
    supplier_name: str | None = StringValidator(max_length=64), Default(None)
    energy_product_name: str | None = StringValidator(max_length=64), Default(None)


@validataclass
class EvseInput(ValidataclassMixin):
    uid: str = StringValidator(max_length=36)
    evse_id: str = StringValidator(max_length=36)
    status: EvseStatus = EnumValidator(EvseStatus)
    status_schedule: list[StatusScheduleInput] | None = (
        ListValidator(DataclassValidator(StatusScheduleInput)),
        Default(None),
    )
    capabilities: list[Capability] | None = ListValidator(EnumValidator(Capability)), Default(None)
    connectors: list[ConnectorInput] = ListValidator(DataclassValidator(ConnectorInput), min_length=1), Default([])
    floor_level: str | None = Noneable(StringValidator(max_length=4)), Default(None)
    coordinates: GeoLocationInput | None = DataclassValidator(GeoLocationInput), Default(None)
    physical_reference: str | None = Noneable(StringValidator(max_length=16)), Default(None)
    directions: list[DisplayTextInput] | None = (
        ListValidator(DataclassValidator(DisplayTextInput)),
        Default(None),
    )
    parking_restrictions: list[ParkingRestriction] | None = (
        ListValidator(EnumValidator(ParkingRestriction)),
        Default(None),
    )
    images: list[ImageInput] | None = ListValidator(DataclassValidator(ImageInput)), Default(None)
    last_updated: datetime = DateTimeValidator(
        DateTimeFormat.LOCAL_OR_UTC,
        local_timezone=timezone.utc,
        target_timezone=timezone.utc,
    )


@validataclass
class LocationInput(ValidataclassMixin):
    id: str = StringValidator(max_length=36)
    name: str | None = StringValidator(max_length=100), Default(None)
    address: str = StringValidator(max_length=45)
    city: str = StringValidator(max_length=45)
    postal_code: str | None = StringValidator(max_length=10), Default(None)
    state: str | None = StringValidator(max_length=20), Default(None)
    country: str = StringValidator(min_length=3, max_length=3)
    coordinates: GeoLocationInput = DataclassValidator(GeoLocationInput)
    related_locations: list[AdditionalGeoLocationInput] | None = (
        ListValidator(DataclassValidator(AdditionalGeoLocationInput)),
        Default(None),
    )
    parking_type: ParkingType | None = EnumValidator(ParkingType), Default(None)
    evses: list[EvseInput] = ListValidator(DataclassValidator(EvseInput)), Default([])
    directions: list[DisplayTextInput] | None = (
        ListValidator(DataclassValidator(DisplayTextInput)),
        Default(None),
    )
    operator: BusinessDetailsInput | None = DataclassValidator(BusinessDetailsInput), Default(None)
    suboperator: BusinessDetailsInput | None = DataclassValidator(BusinessDetailsInput), Default(None)
    owner: BusinessDetailsInput | None = DataclassValidator(BusinessDetailsInput), Default(None)
    facilities: list[Facility] | None = ListValidator(EnumValidator(Facility)), Default(None)
    time_zone: str = StringValidator(max_length=255)
    opening_times: HoursInput | None = DataclassValidator(HoursInput), Default(None)
    charging_when_closed: bool | None = BooleanValidator(), Default(None)
    images: list[ImageInput] | None = ListValidator(DataclassValidator(ImageInput)), Default(None)
    energy_mix: EnergyMixInput | None = DataclassValidator(EnergyMixInput), Default(None)
    last_updated: datetime | None = DateTimeValidator(
        DateTimeFormat.LOCAL_OR_UTC,
        local_timezone=timezone.utc,
        target_timezone=timezone.utc,
    )


@validataclass
class OcpiInput(ValidataclassMixin):
    status_code: int = IntegerValidator()
    timestamp: datetime = DateTimeValidator()
    data: list[dict] = ListValidator(AnythingValidator(allowed_types=[dict]))
