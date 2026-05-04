"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .impact_extended_urban_input import ImpactExtendedUrbanInput


@validataclass
class ImpactExtensionTypeGInput(ValidataclassMixin):
    ImpactExtendedUrban: ImpactExtendedUrbanInput | UnsetValueType = (
        DataclassValidator(ImpactExtendedUrbanInput),
        Default(UnsetValue),
    )
