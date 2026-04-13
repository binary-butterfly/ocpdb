"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .supplementary_positional_description_extended_output import SupplementaryPositionalDescriptionExtendedOutput


@dataclass(kw_only=True)
class SupplementaryPositionalDescriptionExtensionTypeGOutput:
    SupplementaryPositionalDescriptionExtended: SupplementaryPositionalDescriptionExtendedOutput | None = None
