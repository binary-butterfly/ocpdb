"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .cause_type_enum_g_input import CauseTypeEnumGInput
from .detailed_cause_type_input import DetailedCauseTypeInput
from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .situation_record_reference_input import SituationRecordReferenceInput


@validataclass
class CauseInput(ValidataclassMixin):
    causeDescription: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    causeType: CauseTypeEnumGInput | UnsetValueType = DataclassValidator(CauseTypeEnumGInput), Default(UnsetValue)
    detailedCauseType: DetailedCauseTypeInput | UnsetValueType = (
        DataclassValidator(DetailedCauseTypeInput),
        Default(UnsetValue),
    )
    managedCause: SituationRecordReferenceInput | UnsetValueType = (
        DataclassValidator(SituationRecordReferenceInput),
        Default(UnsetValue),
    )
    sitCauseExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
