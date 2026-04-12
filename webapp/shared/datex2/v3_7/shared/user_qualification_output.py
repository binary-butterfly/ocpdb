"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .extension_type_g_output import ExtensionTypeGOutput
from .user_type_enum_g_output import UserTypeEnumGOutput


@dataclass(kw_only=True)
class UserQualificationOutput:
    userGroup: UserTypeEnumGOutput
    afacUserQualificationExtensionG: ExtensionTypeGOutput | None = None
