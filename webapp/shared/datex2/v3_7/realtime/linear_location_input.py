"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.external_referencing_input import ExternalReferencingInput
from webapp.shared.datex2.v3_7.shared.gml_line_string_g_input import GmlLineStringGInput
from webapp.shared.datex2.v3_7.shared.location_extension_type_g_input import LocationExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.location_reference_extension_type_g_input import (
    LocationReferenceExtensionTypeGInput,
)
from webapp.shared.datex2.v3_7.shared.openlr_linear_input import OpenlrLinearInput
from webapp.shared.datex2.v3_7.shared.point_coordinates_input import PointCoordinatesInput
from webapp.shared.datex2.v3_7.shared.supplementary_positional_description_input import (
    SupplementaryPositionalDescriptionInput,
)

from .destination_g_input import DestinationGInput


@validataclass
class LinearLocationInput(ValidataclassMixin):
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
    destination: DestinationGInput | UnsetValueType = DataclassValidator(DestinationGInput), Default(UnsetValue)
    openlrLinear: OpenlrLinearInput | UnsetValueType = DataclassValidator(OpenlrLinearInput), Default(UnsetValue)
    gmlLineString: GmlLineStringGInput | UnsetValueType = DataclassValidator(GmlLineStringGInput), Default(UnsetValue)
    secondarySupplementaryDescription: SupplementaryPositionalDescriptionInput | UnsetValueType = (
        DataclassValidator(SupplementaryPositionalDescriptionInput),
        Default(UnsetValue),
    )
    locLocationReferenceExtensionG: LocationReferenceExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(LocationReferenceExtensionTypeGInput),
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
    locLinearLocationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
