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

import logging
from datetime import datetime, time, timezone
from decimal import Decimal
from typing import Any
from zoneinfo import ZoneInfo

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    AnythingValidator,
    BooleanValidator,
    DataclassValidator,
    DateTimeValidator,
    EnumValidator,
    FloatToDecimalValidator,
    ListValidator,
    Noneable,
    RegexValidator,
    StringValidator,
    TimeFormat,
    TimeValidator,
)

from webapp.common.logging.models import LogMessageType
from webapp.common.validation import RoundingIntegerValidator
from webapp.common.validation.replacing_string_validator import ReplacingStringValidator
from webapp.models.evse import Capability, EvseStatus
from webapp.services.import_services.models import (
    BusinessUpdate,
    ConnectorUpdate,
    EvseUpdate,
    LocationUpdate,
    RegularHoursUpdate,
)

from .models import (
    TIME_ZONE_MAPPING,
    AccessibilityLocationType,
    AuthenticationMode,
    DynamicInfoAvailable,
    Plug,
    SwissEvseStatus,
    SwissPowerType,
    Weekday,
)

logger = logging.getLogger(__name__)


@validataclass
class EVSEData:
    EVSEDataRecord: list[dict] = ListValidator(AnythingValidator(allowed_types=[dict]))
    OperatorID: str = StringValidator()
    OperatorName: str = StringValidator()


@validataclass
class OpendataSwissStaticInput:
    EVSEData: list[EVSEData] = ListValidator(DataclassValidator(EVSEData))


@validataclass
class EvseStatusData:
    EVSEStatusRecord: list[dict] = ListValidator(AnythingValidator(allowed_types=[dict]))


@validataclass
class OpendataSwissRealtimeInput:
    EVSEStatuses: list[EvseStatusData] = ListValidator(DataclassValidator(EvseStatusData))


@validataclass
class Address:
    Street: str = ReplacingStringValidator(mapping={'\u200b': ''})
    HouseNum: str | None = StringValidator(), Default(None)
    Floor: str | None = Noneable(StringValidator()), Default(None)
    PostalCode: str | None = ReplacingStringValidator(mapping={'\xa0': ''}), Default(None)
    City: str = StringValidator()
    Country: str = StringValidator()
    TimeZone: str | None = Noneable(StringValidator()), Default(None)


@validataclass
class ChargingFacility:
    power: Decimal | None = FloatToDecimalValidator(min_value=0, allow_strings=True, allow_integers=True), Default(None)
    power_type: SwissPowerType | None = EnumValidator(SwissPowerType), Default(None)
    Amperage: int | None = RoundingIntegerValidator(min_value=0, allow_strings=True), Default(None)
    Voltage: int | None = RoundingIntegerValidator(min_value=0, allow_strings=True), Default(None)


@validataclass
class ChargingStationName:
    lang: str = StringValidator()
    value: str = StringValidator()


@validataclass
class GeoCoordinates:
    Google: str = RegexValidator(r'-?\d+.\d+ -?\d+.\d+')

    def to_lat_lon(self) -> tuple[Decimal, Decimal]:
        lat, lon = self.Google.split(' ')
        return Decimal(lat), Decimal(lon)


@validataclass
class Period:
    begin: time = TimeValidator(time_format=TimeFormat.NO_SECONDS)
    end: time = TimeValidator(time_format=TimeFormat.NO_SECONDS)


@validataclass
class OpeningTime:
    on: Weekday = EnumValidator(Weekday)
    Period: list[Period] = ListValidator(DataclassValidator(Period))

    def to_regular_hours(self) -> list[RegularHoursUpdate]:
        regular_hours: list[RegularHoursUpdate] = []
        for period in self.Period:
            if self.on == Weekday.WORKDAYS:
                # We assume that 'Workdays' means Monday until Friday.
                for i in range(1, 6):
                    regular_hours.append(
                        RegularHoursUpdate(
                            weekday=i,
                            period_begin=period.begin.hour * 3600 + period.begin.minute * 60,
                            period_end=period.end.hour * 3600 + period.end.minute * 60,
                        )
                    )
            else:
                regular_hours.append(
                    RegularHoursUpdate(
                        weekday=self.on.to_weekday(),
                        period_begin=period.begin.hour * 3600 + period.begin.minute * 60,
                        period_end=period.end.hour * 3600 + period.end.minute * 60,
                    ),
                )
        return regular_hours


