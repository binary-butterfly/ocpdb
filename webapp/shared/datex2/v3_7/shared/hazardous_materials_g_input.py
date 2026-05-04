"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .dangerous_goods_extended_input import DangerousGoodsExtendedInput
from .hazardous_materials_input import HazardousMaterialsInput


@validataclass
class HazardousMaterialsGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    comHazardousMaterials: HazardousMaterialsInput | UnsetValueType = (
        DataclassValidator(HazardousMaterialsInput),
        Default(UnsetValue),
    )
    comxDangerousGoodsExtended: DangerousGoodsExtendedInput | UnsetValueType = (
        DataclassValidator(DangerousGoodsExtendedInput),
        Default(UnsetValue),
    )
