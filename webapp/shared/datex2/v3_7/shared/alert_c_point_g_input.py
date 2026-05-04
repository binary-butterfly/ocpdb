"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .alert_c_method2_point_input import AlertCMethod2PointInput
from .alert_c_method4_point_input import AlertCMethod4PointInput


@validataclass
class AlertCPointGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    locAlertCMethod2Point: AlertCMethod2PointInput | UnsetValueType = (
        DataclassValidator(AlertCMethod2PointInput),
        Default(UnsetValue),
    )
    locAlertCMethod4Point: AlertCMethod4PointInput | UnsetValueType = (
        DataclassValidator(AlertCMethod4PointInput),
        Default(UnsetValue),
    )
