"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, IntegerValidator, ListValidator

from .covered_enum_g_input import CoveredEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .session_activation_mode_enum_g_input import SessionActivationModeEnumGInput
from .staff_enum_g_input import StaffEnumGInput
from .structure_grade_enum_g_input import StructureGradeEnumGInput
from .structure_type_enum_g_input import StructureTypeEnumGInput


@validataclass
class CharacteristicsInput(ValidataclassMixin):
    activationMode: list[SessionActivationModeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(SessionActivationModeEnumGInput)),
        Default(UnsetValue),
    )
    structureGrade: StructureGradeEnumGInput | UnsetValueType = (
        DataclassValidator(StructureGradeEnumGInput),
        Default(UnsetValue),
    )
    robotic: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    accessControlled: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    staffed: StaffEnumGInput | UnsetValueType = DataclassValidator(StaffEnumGInput), Default(UnsetValue)
    structureType: StructureTypeEnumGInput = DataclassValidator(StructureTypeEnumGInput)
    coveredType: CoveredEnumGInput | UnsetValueType = DataclassValidator(CoveredEnumGInput), Default(UnsetValue)
    openToPublic: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    spacesNonDedicated: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    spacesTotal: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    accessForPersonsWithDisabilities: list[bool] | UnsetValueType = (
        ListValidator(BooleanValidator()),
        Default(UnsetValue),
    )
    prkCharacteristicsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
