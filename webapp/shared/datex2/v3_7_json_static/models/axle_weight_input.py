"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator, IntegerValidator

from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class AxleWeightInput(ValidataclassMixin):
    """
    The weight details of a specific axle on the vehicle.
    """

    axlePositionIdentifier: int = IntegerValidator(min_value=0)
    axleWeight: float | UnsetValueType = FloatValidator(), Default(UnsetValue)
    maximumPermittedAxleWeight: float | UnsetValueType = FloatValidator(), Default(UnsetValue)
    comAxleWeightExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
