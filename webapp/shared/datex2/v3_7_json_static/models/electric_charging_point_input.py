"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator, ListValidator, StringValidator

from .connector_input import ConnectorInput
from .electric_energy_mix_input import ElectricEnergyMixInput
from .extension_type_g_input import ExtensionTypeGInput
from .location_reference_g_input import LocationReferenceGInput
from .multilingual_string_input import MultilingualStringInput
from .operating_hours_g_input import OperatingHoursGInput
from .organisation_g_input import OrganisationGInput
from .rates_g_input import RatesGInput
from .supplemental_facility_g_input import SupplementalFacilityGInput


@validataclass
class ElectricChargingPointInput(ValidataclassMixin):
    """
    Technical infrastructure at a specific location that facilitates electric charging of one vehicle at a time
    """

    idG: str = StringValidator()
    versionG: str = StringValidator()
    name: MultilingualStringInput | UnsetValueType = DataclassValidator(MultilingualStringInput), Default(UnsetValue)
    externalIdentifier: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    lastUpdated: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    availableVoltage: list[int] | UnsetValueType = ListValidator(FloatValidator()), Default(UnsetValue)
    availableChargingPower: list[int] | UnsetValueType = ListValidator(FloatValidator()), Default(UnsetValue)
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
    connector: list[ConnectorInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ConnectorInput)),
        Default(UnsetValue),
    )
    electricEnergyMix: list[ElectricEnergyMixInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ElectricEnergyMixInput)),
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
    egiRefillPointExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    egiElectricChargingPointExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
