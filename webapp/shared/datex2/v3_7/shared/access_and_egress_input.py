"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .operating_hours_g_input import OperatingHoursGInput


@validataclass
class AccessAndEgressInput(ValidataclassMixin):
    exitPossibleAtAnyTime: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    openTime: OperatingHoursGInput | UnsetValueType = DataclassValidator(OperatingHoursGInput), Default(UnsetValue)
    entranceOpenTime: OperatingHoursGInput | UnsetValueType = (
        DataclassValidator(OperatingHoursGInput),
        Default(UnsetValue),
    )
    exitOpenTime: OperatingHoursGInput | UnsetValueType = DataclassValidator(OperatingHoursGInput), Default(UnsetValue)
    prkAccessAndEgressExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
