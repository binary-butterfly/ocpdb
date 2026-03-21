"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    DataclassValidator,
    FloatValidator,
    IntegerValidator,
    ListValidator,
    StringValidator,
)

from .dangerous_goods_regulations_enum_g_input import DangerousGoodsRegulationsEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput


@validataclass
class DangerousGoodsExtendedInput(ValidataclassMixin):
    """
    Extension of dangerous goods class.
    """

    chemicalName: MultilingualStringInput = DataclassValidator(MultilingualStringInput)
    dangerousGoodsFlashPoint: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    dangerousGoodsRegulations: DangerousGoodsRegulationsEnumGInput | UnsetValueType = (
        DataclassValidator(DangerousGoodsRegulationsEnumGInput),
        Default(UnsetValue),
    )
    hazardCodeIdentification: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    hazardCodeVersionNumber: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    hazardSubstanceItemPageNumber: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    tremCardNumber: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    undgNumber: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    volumeOfDangerousGoods: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    weightOfDangerousGoods: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    adrClassValue: list[str] | UnsetValueType = ListValidator(StringValidator()), Default(UnsetValue)
    comHazardousMaterialsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    comxDangerousGoodsExtendedExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
