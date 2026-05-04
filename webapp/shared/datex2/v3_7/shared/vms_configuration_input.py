"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .vms_configuration_display_area_index_display_area_g_input import vmsConfigurationDisplayAreaIndexDisplayAreaGInput


@validataclass
class VmsConfigurationInput(ValidataclassMixin):
    numberOfDisplayAreas: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    displayArea: list[vmsConfigurationDisplayAreaIndexDisplayAreaGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(vmsConfigurationDisplayAreaIndexDisplayAreaGInput)),
        Default(UnsetValue),
    )
    vmsVmsConfigurationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
