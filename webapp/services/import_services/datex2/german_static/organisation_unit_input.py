"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .contact_information_g_input import ContactInformationGInput
from .extension_type_g_input import ExtensionTypeGInput
from .location_reference_g_input import LocationReferenceGInput
from .multilingual_string_input import MultilingualStringInput
from .operating_hours_g_input import OperatingHoursGInput


@validataclass
class OrganisationUnitInput:
    name: MultilingualStringInput | UnsetValueType = DataclassValidator(MultilingualStringInput), Default(UnsetValue)
    function: list[MultilingualStringInput] | UnsetValueType = (
        ListValidator(DataclassValidator(MultilingualStringInput)),
        Default(UnsetValue),
    )
    locationReference: LocationReferenceGInput | UnsetValueType = (
        DataclassValidator(LocationReferenceGInput),
        Default(UnsetValue),
    )
    contactInformation: list[ContactInformationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ContactInformationGInput)),
        Default(UnsetValue),
    )
    operatingHours: OperatingHoursGInput | UnsetValueType = (
        DataclassValidator(OperatingHoursGInput),
        Default(UnsetValue),
    )
    afacOrganisationUnitExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
