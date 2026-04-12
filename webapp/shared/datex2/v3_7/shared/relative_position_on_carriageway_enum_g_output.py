"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .relative_position_on_carriageway_enum import RelativePositionOnCarriagewayEnum


@dataclass(kw_only=True)
class RelativePositionOnCarriagewayEnumGOutput:
    value: RelativePositionOnCarriagewayEnum
    extendedValueG: str | None = None
