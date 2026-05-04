"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator

from .displayed_numerical_information_type_enum_g_input import DisplayedNumericalInformationTypeEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .unit_of_measure_enum_g_input import UnitOfMeasureEnumGInput


@validataclass
class DisplayedNumericalInformationInput(ValidataclassMixin):
    numericalInformationType: DisplayedNumericalInformationTypeEnumGInput = DataclassValidator(
        DisplayedNumericalInformationTypeEnumGInput
    )
    numericValue: float = FloatValidator(allow_integers=True)
    unitOfMeasure: UnitOfMeasureEnumGInput = DataclassValidator(UnitOfMeasureEnumGInput)
    vmsDisplayedNumericalInformationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
