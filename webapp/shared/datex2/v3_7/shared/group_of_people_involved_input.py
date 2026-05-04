"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator

from .extension_type_g_input import ExtensionTypeGInput
from .injury_status_type_enum_g_input import InjuryStatusTypeEnumGInput
from .involvement_roles_enum_g_input import InvolvementRolesEnumGInput
from .person_category_enum_g_input import PersonCategoryEnumGInput


@validataclass
class GroupOfPeopleInvolvedInput(ValidataclassMixin):
    numberOfPeople: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    injuryStatusType: InjuryStatusTypeEnumGInput | UnsetValueType = (
        DataclassValidator(InjuryStatusTypeEnumGInput),
        Default(UnsetValue),
    )
    involvementRole: InvolvementRolesEnumGInput | UnsetValueType = (
        DataclassValidator(InvolvementRolesEnumGInput),
        Default(UnsetValue),
    )
    categoryOfPeopleInvolved: PersonCategoryEnumGInput | UnsetValueType = (
        DataclassValidator(PersonCategoryEnumGInput),
        Default(UnsetValue),
    )
    sitGroupOfPeopleInvolvedExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
