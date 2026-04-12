"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .extension_type_g_output import ExtensionTypeGOutput
from .multilingual_string_output import MultilingualStringOutput
from .rate_line_tax_output import RateLineTaxOutput
from .rate_line_type_enum_g_output import RateLineTypeEnumGOutput
from .rate_line_usage_conditions_type_enum_g_output import RateLineUsageConditionsTypeEnumGOutput
from .surcharge_output import SurchargeOutput


@dataclass(kw_only=True)
class RateLineOutput:
    sequence: int
    rateLineType: RateLineTypeEnumGOutput
    description: MultilingualStringOutput | None = None
    durationStart: str | None = None
    durationEnd: str | None = None
    incrementPeriod: str | None = None
    value: float
    minValue: float | None = None
    maxValue: float | None = None
    usageCondition: RateLineUsageConditionsTypeEnumGOutput | None = None
    usageDurationLimitation: str | None = None
    usageCountLimitation: int | None = None
    surcharge: list[SurchargeOutput] | None = None
    rateLineTax: list[RateLineTaxOutput] | None = None
    afacRateLineExtensionG: ExtensionTypeGOutput | None = None
