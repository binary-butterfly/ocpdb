"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .iso_named_area_output import IsoNamedAreaOutput
from .named_area_output import NamedAreaOutput
from .nuts_named_area_output import NutsNamedAreaOutput


@dataclass(kw_only=True)
class NamedAreaGOutput:
    """
    Only one of the properties shall be used in an instance.
    """

    locNamedArea: NamedAreaOutput | None = None
    locNutsNamedArea: NutsNamedAreaOutput | None = None
    locIsoNamedArea: IsoNamedAreaOutput | None = None
