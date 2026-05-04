"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    DataclassValidator,
    DateTimeValidator,
    FloatValidator,
    ListValidator,
    RegexValidator,
    StringValidator,
)

from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .public_transport_type_enum_g_input import PublicTransportTypeEnumGInput
from .public_transport_vehicle_type_g_input import PublicTransportVehicleTypeGInput
from .validity_input import ValidityInput


@validataclass
class PublicTransportScheduleInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    lastUpdated: datetime = DateTimeValidator()
    line: list[str] | UnsetValueType = ListValidator(StringValidator()), Default(UnsetValue)
    nextDepartures: list[str] | UnsetValueType = (
        ListValidator(
            RegexValidator(
                pattern=r'^(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?|(24:00:00(\.0+)?))(Z|(\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))?$'
            )
        ),
        Default(UnsetValue),
    )
    destination: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    interval: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    travelTimeToDestination: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    ptType: list[PublicTransportTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(PublicTransportTypeEnumGInput)),
        Default(UnsetValue),
    )
    ptVehicleType: PublicTransportVehicleTypeGInput | UnsetValueType = (
        DataclassValidator(PublicTransportVehicleTypeGInput),
        Default(UnsetValue),
    )
    ptVehicleName: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    ptOperator: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    validity: ValidityInput | UnsetValueType = DataclassValidator(ValidityInput), Default(UnsetValue)
    prkPublicTransportScheduleExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
