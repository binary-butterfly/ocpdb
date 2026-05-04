"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator

from .extension_type_g_input import ExtensionTypeGInput
from .referent_input import ReferentInput


@validataclass
class DistanceFromLinearElementReferentInput(ValidataclassMixin):
    distanceAlong: float = FloatValidator(allow_integers=True)
    fromReferent: ReferentInput = DataclassValidator(ReferentInput)
    towardsReferent: ReferentInput | UnsetValueType = DataclassValidator(ReferentInput), Default(UnsetValue)
    locDistanceAlongLinearElementExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locDistanceFromLinearElementReferentExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
