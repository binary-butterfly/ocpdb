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

from webapp.shared.datex2.v3_7.shared.access_and_egress_input import AccessAndEgressInput
from webapp.shared.datex2.v3_7.shared.access_equipment_enum_g_input import AccessEquipmentEnumGInput
from webapp.shared.datex2.v3_7.shared.access_road_input import AccessRoadInput
from webapp.shared.datex2.v3_7.shared.access_type_enum_g_input import AccessTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.accessibility_enum_g_input import AccessibilityEnumGInput
from webapp.shared.datex2.v3_7.shared.associated_facility_g_input import AssociatedFacilityGInput
from webapp.shared.datex2.v3_7.shared.dimension_input import DimensionInput
from webapp.shared.datex2.v3_7.shared.direction_compass_enum_g_input import DirectionCompassEnumGInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.facility_object_versioned_reference_g_input import (
    FacilityObjectVersionedReferenceGInput,
)
from webapp.shared.datex2.v3_7.shared.hierarchy_element_type_enum_g_input import HierarchyElementTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.image_input import ImageInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.occupancy_level_input import OccupancyLevelInput
from webapp.shared.datex2.v3_7.shared.operating_hours_g_input import OperatingHoursGInput
from webapp.shared.datex2.v3_7.shared.operator_defined_place_versioned_reference_g_input import (
    OperatorDefinedPlaceVersionedReferenceGInput,
)
from webapp.shared.datex2.v3_7.shared.pedestrian_access_style_enum_g_input import PedestrianAccessStyleEnumGInput
from webapp.shared.datex2.v3_7.shared.supply_input import SupplyInput
from webapp.shared.datex2.v3_7.shared.url_link_input import UrlLinkInput

from .additional_characteristics_input import AdditionalCharacteristicsInput
from .location_reference_g_input import LocationReferenceGInput
from .operating_pattern_g_input import OperatingPatternGInput
from .operator_defined_place_input import OperatorDefinedPlaceInput
from .organisation_g_input import OrganisationGInput
from .rates_g_input import RatesGInput
from .responsibility_role_assignment_input import ResponsibilityRoleAssignmentInput
from .supplemental_facility_g_input import SupplementalFacilityGInput
from .vehicle_characteristics_input import VehicleCharacteristicsInput


@validataclass
class PedestrianAccessInput(ValidataclassMixin):
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
    accessType: AccessTypeEnumGInput = DataclassValidator(AccessTypeEnumGInput)
    equipment: list[AccessEquipmentEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(AccessEquipmentEnumGInput)),
        Default(UnsetValue),
    )
    orientation: list[DirectionCompassEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(DirectionCompassEnumGInput)),
        Default(UnsetValue),
    )
    style: PedestrianAccessStyleEnumGInput | UnsetValueType = (
        DataclassValidator(PedestrianAccessStyleEnumGInput),
        Default(UnsetValue),
    )
    numberOfPortals: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
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
    operatingPattern: list[OperatingPatternGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(OperatingPatternGInput)),
        Default(UnsetValue),
    )
    additionalCharacteristics: AdditionalCharacteristicsInput | UnsetValueType = (
        DataclassValidator(AdditionalCharacteristicsInput),
        Default(UnsetValue),
    )
    accessAndEgress: AccessAndEgressInput | UnsetValueType = (
        DataclassValidator(AccessAndEgressInput),
        Default(UnsetValue),
    )
    primaryRoad: list[AccessRoadInput] | UnsetValueType = (
        ListValidator(DataclassValidator(AccessRoadInput)),
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
    prkIdentifiedAreaExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    prkAccessExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    prkPedestrianAccessExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
