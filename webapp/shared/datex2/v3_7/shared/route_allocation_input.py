"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, FloatValidator, ListValidator

from .compliance_option_enum_g_input import ComplianceOptionEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .rerouting_advice_type_enum_g_input import ReroutingAdviceTypeEnumGInput


@validataclass
class RouteAllocationInput(ValidataclassMixin):
    routeProportion: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    reroutingAdvice: list[ReroutingAdviceTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ReroutingAdviceTypeEnumGInput)),
        Default(UnsetValue),
    )
    complianceOptionOverride: ComplianceOptionEnumGInput | UnsetValueType = (
        DataclassValidator(ComplianceOptionEnumGInput),
        Default(UnsetValue),
    )
    routeEffectivlyClosedForAllocation: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    rerRouteAllocationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
