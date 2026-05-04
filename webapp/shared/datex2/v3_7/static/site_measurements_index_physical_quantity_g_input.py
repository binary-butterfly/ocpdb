"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import ValidataclassMixin, validataclass
from validataclass.validators import DataclassValidator, IntegerValidator

from .physical_quantity_g_input import PhysicalQuantityGInput


@validataclass
class siteMeasurementsIndexPhysicalQuantityGInput(ValidataclassMixin):
    physicalQuantity: PhysicalQuantityGInput = DataclassValidator(PhysicalQuantityGInput)
    index: int = IntegerValidator()
