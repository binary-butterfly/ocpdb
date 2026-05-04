"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .group_of_non_vehicular_road_users_involved_input import GroupOfNonVehicularRoadUsersInvolvedInput


@validataclass
class AccidentExtendedUrbanInput(ValidataclassMixin):
    groupOfNonVehicularRoadUsersInvolved: list[GroupOfNonVehicularRoadUsersInvolvedInput] | UnsetValueType = (
        ListValidator(DataclassValidator(GroupOfNonVehicularRoadUsersInvolvedInput)),
        Default(UnsetValue),
    )
