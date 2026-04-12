"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .extension_type_g_output import ExtensionTypeGOutput
from .means_of_payment_enum_g_output import MeansOfPaymentEnumGOutput
from .multilingual_string_output import MultilingualStringOutput
from .payment_brands_enum_g_output import PaymentBrandsEnumGOutput
from .payment_mode_enum_g_output import PaymentModeEnumGOutput


@dataclass(kw_only=True)
class PaymentOutput:
    paymentMode: list[PaymentModeEnumGOutput] | None = None
    paymentMeans: list[MeansOfPaymentEnumGOutput] | None = None
    otherPaymentMeans: list[MultilingualStringOutput] | None = None
    brandsAccepted: list[PaymentBrandsEnumGOutput] | None = None
    otherBrandsAccepted: list[str] | None = None
    afacPaymentExtensionG: ExtensionTypeGOutput | None = None
