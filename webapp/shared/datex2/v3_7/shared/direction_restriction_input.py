"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator

from .direction_restriction_type_enum_g_input import DirectionRestrictionTypeEnumGInput
from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class DirectionRestrictionInput(ValidataclassMixin):
    directionToBeFollowed: DirectionRestrictionTypeEnumGInput = DataclassValidator(DirectionRestrictionTypeEnumGInput)
    respectBicycle: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    respectPedestrian: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    respectMotorisedPersonalTransportDevices: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    troTypeOfRegulationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    troDirectionRestrictionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
