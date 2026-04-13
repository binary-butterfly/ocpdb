"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .organisation_type_enum import OrganisationTypeEnum


@dataclass(kw_only=True)
class OrganisationTypeEnumGOutput:
    value: OrganisationTypeEnum
    extendedValueG: str | None = None
