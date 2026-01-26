"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class ClosureInformationInput:
    permananentlyClosed: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    temporarilyClosed: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    closedFrom: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    temporarilyClosedUntil: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    afacClosureInformationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
