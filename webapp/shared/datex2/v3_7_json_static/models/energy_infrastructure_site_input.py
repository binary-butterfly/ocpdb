"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from .energy_infrastructure_station_input import EnergyInfrastructureStationInput
from .extension_type_g_input import ExtensionTypeGInput
from .location_g_input import LocationGInput
from .location_reference_g_input import LocationReferenceGInput
from .multilingual_string_input import MultilingualStringInput
from .operating_hours_g_input import OperatingHoursGInput
from .organisation_g_input import OrganisationGInput
from .rates_g_input import RatesGInput
from .supplemental_facility_g_input import SupplementalFacilityGInput


@validataclass
class EnergyInfrastructureSiteInput(ValidataclassMixin):
    """
    A site where vehicles can be supplied with energy, including all buildings, stations, parking spaces and other associated services.
    """

    idG: str = StringValidator()
    versionG: str = StringValidator()
    name: MultilingualStringInput | UnsetValueType = DataclassValidator(MultilingualStringInput), Default(UnsetValue)
    externalIdentifier: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    lastUpdated: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    brand: MultilingualStringInput | UnsetValueType = DataclassValidator(MultilingualStringInput), Default(UnsetValue)
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
    entrance: list[LocationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(LocationGInput)),
        Default(UnsetValue),
    )
    energyInfrastructureStation: list[EnergyInfrastructureStationInput] | UnsetValueType = (
        ListValidator(DataclassValidator(EnergyInfrastructureStationInput)),
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
    egiEnergyInfrastructureSiteExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
