"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .closure_information_output import ClosureInformationOutput
from .extension_type_g_output import ExtensionTypeGOutput


@dataclass(kw_only=True)
class UndefinedOperatingHoursOutput:
    closureInformation: ClosureInformationOutput | None = None
    afacOperatingHoursExtensionG: ExtensionTypeGOutput | None = None
    afacUndefinedOperatingHoursExtensionG: ExtensionTypeGOutput | None = None
