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
from typing import Any, List, Optional

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
    thumbUri: Optional[str] = UrlValidator(max_length=255), Default(None)
    type: str = StringValidator(max_length=4)
    class_: OchpImageCategory = OchpEnumValidator(OchpImageCategory)
    width: Optional[int] = IntegerValidator(min_value=1, allow_strings=True), Default(None)
    height: Optional[int] = IntegerValidator(min_value=1, allow_strings=True), Default(None)


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
    class_: List[OchpRelatedResourceType] \
        = ListValidator(OchpEnumValidator(OchpRelatedResourceType)), DefaultFactory(lambda: [])


@validataclass
class AddressInput:
    houseNumber: Optional[str] = StringValidator(max_length=6), Default(None)
    address: str = StringValidator(max_length=45)
    city: str = StringValidator(max_length=45)
    zipCode: str = StringValidator(max_length=10)
    country: str = StringValidator(min_length=3, max_length=3)


@validataclass
class GeoPointInput:
    lat: Decimal = DecimalValidator()
    lon: Decimal = DecimalValidator()


@validataclass
class AdditionalGeoPoint:
    lat: Decimal = DecimalValidator()
    lon: Decimal = DecimalValidator()
    name: Optional[str] = StringValidator(max_length=255), Default(None)
    type: OchpGeoType = OchpEnumValidator(OchpGeoType)


@validataclass
class OpeningTimesInput:
    regularHours: Optional[List[RegularHoursInput]] = ListValidator(DataclassValidator(RegularHoursInput)), Default(None)
    twentyfourseven: Optional[bool] = BooleanValidator(allow_strings=True), Default(None)
    closedCharging: bool = BooleanValidator(allow_strings=True)
    exceptionalOpenings: List[ExceptionalPeriodInput] \
        = ListValidator(DataclassValidator(ExceptionalPeriodInput)), DefaultFactory(lambda: [])
    exceptionalClosings: List[ExceptionalPeriodInput] \
        = ListValidator(DataclassValidator(ExceptionalPeriodInput)), DefaultFactory(lambda: [])

    def __post_init__(self):
        if (self.regularHours is None and self.twentyfourseven is None) \
                or (self.regularHours is not None and self.twentyfourseven is not None):
            raise ValidationError(code='only one of regularHours and twentyfourseven must be set')


@validataclass
class ScheduleInput:
    startDate: datetime = OchpDateTimeValidator()
    endDate: Optional[datetime] = OchpDateTimeValidator(), Default(None)
    status: OchpStaticStatus = OchpEnumValidator(OchpStaticStatus)


@validataclass
class ConnectorInput:
    connectorStandard: OchpConnectorStandard = OchpEnumValidator(OchpConnectorStandard)
    connectorFormat: OchpConnectorFormat = OchpEnumValidator(OchpConnectorFormat)
    tariffId: Optional[str] = StringValidator(max_length=64), Default(None)


@validataclass
class RatingsInput:
    maximumPower: Decimal = DecimalValidator()
    guaranteedPower: Optional[Decimal] = DecimalValidator(), Default(None)
    nominalVoltage: Optional[int] = IntegerValidator(allow_strings=True), Default(None)


@validataclass
class ChargePointInput:
    evseId: str = StringValidator(max_length=64)
    locationId: str = StringValidator(max_length=15)
    timestamp: Optional[datetime] = OchpDateTimeValidator(), Default(None)
    locationName: str = StringValidator(max_length=100)
    locationNameLang: str = StringValidator(min_length=3, max_length=3)
    images: List[ImageInput] = ListValidator(DataclassValidator(ImageInput)), DefaultFactory(lambda: [])
    relatedResource: List[RelatedResourceInput] = ListValidator(DataclassValidator(RelatedResourceInput)), DefaultFactory(lambda: [])
    chargePointAddress: AddressInput = DataclassValidator(AddressInput)
    chargePointLocation: GeoPointInput = DataclassValidator(GeoPointInput)
    relatedLocation: Optional[List[AdditionalGeoPoint]] = ListValidator(DataclassValidator(AdditionalGeoPoint)), Default(None)
    timeZone: str = StringValidator(max_length=255)
    openingTimes: Optional[OpeningTimesInput] = DataclassValidator(OpeningTimesInput), Default(None)
    status: Optional[OchpStaticStatus] = OchpEnumValidator(OchpStaticStatus), Default(None)
    statusSchedule: Optional[List[ScheduleInput]] = ListValidator(DataclassValidator(ScheduleInput)), Default(None)
    telephoneNumber: Optional[str] = StringValidator(max_length=20), Default(None)
    location: OchpLocationType = OchpEnumValidator(OchpLocationType)
    parkingRestriction: List[OchpParkingRestrictionType] \
        = ListValidator(OchpEnumValidator(OchpParkingRestrictionType)), DefaultFactory(lambda: [])
    authMethods: List[OchpAuthMethodType] = ListValidator(OchpEnumValidator(OchpAuthMethodType)), DefaultFactory(lambda: [])
    connectors: List[ConnectorInput] = ListValidator(DataclassValidator(ConnectorInput), min_length=1)
    chargePointType: OchpChargePointType = OchpEnumValidator(OchpChargePointType)
    ratings: Optional[RatingsInput] = DataclassValidator(RatingsInput), Default(None)
    userInterfaceLang: List[str] = ListValidator(StringValidator(min_length=3, max_length=3)), DefaultFactory(lambda: [])
    maxReservation: Optional[Decimal] = DecimalValidator(), Default(None)


@validataclass
class ChargePointStatusInput:
    evseId: str = StringValidator(max_length=64)
    major: OchpMajorStatus = OchpEnumValidator(OchpMajorStatus)
    minor: Optional[OchpMinorStatus] = OchpEnumValidator(OchpMinorStatus), Default(None)
    ttl: Optional[datetime] = OchpDateTimeValidator(), Default(None)

    def __post_init__(self):
        if self.major == OchpMajorStatus.available and self.minor not in [OchpMinorStatus.available, OchpMinorStatus.reserved]:
            raise ValidationError(code='invalid_minor')
        if self.major == OchpMajorStatus.available \
                and self.minor in [OchpMinorStatus.charging, OchpMinorStatus.blocked, OchpMinorStatus.reserved, OchpMinorStatus.outoforder]:
            raise ValidationError(code='invalid_minor')
        if self.major == OchpMajorStatus.unknown and self.minor is not None:
            raise ValidationError(code='invalid_minor')


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
    chargePointInfoArray: List[dict] = ListValidator(AnythingValidator(allowed_types=[dict]))


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
    evse: List[dict] = ListValidator(AnythingValidator(allowed_types=[dict]))


@validataclass
class GetStatusResponseInput:
    GetStatusResponse: List[GetStatusEvseInput] = DataclassValidator(GetStatusEvseInput)


@validataclass
class GetStatusBodyInput:
    Body: GetStatusResponseInput = DataclassValidator(GetStatusResponseInput)


@validataclass
class GetStatusEnvelopeInput:
    Envelope: GetStatusBodyInput = DataclassValidator(GetStatusBodyInput)

