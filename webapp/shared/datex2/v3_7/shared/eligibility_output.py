"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .extension_type_g_output import ExtensionTypeGOutput
from .multilingual_string_output import MultilingualStringOutput
from .qualification_output import QualificationOutput
from .rate_discount_output import RateDiscountOutput
from .right_specification_output import RightSpecificationOutput


@dataclass(kw_only=True)
class EligibilityOutput:
    name: MultilingualStringOutput | None = None
    noFeeToUse: bool | None = None
    description: MultilingualStringOutput | None = None
    priority: int | None = None
    combinable: bool | None = None
    qualification: list[QualificationOutput] | None = None
    rateDiscount: RateDiscountOutput | None = None
    rightSpecification: list[RightSpecificationOutput] | None = None
    afacEligibilityExtensionG: ExtensionTypeGOutput | None = None
