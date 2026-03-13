"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .area_places_enum_g_input import AreaPlacesEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .external_referencing_input import ExternalReferencingInput
from .gml_multi_polygon_input import GmlMultiPolygonInput
from .location_extension_type_g_input import LocationExtensionTypeGInput
from .named_area_g_input import NamedAreaGInput
from .openlr_area_location_reference_g_input import OpenlrAreaLocationReferenceGInput
from .point_coordinates_input import PointCoordinatesInput


@validataclass
class AreaLocationInput:
    areasAtWhichApplicable: AreaPlacesEnumGInput | UnsetValueType = (
        DataclassValidator(AreaPlacesEnumGInput),
        Default(UnsetValue),
    )
    externalReferencing: list[ExternalReferencingInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ExternalReferencingInput)),
        Default(UnsetValue),
    )
    coordinatesForDisplay: PointCoordinatesInput | UnsetValueType = (
        DataclassValidator(PointCoordinatesInput),
        Default(UnsetValue),
    )
    namedArea: NamedAreaGInput | UnsetValueType = DataclassValidator(NamedAreaGInput), Default(UnsetValue)
    gmlMultiPolygon: GmlMultiPolygonInput | UnsetValueType = (
        DataclassValidator(GmlMultiPolygonInput),
        Default(UnsetValue),
    )
    openlrAreaLocationReference: OpenlrAreaLocationReferenceGInput | UnsetValueType = (
        DataclassValidator(OpenlrAreaLocationReferenceGInput),
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
    locAreaLocationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
