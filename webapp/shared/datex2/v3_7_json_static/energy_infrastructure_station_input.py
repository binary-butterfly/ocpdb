"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from .authentication_and_identification_enum_g_input import AuthenticationAndIdentificationEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .location_reference_g_input import LocationReferenceGInput
from .multilingual_string_input import MultilingualStringInput
from .operating_hours_g_input import OperatingHoursGInput
from .organisation_g_input import OrganisationGInput
from .rates_g_input import RatesGInput
from .refill_point_g_input import RefillPointGInput
from .supplemental_facility_g_input import SupplementalFacilityGInput


@validataclass
class EnergyInfrastructureStationInput(ValidataclassMixin):
    """
    A collection of associated refill points (which can be of different type). An example would be a fuel dispenser that serves different types of fuel. Often the vehicle space of the station is shared between the different refill points.
    """

    idG: str = StringValidator()
    versionG: str = StringValidator()
    name: MultilingualStringInput | UnsetValueType = DataclassValidator(MultilingualStringInput), Default(UnsetValue)
    externalIdentifier: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    lastUpdated: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    authenticationAndIdentificationMethods: list[AuthenticationAndIdentificationEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(AuthenticationAndIdentificationEnumGInput)),
        Default(UnsetValue),
    )
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
    rates: RatesGInput | UnsetValueType = DataclassValidator(RatesGInput), Default(UnsetValue)
    supplementalFacility: list[SupplementalFacilityGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(SupplementalFacilityGInput)),
        Default(UnsetValue),
    )
    energyProvider: OrganisationGInput | UnsetValueType = DataclassValidator(OrganisationGInput), Default(UnsetValue)
    refillPoint: list[RefillPointGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(RefillPointGInput)),
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
    egiEnergyInfrastructureStationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
