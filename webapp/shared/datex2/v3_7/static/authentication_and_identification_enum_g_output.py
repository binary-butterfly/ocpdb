"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .authentication_and_identification_enum import AuthenticationAndIdentificationEnum


@dataclass(kw_only=True)
class AuthenticationAndIdentificationEnumGOutput:
    value: AuthenticationAndIdentificationEnum
    extendedValueG: str | None = None
