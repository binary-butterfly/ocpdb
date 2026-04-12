"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .eu_bodywork_supplementary_digit import EuBodyworkSupplementaryDigit


@dataclass(kw_only=True)
class EuBodyworkSupplementaryDigitGOutput:
    value: EuBodyworkSupplementaryDigit
    extendedValueG: str | None = None
