"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class RelativeOffsetsInput(ValidataclassMixin):
    earliestStartRelative: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    latestStartRelative: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    earliestEndRelative: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    latestEndRelative: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    afacAssignedRightTimeRelativeExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    afacRelativeOffsetsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
