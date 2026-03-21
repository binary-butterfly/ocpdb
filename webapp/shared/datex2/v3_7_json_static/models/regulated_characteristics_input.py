"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .eu_special_purpose_vehicle_enum_g_input import EuSpecialPurposeVehicleEnumGInput
from .eu_vehicle_category_enum_g_input import EuVehicleCategoryEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput


@validataclass
class RegulatedCharacteristicsInput(ValidataclassMixin):
    """
    Characteristics as defined in EU and or national regulations.
    """

    euVehicleCategory: list[EuVehicleCategoryEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(EuVehicleCategoryEnumGInput)),
        Default(UnsetValue),
    )
    euSpecialPurposeVehicle: EuSpecialPurposeVehicleEnumGInput | UnsetValueType = (
        DataclassValidator(EuSpecialPurposeVehicleEnumGInput),
        Default(UnsetValue),
    )
    nationalSpecialPurposeVehicle: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    comxRegulatedCharacteristicsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
