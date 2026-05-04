"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .status_configuration_input import StatusConfigurationInput


@validataclass
class ThresholdConfigurationInput(ValidataclassMixin):
    lastMaximumOccupancy: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    statusConfiguration: list[StatusConfigurationInput] = ListValidator(DataclassValidator(StatusConfigurationInput))
    prkThresholdConfigurationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
