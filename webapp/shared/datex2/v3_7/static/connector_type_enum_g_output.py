"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .connector_type_enum import ConnectorTypeEnum


@dataclass(kw_only=True)
class ConnectorTypeEnumGOutput:
    value: ConnectorTypeEnum
    extendedValueG: str | None = None
