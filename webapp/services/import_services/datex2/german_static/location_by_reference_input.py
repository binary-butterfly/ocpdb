"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .external_referencing_input import ExternalReferencingInput
from .location_extension_type_g_input import LocationExtensionTypeGInput
from .point_coordinates_input import PointCoordinatesInput
from .predefined_location_versioned_reference_g_input import PredefinedLocationVersionedReferenceGInput


@validataclass
class LocationByReferenceInput:
    predefinedLocationReference: PredefinedLocationVersionedReferenceGInput = DataclassValidator(
        PredefinedLocationVersionedReferenceGInput
    )
    externalReferencing: list[ExternalReferencingInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ExternalReferencingInput)),
        Default(UnsetValue),
    )
    coordinatesForDisplay: PointCoordinatesInput | UnsetValueType = (
        DataclassValidator(PointCoordinatesInput),
        Default(UnsetValue),
    )
    locLocationReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locLocationExtensionG: LocationExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(LocationExtensionTypeGInput),
        Default(UnsetValue),
    )
    locLocationByReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
