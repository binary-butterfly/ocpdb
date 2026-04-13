"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .dangerous_goods_regulations_enum_g_output import DangerousGoodsRegulationsEnumGOutput
from .extension_type_g_output import ExtensionTypeGOutput
from .multilingual_string_output import MultilingualStringOutput


@dataclass(kw_only=True)
class DangerousGoodsExtendedOutput:
    chemicalName: MultilingualStringOutput
    dangerousGoodsFlashPoint: float | None = None
    dangerousGoodsRegulations: DangerousGoodsRegulationsEnumGOutput | None = None
    hazardCodeIdentification: str | None = None
    hazardCodeVersionNumber: int | None = None
    hazardSubstanceItemPageNumber: str | None = None
    tremCardNumber: str | None = None
    undgNumber: str | None = None
    volumeOfDangerousGoods: float | None = None
    weightOfDangerousGoods: float | None = None
    adrClassValue: list[str] | None = None
    comHazardousMaterialsExtensionG: ExtensionTypeGOutput | None = None
    comxDangerousGoodsExtendedExtensionG: ExtensionTypeGOutput | None = None
