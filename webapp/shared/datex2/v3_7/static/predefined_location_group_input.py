"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput

from .location_group_g_input import LocationGroupGInput
from .predefined_location_input import PredefinedLocationInput


@validataclass
class PredefinedLocationGroupInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    predefinedLocationGroupName: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    locationGroup: LocationGroupGInput | UnsetValueType = DataclassValidator(LocationGroupGInput), Default(UnsetValue)
    predefinedLocation: list[PredefinedLocationInput] | UnsetValueType = (
        ListValidator(DataclassValidator(PredefinedLocationInput)),
        Default(UnsetValue),
    )
    locPredefinedLocationReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locPredefinedLocationGroupExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
