"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput

from .impact_input import ImpactInput


@validataclass
class ImpactKindInput(ValidataclassMixin):
    capacityReduced: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    impactDetail: ImpactInput | UnsetValueType = DataclassValidator(ImpactInput), Default(UnsetValue)
    tmpImpactKindExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
