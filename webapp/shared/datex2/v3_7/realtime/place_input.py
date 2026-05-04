"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    DataclassValidator,
    DateTimeValidator,
    IntegerValidator,
    ListValidator,
    StringValidator,
)

from webapp.shared.datex2.v3_7.shared.accessibility_enum_g_input import AccessibilityEnumGInput
from webapp.shared.datex2.v3_7.shared.associated_facility_g_input import AssociatedFacilityGInput
from webapp.shared.datex2.v3_7.shared.dimension_input import DimensionInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.facility_object_versioned_reference_g_input import (
    FacilityObjectVersionedReferenceGInput,
)
from webapp.shared.datex2.v3_7.shared.hierarchy_element_type_enum_g_input import HierarchyElementTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.image_input import ImageInput
from webapp.shared.datex2.v3_7.shared.layout_enum_g_input import LayoutEnumGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.occupancy_level_input import OccupancyLevelInput
from webapp.shared.datex2.v3_7.shared.operating_hours_g_input import OperatingHoursGInput
from webapp.shared.datex2.v3_7.shared.operator_defined_place_versioned_reference_g_input import (
    OperatorDefinedPlaceVersionedReferenceGInput,
)
from webapp.shared.datex2.v3_7.shared.supply_input import SupplyInput
from webapp.shared.datex2.v3_7.shared.url_link_input import UrlLinkInput

from .common_components_input import CommonComponentsInput
from .location_reference_g_input import LocationReferenceGInput
from .operator_defined_place_input import OperatorDefinedPlaceInput
from .organisation_g_input import OrganisationGInput
from .rates_g_input import RatesGInput
from .responsibility_role_assignment_input import ResponsibilityRoleAssignmentInput
from .supplemental_facility_g_input import SupplementalFacilityGInput
from .vehicle_characteristics_input import VehicleCharacteristicsInput


@validataclass
class PlaceInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    name: MultilingualStringInput | UnsetValueType = DataclassValidator(MultilingualStringInput), Default(UnsetValue)
    alias: list[MultilingualStringInput] | UnsetValueType = (
        ListValidator(DataclassValidator(MultilingualStringInput)),
        Default(UnsetValue),
    )
    externalIdentifier: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    lastUpdated: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    description: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    accessibility: list[AccessibilityEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(AccessibilityEnumGInput)),
        Default(UnsetValue),
    )
    additionalInformation: list[MultilingualStringInput] | UnsetValueType = (
        ListValidator(DataclassValidator(MultilingualStringInput)),
        Default(UnsetValue),
    )
    layer: int = IntegerValidator(min_value=0)
    type: HierarchyElementTypeEnumGInput = DataclassValidator(HierarchyElementTypeEnumGInput)
    parentId: FacilityObjectVersionedReferenceGInput | UnsetValueType = (
        DataclassValidator(FacilityObjectVersionedReferenceGInput),
        Default(UnsetValue),
    )
    childId: list[FacilityObjectVersionedReferenceGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(FacilityObjectVersionedReferenceGInput)),
        Default(UnsetValue),
    )
    operatorDefinedReference: OperatorDefinedPlaceVersionedReferenceGInput | UnsetValueType = (
        DataclassValidator(OperatorDefinedPlaceVersionedReferenceGInput),
        Default(UnsetValue),
    )
    layout: LayoutEnumGInput | UnsetValueType = DataclassValidator(LayoutEnumGInput), Default(UnsetValue)
    availableFloors: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    informationWebsite: list[UrlLinkInput] | UnsetValueType = (
        ListValidator(DataclassValidator(UrlLinkInput)),
        Default(UnsetValue),
    )
    photoUrl: list[UrlLinkInput] | UnsetValueType = ListValidator(DataclassValidator(UrlLinkInput)), Default(UnsetValue)
    photo: list[ImageInput] | UnsetValueType = ListValidator(DataclassValidator(ImageInput)), Default(UnsetValue)
    operatingHours: OperatingHoursGInput | UnsetValueType = (
        DataclassValidator(OperatingHoursGInput),
        Default(UnsetValue),
    )
    locationReference: LocationReferenceGInput | UnsetValueType = (
        DataclassValidator(LocationReferenceGInput),
        Default(UnsetValue),
    )
    owner: OrganisationGInput | UnsetValueType = DataclassValidator(OrganisationGInput), Default(UnsetValue)
    operator: OrganisationGInput | UnsetValueType = DataclassValidator(OrganisationGInput), Default(UnsetValue)
    associatedFacility: list[AssociatedFacilityGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(AssociatedFacilityGInput)),
        Default(UnsetValue),
    )
    rates: RatesGInput | UnsetValueType = DataclassValidator(RatesGInput), Default(UnsetValue)
    applicableForVehicles: list[VehicleCharacteristicsInput] | UnsetValueType = (
        ListValidator(DataclassValidator(VehicleCharacteristicsInput)),
        Default(UnsetValue),
    )
    dimension: DimensionInput | UnsetValueType = DataclassValidator(DimensionInput), Default(UnsetValue)
    supplementalFacility: list[SupplementalFacilityGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(SupplementalFacilityGInput)),
        Default(UnsetValue),
    )
    occupancyLevel: OccupancyLevelInput | UnsetValueType = DataclassValidator(OccupancyLevelInput), Default(UnsetValue)
    operatorDefinedPlace: list[OperatorDefinedPlaceInput] | UnsetValueType = (
        ListValidator(DataclassValidator(OperatorDefinedPlaceInput)),
        Default(UnsetValue),
    )
    responsibilityRoleAssignment: list[ResponsibilityRoleAssignmentInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ResponsibilityRoleAssignmentInput)),
        Default(UnsetValue),
    )
    supply: SupplyInput | UnsetValueType = DataclassValidator(SupplyInput), Default(UnsetValue)
    commonComponents: CommonComponentsInput | UnsetValueType = (
        DataclassValidator(CommonComponentsInput),
        Default(UnsetValue),
    )
    facFacilityObjectExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    facFacilityExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    prkHierarchyElementGeneralExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    prkPlaceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
