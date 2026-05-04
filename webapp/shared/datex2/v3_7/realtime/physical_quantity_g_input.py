"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .single_physical_quantity_input import SinglePhysicalQuantityInput
from .time_profiled_physical_quantity_input import TimeProfiledPhysicalQuantityInput


@validataclass
class PhysicalQuantityGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    roaTimeProfiledPhysicalQuantity: TimeProfiledPhysicalQuantityInput | UnsetValueType = (
        DataclassValidator(TimeProfiledPhysicalQuantityInput),
        Default(UnsetValue),
    )
    roaSinglePhysicalQuantity: SinglePhysicalQuantityInput | UnsetValueType = (
        DataclassValidator(SinglePhysicalQuantityInput),
        Default(UnsetValue),
    )
