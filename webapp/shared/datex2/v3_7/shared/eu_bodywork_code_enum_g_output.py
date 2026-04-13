"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .eu_bodywork_code_enum import EuBodyworkCodeEnum


@dataclass(kw_only=True)
class EuBodyworkCodeEnumGOutput:
    value: EuBodyworkCodeEnum
    extendedValueG: str | None = None
