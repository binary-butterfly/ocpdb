"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, StringValidator

from .condition_g_input import ConditionGInput
from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class PredefinedConditionInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    condition: ConditionGInput = DataclassValidator(ConditionGInput)
    troPredefinedConditionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
