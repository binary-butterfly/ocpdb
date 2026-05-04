"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .alert_c_direction_enum_g_input import AlertCDirectionEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .linear_direction_enum_g_input import LinearDirectionEnumGInput
from .multilingual_string_input import MultilingualStringInput


@validataclass
class AlertCDirectionInput(ValidataclassMixin):
    alertCDirectionCoded: AlertCDirectionEnumGInput = DataclassValidator(AlertCDirectionEnumGInput)
    alertCDirectionNamed: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    alertCAffectedDirection: LinearDirectionEnumGInput = DataclassValidator(LinearDirectionEnumGInput)
    locAlertCDirectionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
