"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .measure_definition_versioned_reference_g_input import MeasureDefinitionVersionedReferenceGInput
from .predefined_action_input import PredefinedActionInput


@validataclass
class PredefinedMeasureSelectedInput(ValidataclassMixin):
    predefinedMeasureReference: MeasureDefinitionVersionedReferenceGInput = DataclassValidator(
        MeasureDefinitionVersionedReferenceGInput
    )
    predefinedAction: list[PredefinedActionInput] | UnsetValueType = (
        ListValidator(DataclassValidator(PredefinedActionInput)),
        Default(UnsetValue),
    )
    tmpPredefinedMeasureSelectedExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
