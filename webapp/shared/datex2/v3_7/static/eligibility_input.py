"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, IntegerValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.rate_discount_input import RateDiscountInput
from webapp.shared.datex2.v3_7.shared.right_specification_input import RightSpecificationInput

from .qualification_input import QualificationInput


@validataclass
class EligibilityInput(ValidataclassMixin):
    name: MultilingualStringInput | UnsetValueType = DataclassValidator(MultilingualStringInput), Default(UnsetValue)
    noFeeToUse: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    description: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    priority: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    combinable: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    qualification: list[QualificationInput] | UnsetValueType = (
        ListValidator(DataclassValidator(QualificationInput)),
        Default(UnsetValue),
    )
    rateDiscount: RateDiscountInput | UnsetValueType = DataclassValidator(RateDiscountInput), Default(UnsetValue)
    rightSpecification: list[RightSpecificationInput] | UnsetValueType = (
        ListValidator(DataclassValidator(RightSpecificationInput)),
        Default(UnsetValue),
    )
    afacEligibilityExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
