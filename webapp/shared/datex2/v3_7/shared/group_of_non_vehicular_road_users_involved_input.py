"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator

from .extension_type_g_input import ExtensionTypeGInput
from .injury_status_type_enum_g_input import InjuryStatusTypeEnumGInput
from .non_vehicular_road_users_input import NonVehicularRoadUsersInput


@validataclass
class GroupOfNonVehicularRoadUsersInvolvedInput(ValidataclassMixin):
    numberOfNonVehicularRoadUsers: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    injuryStatusType: InjuryStatusTypeEnumGInput | UnsetValueType = (
        DataclassValidator(InjuryStatusTypeEnumGInput),
        Default(UnsetValue),
    )
    nonVehicularRoadUsers: NonVehicularRoadUsersInput | UnsetValueType = (
        DataclassValidator(NonVehicularRoadUsersInput),
        Default(UnsetValue),
    )
    ubxGroupOfNonVehicularRoadUsersInvolvedExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
