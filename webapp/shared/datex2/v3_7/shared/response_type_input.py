"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .response_effect_type_enum_g_input import ResponseEffectTypeEnumGInput
from .response_stage_enum_g_input import ResponseStageEnumGInput


@validataclass
class ResponseTypeInput(ValidataclassMixin):
    effect: ResponseEffectTypeEnumGInput = DataclassValidator(ResponseEffectTypeEnumGInput)
    stage: ResponseStageEnumGInput | UnsetValueType = DataclassValidator(ResponseStageEnumGInput), Default(UnsetValue)
    tmpResponseTypeExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
