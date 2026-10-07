"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .non_vehicular_road_user_type_enum_g_input import NonVehicularRoadUserTypeEnumGInput


@validataclass(reject_unknown_fields=True)
class NonVehicularRoadUsersInput(ValidataclassMixin):
    nonVehicularRoadUser: list[NonVehicularRoadUserTypeEnumGInput] = ListValidator(
        DataclassValidator(NonVehicularRoadUserTypeEnumGInput)
    )
    ubxNonVehicularRoadUsersExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
