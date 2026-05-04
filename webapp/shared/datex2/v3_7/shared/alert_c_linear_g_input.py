"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .alert_c_linear_by_code_input import AlertCLinearByCodeInput
from .alert_c_method2_linear_input import AlertCMethod2LinearInput
from .alert_c_method4_linear_input import AlertCMethod4LinearInput


@validataclass
class AlertCLinearGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    locAlertCLinearByCode: AlertCLinearByCodeInput | UnsetValueType = (
        DataclassValidator(AlertCLinearByCodeInput),
        Default(UnsetValue),
    )
    locAlertCMethod4Linear: AlertCMethod4LinearInput | UnsetValueType = (
        DataclassValidator(AlertCMethod4LinearInput),
        Default(UnsetValue),
    )
    locAlertCMethod2Linear: AlertCMethod2LinearInput | UnsetValueType = (
        DataclassValidator(AlertCMethod2LinearInput),
        Default(UnsetValue),
    )
