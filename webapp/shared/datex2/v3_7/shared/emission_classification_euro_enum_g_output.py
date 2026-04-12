"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .emission_classification_euro_enum import EmissionClassificationEuroEnum
from .emission_classification_euro_enum_extension_type_g import EmissionClassificationEuroEnumExtensionTypeG


@dataclass(kw_only=True)
class EmissionClassificationEuroEnumGOutput:
    value: EmissionClassificationEuroEnum
    extendedValueG: EmissionClassificationEuroEnumExtensionTypeG | None = None
