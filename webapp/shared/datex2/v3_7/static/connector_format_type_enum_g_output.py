"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .connector_format_type_enum import ConnectorFormatTypeEnum


@dataclass(kw_only=True)
class ConnectorFormatTypeEnumGOutput:
    value: ConnectorFormatTypeEnum
    extendedValueG: str | None = None
