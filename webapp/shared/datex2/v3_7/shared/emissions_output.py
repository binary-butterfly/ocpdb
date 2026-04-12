"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .emission_classification_euro_enum_g_output import EmissionClassificationEuroEnumGOutput
from .emissions_extension_type_g_output import EmissionsExtensionTypeGOutput
from .low_emission_level_enum_g_output import LowEmissionLevelEnumGOutput


@dataclass(kw_only=True)
class EmissionsOutput:
    emissionClassificationEuro: EmissionClassificationEuroEnumGOutput | None = None
    emissionClassificationOther: list[str] | None = None
    emissionLevel: LowEmissionLevelEnumGOutput | None = None
    comEmissionsExtensionG: EmissionsExtensionTypeGOutput | None = None
