"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .type_of_identifier_enum import TypeOfIdentifierEnum
from .type_of_identifier_enum_extension_type_g import TypeOfIdentifierEnumExtensionTypeG


@dataclass(kw_only=True)
class TypeOfIdentifierEnumGOutput:
    value: TypeOfIdentifierEnum
    extendedValueG: TypeOfIdentifierEnumExtensionTypeG | None = None
