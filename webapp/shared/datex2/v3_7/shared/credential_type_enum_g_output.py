"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .credential_type_enum import CredentialTypeEnum


@dataclass(kw_only=True)
class CredentialTypeEnumGOutput:
    value: CredentialTypeEnum
    extendedValueG: str | None = None
