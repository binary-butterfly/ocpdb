"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator

from .comparison_operator_enum_g_input import ComparisonOperatorEnumGInput
from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class AgeCharacteristicInput(ValidataclassMixin):
    """
    Characteristics depending on vehicle age.
    """

    comparisonOperator: ComparisonOperatorEnumGInput = DataclassValidator(ComparisonOperatorEnumGInput)
    yearOfFirstRegistration: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    comxAgeCharacteristicExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
