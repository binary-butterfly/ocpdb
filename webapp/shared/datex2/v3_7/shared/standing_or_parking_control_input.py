"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .standing_or_parking_control_type_enum_g_input import StandingOrParkingControlTypeEnumGInput


@validataclass
class StandingOrParkingControlInput(ValidataclassMixin):
    standingOrParkingControlType: StandingOrParkingControlTypeEnumGInput = DataclassValidator(
        StandingOrParkingControlTypeEnumGInput
    )
    permittedStandingTime: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    permittedParkingTime: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    paidParking: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    troTypeOfRegulationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    troStandingOrParkingControlExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
