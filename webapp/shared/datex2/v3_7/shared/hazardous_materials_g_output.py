"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .dangerous_goods_extended_output import DangerousGoodsExtendedOutput
from .hazardous_materials_output import HazardousMaterialsOutput


@dataclass(kw_only=True)
class HazardousMaterialsGOutput:
    """
    Only one of the properties shall be used in an instance.
    """

    comHazardousMaterials: HazardousMaterialsOutput | None = None
    comxDangerousGoodsExtended: DangerousGoodsExtendedOutput | None = None
