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
from .openlr_point_location_reference_g_input import OpenlrPointLocationReferenceGInput
from .point_by_coordinates_input import PointByCoordinatesInput
from .point_coordinates_input import PointCoordinatesInput
from .supplementary_positional_description_input import SupplementaryPositionalDescriptionInput


@validataclass
class PointLocationInput:
    externalReferencing: list[ExternalReferencingInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ExternalReferencingInput)),
        Default(UnsetValue),
    )
    coordinatesForDisplay: PointCoordinatesInput | UnsetValueType = (
        DataclassValidator(PointCoordinatesInput),
        Default(UnsetValue),
    )
    supplementaryPositionalDescription: SupplementaryPositionalDescriptionInput | UnsetValueType = (
        DataclassValidator(SupplementaryPositionalDescriptionInput),
        Default(UnsetValue),
    )
    pointByCoordinates: PointByCoordinatesInput | UnsetValueType = (
        DataclassValidator(PointByCoordinatesInput),
        Default(UnsetValue),
    )
    openlrPointLocationReference: OpenlrPointLocationReferenceGInput | UnsetValueType = (
        DataclassValidator(OpenlrPointLocationReferenceGInput),
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
    locNetworkLocationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locPointLocationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
