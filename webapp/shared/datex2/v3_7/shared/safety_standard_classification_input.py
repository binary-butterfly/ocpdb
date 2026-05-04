"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .certified_secure_parking_input import CertifiedSecureParkingInput
from .esporg_standard_level_enum_g_input import EsporgStandardLevelEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .parking_safety_enum_g_input import ParkingSafetyEnumGInput
from .parking_security_enum_g_input import ParkingSecurityEnumGInput
from .parking_supervision_enum_g_input import ParkingSupervisionEnumGInput


@validataclass
class SafetyStandardClassificationInput(ValidataclassMixin):
    securityFeature: ParkingSecurityEnumGInput | UnsetValueType = (
        DataclassValidator(ParkingSecurityEnumGInput),
        Default(UnsetValue),
    )
    securityLevel: EsporgStandardLevelEnumGInput | UnsetValueType = (
        DataclassValidator(EsporgStandardLevelEnumGInput),
        Default(UnsetValue),
    )
    additionalSecurity: list[MultilingualStringInput] | UnsetValueType = (
        ListValidator(DataclassValidator(MultilingualStringInput)),
        Default(UnsetValue),
    )
    safety: list[ParkingSafetyEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ParkingSafetyEnumGInput)),
        Default(UnsetValue),
    )
    additionalSafety: list[MultilingualStringInput] | UnsetValueType = (
        ListValidator(DataclassValidator(MultilingualStringInput)),
        Default(UnsetValue),
    )
    supervision: list[ParkingSupervisionEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ParkingSupervisionEnumGInput)),
        Default(UnsetValue),
    )
    securityNationalClassification: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    certifiedSecureParking: list[CertifiedSecureParkingInput] | UnsetValueType = (
        ListValidator(DataclassValidator(CertifiedSecureParkingInput)),
        Default(UnsetValue),
    )
    prkSafetyStandardClassificationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
