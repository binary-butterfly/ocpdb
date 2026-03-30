"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator, IntegerValidator, StringValidator

from .dangerous_goods_regulations_enum_g_input import DangerousGoodsRegulationsEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput


@validataclass
class HazardousMaterialsInput(ValidataclassMixin):
    """
    Details of hazardous materials.
    """

    chemicalName: MultilingualStringInput = DataclassValidator(MultilingualStringInput)
    dangerousGoodsFlashPoint: float | UnsetValueType = FloatValidator(), Default(UnsetValue)
    dangerousGoodsRegulations: DangerousGoodsRegulationsEnumGInput | UnsetValueType = (
        DataclassValidator(DangerousGoodsRegulationsEnumGInput),
        Default(UnsetValue),
    )
    hazardCodeIdentification: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    hazardCodeVersionNumber: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    hazardSubstanceItemPageNumber: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    tremCardNumber: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    undgNumber: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    volumeOfDangerousGoods: float | UnsetValueType = FloatValidator(), Default(UnsetValue)
    weightOfDangerousGoods: float | UnsetValueType = FloatValidator(), Default(UnsetValue)
    comHazardousMaterialsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
