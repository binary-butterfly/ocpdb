"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator, IntegerValidator

from webapp.shared.datex2.v3_7.shared.delays_input import DelaysInput

from .impact_extension_type_g_input import ImpactExtensionTypeGInput


@validataclass
class ImpactInput(ValidataclassMixin):
    capacityRemaining: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    numberOfLanesRestricted: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    numberOfOperationalLanes: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    residualLaneWidth: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    residualRoadWidth: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    delays: DelaysInput | UnsetValueType = DataclassValidator(DelaysInput), Default(UnsetValue)
    sitImpactExtensionG: ImpactExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ImpactExtensionTypeGInput),
        Default(UnsetValue),
    )
