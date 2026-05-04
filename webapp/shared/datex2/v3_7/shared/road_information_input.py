"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class RoadInformationInput(ValidataclassMixin):
    roadDestination: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    roadName: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    roadNumber: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    locRoadInformationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
