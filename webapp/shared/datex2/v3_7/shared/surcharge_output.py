"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .extension_type_g_output import ExtensionTypeGOutput
from .multilingual_string_output import MultilingualStringOutput
from .refund_type_enum_g_output import RefundTypeEnumGOutput
from .surcharge_type_enum_g_output import SurchargeTypeEnumGOutput


@dataclass(kw_only=True)
class SurchargeOutput:
    surchargeType: SurchargeTypeEnumGOutput
    value: float | None = None
    rate: float | None = None
    trigger: MultilingualStringOutput | None = None
    refund: RefundTypeEnumGOutput | None = None
    labelForDisplay: MultilingualStringOutput | None = None
    afacSurchargeExtensionG: ExtensionTypeGOutput | None = None
