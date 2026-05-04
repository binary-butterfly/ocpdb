"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .activity_enum_g_input import ActivityEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .regulation_enum_g_input import RegulationEnumGInput


@validataclass
class PermitsAndProhibitionsInput(ValidataclassMixin):
    activity: ActivityEnumGInput = DataclassValidator(ActivityEnumGInput)
    regulation: RegulationEnumGInput = DataclassValidator(RegulationEnumGInput)
    prkPermitsAndProhibitionsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
