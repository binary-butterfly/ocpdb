"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator

from .driver_characteristics_type_enum_g_input import DriverCharacteristicsTypeEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .legal_basis_input import LegalBasisInput
from .licence_characteristics_enum_g_input import LicenceCharacteristicsEnumGInput
from .non_negative_integer_comparison_input import NonNegativeIntegerComparisonInput
from .time_drivers_licence_held_input import TimeDriversLicenceHeldInput


@validataclass
class DriverConditionInput(ValidataclassMixin):
    negate: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    active: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    driverCharacteristicsType: DriverCharacteristicsTypeEnumGInput | UnsetValueType = (
        DataclassValidator(DriverCharacteristicsTypeEnumGInput),
        Default(UnsetValue),
    )
    licenceCharacteristics: LicenceCharacteristicsEnumGInput | UnsetValueType = (
        DataclassValidator(LicenceCharacteristicsEnumGInput),
        Default(UnsetValue),
    )
    legalBasis: LegalBasisInput | UnsetValueType = DataclassValidator(LegalBasisInput), Default(UnsetValue)
    ageOfDriver: NonNegativeIntegerComparisonInput | UnsetValueType = (
        DataclassValidator(NonNegativeIntegerComparisonInput),
        Default(UnsetValue),
    )
    timeDriversLicenceHeld: TimeDriversLicenceHeldInput | UnsetValueType = (
        DataclassValidator(TimeDriversLicenceHeldInput),
        Default(UnsetValue),
    )
    troConditionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    troDriverConditionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
