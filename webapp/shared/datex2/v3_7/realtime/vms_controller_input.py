"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator, ListValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput

from .vms_controller_vms_index_vms_g_input import vmsControllerVmsIndexVmsGInput


@validataclass
class VmsControllerInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    numberOfVms: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    externalIdentifier: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    ipAddress: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    electronicAddress: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    vms: list[vmsControllerVmsIndexVmsGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(vmsControllerVmsIndexVmsGInput)),
        Default(UnsetValue),
    )
    vmsVmsControllerExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
