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
from enum import Enum
from typing import Any

from validataclass.dataclasses import Default, DefaultFactory, validataclass
from validataclass.exceptions import ValidationError
from validataclass.validators import (
    AnythingValidator,
    BooleanValidator,
    DataclassValidator,
    DateTimeFormat,
    DateTimeValidator,
    DecimalValidator,
    EnumValidator,
    IntegerValidator,
    ListValidator,
    Noneable,
    StringValidator,
    TimeFormat,
    TimeValidator,
    UrlValidator,
)

from .ochp_models import (
    OchpAuthMethodType,
    OchpChargePointType,
    OchpConnectorFormat,
    OchpConnectorStandard,
    OchpGeoType,
    OchpImageCategory,
    OchpLocationType,
    OchpMajorStatus,
    OchpMinorStatus,
    OchpParkingRestrictionType,
    OchpRelatedResourceType,
    OchpStaticStatus,
)


class OchpDateTimeValidator(DateTimeValidator):
    def __init__(self):
        super().__init__(
            datetime_format=DateTimeFormat.REQUIRE_UTC,
            local_timezone=timezone.utc,
            target_timezone=timezone.utc,
        )


class OchpEnumValidator(EnumValidator):
    def validate(self, input_data: Any, **kwargs) -> Enum:
        if type(input_data) is str:
            input_data = input_data.replace('-', '_')
        return super().validate(input_data)


@validataclass
class ImageInput:
    uri: str = UrlValidator(max_length=255)
    thumbUri: str | None = UrlValidator(max_length=255), Default(None)
    type: str = StringValidator(max_length=4)
    class_: OchpImageCategory = OchpEnumValidator(OchpImageCategory)
    width: int | None = IntegerValidator(min_value=1, allow_strings=True), Default(None)
    height: int | None = IntegerValidator(min_value=1, allow_strings=True), Default(None)


@validataclass
class RegularHoursInput:
    weekday: int = IntegerValidator(min_value=1, max_value=7, allow_strings=True)
    periodBegin: time = TimeValidator(time_format=TimeFormat.NO_SECONDS)
    periodEnd: time = TimeValidator(time_format=TimeFormat.NO_SECONDS)


@validataclass
class ExceptionalPeriodInput:
    periodBegin: datetime = OchpDateTimeValidator()
    periodEnd: datetime = OchpDateTimeValidator()


@validataclass
class RelatedResourceInput:
    uri: str = UrlValidator(max_length=255)
    class_: list[OchpRelatedResourceType] = (
        ListValidator(OchpEnumValidator(OchpRelatedResourceType)),
        DefaultFactory(list),
    )


@validataclass
class AddressInput:
    houseNumber: str | None = StringValidator(max_length=6), Default(None)
    address: str = StringValidator(max_length=45)
    city: str = StringValidator(max_length=45)
    zipCode: str = StringValidator(max_length=10)
    country: str = StringValidator(min_length=3, max_length=3)


@validataclass
class GeoPointInput:
    lat: Decimal = DecimalValidator(min_value=-90, max_value=90)
    lon: Decimal = DecimalValidator(min_value=-180, max_value=180)


@validataclass
class AdditionalGeoPoint:
    lat: Decimal = DecimalValidator(min_value=-90, max_value=90)
    lon: Decimal = DecimalValidator(min_value=-180, max_value=180)
    name: str | None = StringValidator(max_length=255), Default(None)
    type: OchpGeoType = OchpEnumValidator(OchpGeoType)


@validataclass
class OpeningTimesInput:
    regularHours: list[RegularHoursInput] | None = (
        ListValidator(DataclassValidator(RegularHoursInput)),
        Default(None),
    )
    twentyfourseven: bool | None = BooleanValidator(allow_strings=True), Default(None)
    closedCharging: bool = BooleanValidator(allow_strings=True)
    exceptionalOpenings: list[ExceptionalPeriodInput] = (
        ListValidator(DataclassValidator(ExceptionalPeriodInput)),
        DefaultFactory(list),
    )
    exceptionalClosings: list[ExceptionalPeriodInput] = (
        ListValidator(DataclassValidator(ExceptionalPeriodInput)),
        DefaultFactory(list),
    )

    def __post_init__(self):
        if (self.regularHours is None and self.twentyfourseven is None) or (
            self.regularHours is not None and self.twentyfourseven is not None
        ):
            raise ValidationError(code='only one of regularHours and twentyfourseven must be set')


@validataclass
class ScheduleInput:
    startDate: datetime = OchpDateTimeValidator()
    endDate: datetime | None = OchpDateTimeValidator(), Default(None)
    status: OchpStaticStatus = OchpEnumValidator(OchpStaticStatus)