@validataclass
class EVSEDataRecord:
    AccessibilityLocation: AccessibilityLocationType | None = Noneable(EnumValidator(AccessibilityLocationType))
    Address: Address = DataclassValidator(Address)
    AuthenticationModes: list[AuthenticationMode] = ListValidator(EnumValidator(AuthenticationMode))
    ChargingFacilities: list[ChargingFacility] = ListValidator(DataclassValidator(ChargingFacility))
    ChargingStationId: str = StringValidator()
    ChargingStationNames: list[ChargingStationName] | None = Noneable(
        ListValidator(DataclassValidator(ChargingStationName)),
    )
    EvseID: str = StringValidator()
    GeoCoordinates: GeoCoordinates = DataclassValidator(GeoCoordinates)
    HotlinePhoneNumber: str = StringValidator()
    lastUpdate: datetime | None = (
        DateTimeValidator(
            local_timezone=ZoneInfo('Europe/Berlin'),
            target_timezone=timezone.utc,
        ),
        Default(None),
    )
    IsOpen24Hours: bool = BooleanValidator(allow_strings=True)
    OpeningTimes: list[OpeningTime] | None = Noneable(ListValidator(DataclassValidator(OpeningTime))), Default(None)
    Plugs: list[Plug] = ListValidator(EnumValidator(Plug))
    DynamicInfoAvailable: DynamicInfoAvailable = EnumValidator(DynamicInfoAvailable)

    @staticmethod
    def __pre_validate__(input_data: Any, **kwargs) -> Any:
        # For weird reasons, ChargingStationNames is sometimes a dict, and not a list of dict. We normalize this.
        if 'ChargingStationNames' in input_data and isinstance(input_data['ChargingStationNames'], dict):
            input_data['ChargingStationNames'] = [input_data['ChargingStationNames']]

        return input_data

    def to_location_update(self, location_update: LocationUpdate | None, operator_name: str) -> LocationUpdate:
        last_updated = self.lastUpdate or datetime.now(tz=timezone.utc)
        if location_update is None:
            if self.Address.HouseNum and self.Address.HouseNum != '0':
                address = f'{self.Address.Street} {self.Address.HouseNum}'
            else:
                address = self.Address.Street

            lat, lon = self.GeoCoordinates.to_lat_lon()

            name: str | None = None
            if self.ChargingStationNames is not None:
                name = next(iter(item.value for item in self.ChargingStationNames), None)

            # Opening Times
            regular_hours: list[RegularHoursUpdate] | UnsetValueType
            if self.OpeningTimes is None or self.OpeningTimes == []:
                regular_hours = UnsetValue
            else:
                regular_hours = []
                for opening_time in self.OpeningTimes:
                    regular_hours += opening_time.to_regular_hours()

            # Check if we have all time zones registered
            if self.Address.Country not in TIME_ZONE_MAPPING:
                logger.warning(
                    f'opendata swiss country {self.Address.Country} missing in time zone mapping',
                    extra={'attributes': {'type': LogMessageType.IMPORT_LOCATION}},
                )

            location_update = LocationUpdate(
                uid=self.ChargingStationId,
                source='opendata_swiss',
                name=name,
                operator=BusinessUpdate(name=operator_name),
                twentyfourseven=self.IsOpen24Hours,
                address=address,
                postal_code=None if self.Address.PostalCode == '0' else self.Address.PostalCode,
                city=self.Address.City,
                country=self.Address.Country,
                lat=lat,
                lon=lon,
                parking_type=self.AccessibilityLocation.to_parking_type() if self.AccessibilityLocation else None,
                time_zone=self.Address.TimeZone or TIME_ZONE_MAPPING.get(self.Address.Country),
                regular_hours=regular_hours,
                last_updated=last_updated,
                evses=[],
            )

        capabilities: list[Capability] = []
        if self.AuthenticationModes:
            for mode in self.AuthenticationModes:
                capability = mode.to_capability()
                if mode.to_capability() is not None and capability not in capabilities:
                    capabilities.append(capability)

        evse_update = EvseUpdate(
            uid=self.EvseID,
            evse_id=self.EvseID,
            floor_level=self.Address.Floor,
            phone=self.HotlinePhoneNumber,
            capabilities=capabilities,
            last_updated=last_updated,
            connectors=[],
        )
        if self.DynamicInfoAvailable == DynamicInfoAvailable.FALSE:
            evse_update.status = EvseStatus.STATIC

        for i, plug in enumerate(self.Plugs):
            connector_update = ConnectorUpdate(
                uid=str(i + 1),
                standard=plug.to_standard(),
                format=plug.to_format(),
                last_updated=last_updated,
            )
            # Sometimes, there is no ChargingFacility for a plug, so we have to check before
            if len(self.ChargingFacilities) > i:
                connector_update.max_current = self.ChargingFacilities[i].Amperage
                connector_update.max_voltage = self.ChargingFacilities[i].Voltage
                if self.ChargingFacilities[i].power:
                    connector_update.max_electric_power = int(self.ChargingFacilities[i].power * 1000)

            evse_update.connectors.append(connector_update)

        location_update.evses.append(evse_update)

        return location_update


@validataclass
class EVSEStatusRecord:
    EvseID: str = StringValidator()
    EVSEStatus: SwissEvseStatus = EnumValidator(SwissEvseStatus)

    def to_evse_update(self) -> EvseUpdate:
        return EvseUpdate(
            last_updated=datetime.now(tz=timezone.utc),
            uid=self.EvseID,
            evse_id=self.EvseID,
            status=self.EVSEStatus.to_evse_status(),
        )
