"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, DateTimeValidator

from .extension_type_g_input import ExtensionTypeGInput
from .measure_definition_versioned_reference_g_input import MeasureDefinitionVersionedReferenceGInput


@validataclass
class MeasureByReferenceInput(ValidataclassMixin):
    versionTime: datetime = DateTimeValidator()
    measureReference: MeasureDefinitionVersionedReferenceGInput = DataclassValidator(
        MeasureDefinitionVersionedReferenceGInput
    )
    tmpMeasureExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    tmpMeasureByReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