@validataclass
class ConnectorInput:
    connectorStandard: OchpConnectorStandard = OchpEnumValidator(OchpConnectorStandard)
    connectorFormat: OchpConnectorFormat = OchpEnumValidator(OchpConnectorFormat)
    tariffId: str | None = StringValidator(max_length=64), Default(None)


@validataclass
class RatingsInput:
    maximumPower: Decimal = DecimalValidator()
    guaranteedPower: Decimal | None = DecimalValidator(), Default(None)
    nominalVoltage: int | None = IntegerValidator(allow_strings=True), Default(None)


@validataclass
class ChargePointInput:
    evseId: str = StringValidator(max_length=64)
    locationId: str = StringValidator(max_length=15)
    timestamp: datetime | None = OchpDateTimeValidator(), Default(None)
    locationName: str = StringValidator(max_length=100)
    locationNameLang: str = StringValidator(min_length=3, max_length=3)
    images: list[ImageInput] = ListValidator(DataclassValidator(ImageInput)), DefaultFactory(list)
    relatedResource: list[RelatedResourceInput] = (
        ListValidator(DataclassValidator(RelatedResourceInput)),
        DefaultFactory(list),
    )
    chargePointAddress: AddressInput = DataclassValidator(AddressInput)
    chargePointLocation: GeoPointInput = DataclassValidator(GeoPointInput)
    relatedLocation: list[AdditionalGeoPoint] | None = (
        ListValidator(DataclassValidator(AdditionalGeoPoint)),
        Default(None),
    )
    timeZone: str = StringValidator(max_length=255)
    openingTimes: OpeningTimesInput | None = DataclassValidator(OpeningTimesInput), Default(None)
    status: OchpStaticStatus | None = OchpEnumValidator(OchpStaticStatus), Default(None)
    statusSchedule: list[ScheduleInput] | None = ListValidator(DataclassValidator(ScheduleInput)), Default(None)
    telephoneNumber: str | None = StringValidator(max_length=20), Default(None)
    location: OchpLocationType = OchpEnumValidator(OchpLocationType)
    parkingRestriction: list[OchpParkingRestrictionType] = (
        ListValidator(OchpEnumValidator(OchpParkingRestrictionType)),
        DefaultFactory(list),
    )
    authMethods: list[OchpAuthMethodType] = ListValidator(OchpEnumValidator(OchpAuthMethodType)), DefaultFactory(list)
    connectors: list[ConnectorInput] = ListValidator(DataclassValidator(ConnectorInput), min_length=1)
    chargePointType: OchpChargePointType = OchpEnumValidator(OchpChargePointType)
    ratings: RatingsInput | None = DataclassValidator(RatingsInput), Default(None)
    userInterfaceLang: list[str] = ListValidator(StringValidator(min_length=3, max_length=3)), DefaultFactory(list)
    maxReservation: Decimal | None = DecimalValidator(), Default(None)


@validataclass
class ChargePointStatusInput:
    evseId: str = StringValidator(max_length=64)
    major: OchpMajorStatus = OchpEnumValidator(OchpMajorStatus)
    minor: OchpMinorStatus | None = OchpEnumValidator(OchpMinorStatus), Default(None)
    ttl: datetime | None = OchpDateTimeValidator(), Default(None)


@validataclass
class GetChargePointListResultCodeInput:
    resultCode: str = StringValidator()


@validataclass
class GetChargePointListResultInput:
    resultCode: GetChargePointListResultCodeInput = DataclassValidator(GetChargePointListResultCodeInput)
    resultDescription: str = StringValidator()


@validataclass
class GetChargePointListResponseInput:
    result: GetChargePointListResultInput = DataclassValidator(GetChargePointListResultInput)
    chargePointInfoArray: list[dict] = ListValidator(AnythingValidator(allowed_types=[dict]))


@validataclass
class GetChargePointListBodyInput:
    GetChargePointListResponse: GetChargePointListResponseInput = DataclassValidator(GetChargePointListResponseInput)


@validataclass
class GetChargePointListEnvelopeInput:
    Body: GetChargePointListBodyInput = DataclassValidator(GetChargePointListBodyInput)


@validataclass
class GetChargePointListInput:
    Envelope: GetChargePointListEnvelopeInput = DataclassValidator(GetChargePointListEnvelopeInput)


@validataclass
class GetStatusEvseInput:
    evse: list[dict] = ListValidator(AnythingValidator(allowed_types=[dict]))


@validataclass
class GetStatusResponseInput:
    GetStatusResponse: GetStatusEvseInput | None = Noneable(DataclassValidator(GetStatusEvseInput))


@validataclass
class GetStatusBodyInput:
    Body: GetStatusResponseInput = DataclassValidator(GetStatusResponseInput)


@validataclass
class GetStatusEnvelopeInput:
    Envelope: GetStatusBodyInput = DataclassValidator(GetStatusBodyInput)
