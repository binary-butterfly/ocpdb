"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput

from .itinerary_g_input import ItineraryGInput
from .predefined_location_input import PredefinedLocationInput


@validataclass
class PredefinedItineraryInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    predefinedItineraryName: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    itinerary: ItineraryGInput | UnsetValueType = DataclassValidator(ItineraryGInput), Default(UnsetValue)
    predefinedLocation: list[PredefinedLocationInput] | UnsetValueType = (
        ListValidator(DataclassValidator(PredefinedLocationInput)),
        Default(UnsetValue),
    )
    locPredefinedLocationReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locPredefinedItineraryExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
