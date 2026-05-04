"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.alert_c_point_g_input import AlertCPointGInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.external_referencing_input import ExternalReferencingInput
from webapp.shared.datex2.v3_7.shared.junction_information_input import JunctionInformationInput
from webapp.shared.datex2.v3_7.shared.location_extension_type_g_input import LocationExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.location_reference_extension_type_g_input import (
    LocationReferenceExtensionTypeGInput,
)
from webapp.shared.datex2.v3_7.shared.openlr_point_location_reference_g_input import OpenlrPointLocationReferenceGInput
from webapp.shared.datex2.v3_7.shared.point_along_linear_element_input import PointAlongLinearElementInput
from webapp.shared.datex2.v3_7.shared.point_by_coordinates_input import PointByCoordinatesInput
from webapp.shared.datex2.v3_7.shared.point_coordinates_input import PointCoordinatesInput
from webapp.shared.datex2.v3_7.shared.supplementary_positional_description_input import (
    SupplementaryPositionalDescriptionInput,
)
from webapp.shared.datex2.v3_7.shared.tpeg_point_location_g_input import TpegPointLocationGInput


@validataclass
class PointLocationForParkingInput(ValidataclassMixin):
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
    pointAlongLinearElement: list[PointAlongLinearElementInput] | UnsetValueType = (
        ListValidator(DataclassValidator(PointAlongLinearElementInput)),
        Default(UnsetValue),
    )
    alertCPoint: list[AlertCPointGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(AlertCPointGInput)),
        Default(UnsetValue),
    )
    tpegPointLocation: TpegPointLocationGInput | UnsetValueType = (
        DataclassValidator(TpegPointLocationGInput),
        Default(UnsetValue),
    )
    openlrPointLocationReference: OpenlrPointLocationReferenceGInput | UnsetValueType = (
        DataclassValidator(OpenlrPointLocationReferenceGInput),
        Default(UnsetValue),
    )
    junctionInformation: JunctionInformationInput | UnsetValueType = (
        DataclassValidator(JunctionInformationInput),
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
    locPointLocationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    prkPointLocationForParkingExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
