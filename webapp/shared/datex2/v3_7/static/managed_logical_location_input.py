"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput

from .location_g_input import LocationGInput


@validataclass
class ManagedLogicalLocationInput(ValidataclassMixin):
    managedLogicalLocation: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    distanceFromLogicalLocation: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    managedLocation: LocationGInput | UnsetValueType = DataclassValidator(LocationGInput), Default(UnsetValue)
    vmsManagedLogicalLocationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
