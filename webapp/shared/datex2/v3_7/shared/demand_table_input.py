"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, DateTimeValidator, ListValidator, StringValidator

from .demand_space_type_input import DemandSpaceTypeInput
from .demand_type_input import DemandTypeInput
from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class DemandTableInput(ValidataclassMixin):
    frequency: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    timestamp: datetime = DateTimeValidator()
    demandType: list[DemandTypeInput] | UnsetValueType = (
        ListValidator(DataclassValidator(DemandTypeInput)),
        Default(UnsetValue),
    )
    demandSpaceType: list[DemandSpaceTypeInput] | UnsetValueType = (
        ListValidator(DataclassValidator(DemandSpaceTypeInput)),
        Default(UnsetValue),
    )
    prkDemandTableExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
