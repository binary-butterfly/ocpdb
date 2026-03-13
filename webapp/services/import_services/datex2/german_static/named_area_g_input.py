"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .iso_named_area_input import IsoNamedAreaInput
from .named_area_input import NamedAreaInput
from .nuts_named_area_input import NutsNamedAreaInput


@validataclass
class NamedAreaGInput:
    locNamedArea: NamedAreaInput | UnsetValueType = DataclassValidator(NamedAreaInput), Default(UnsetValue)
    locNutsNamedArea: NutsNamedAreaInput | UnsetValueType = DataclassValidator(NutsNamedAreaInput), Default(UnsetValue)
    locIsoNamedArea: IsoNamedAreaInput | UnsetValueType = DataclassValidator(IsoNamedAreaInput), Default(UnsetValue)
