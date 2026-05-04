"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator

from .extension_type_g_input import ExtensionTypeGInput
from .subject_type_of_works_enum_g_input import SubjectTypeOfWorksEnumGInput


@validataclass
class SubjectsInput(ValidataclassMixin):
    subjectTypeOfWorks: SubjectTypeOfWorksEnumGInput = DataclassValidator(SubjectTypeOfWorksEnumGInput)
    numberOfSubjects: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    sitSubjectsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
