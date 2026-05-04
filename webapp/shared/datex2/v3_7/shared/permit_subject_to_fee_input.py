"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class PermitSubjectToFeeInput(ValidataclassMixin):
    amountDue: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    maximumAccessDuration: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    paymentInformation: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    troPermitSubjectToFeeExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
