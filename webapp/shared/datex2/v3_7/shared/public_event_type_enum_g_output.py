"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .public_event_type_enum import PublicEventTypeEnum


@dataclass(kw_only=True)
class PublicEventTypeEnumGOutput:
    value: PublicEventTypeEnum
    extendedValueG: str | None = None
