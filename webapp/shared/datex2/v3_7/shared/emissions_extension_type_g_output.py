"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .emissions_extension_output import EmissionsExtensionOutput


@dataclass(kw_only=True)
class EmissionsExtensionTypeGOutput:
    EmissionsExtension: EmissionsExtensionOutput | None = None
