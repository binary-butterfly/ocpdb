"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, DateTimeValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.international_identifier_input import InternationalIdentifierInput
from webapp.shared.datex2.v3_7.shared.vms_controller_fault_input import VmsControllerFaultInput
from webapp.shared.datex2.v3_7.shared.vms_controller_table_versioned_reference_g_input import (
    VmsControllerTableVersionedReferenceGInput,
)
from webapp.shared.datex2.v3_7.shared.vms_controller_versioned_reference_g_input import (
    VmsControllerVersionedReferenceGInput,
)

from .vms_controller_status_vms_index_vms_status_g_input import vmsControllerStatusVmsIndexVmsStatusGInput


@validataclass
class VmsControllerStatusInput(ValidataclassMixin):
    vmsControllerTableReference: VmsControllerTableVersionedReferenceGInput = DataclassValidator(
        VmsControllerTableVersionedReferenceGInput
    )
    vmsControllerReference: VmsControllerVersionedReferenceGInput = DataclassValidator(
        VmsControllerVersionedReferenceGInput
    )
    statusUpdateTime: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    informationManagerOverride: InternationalIdentifierInput | UnsetValueType = (
        DataclassValidator(InternationalIdentifierInput),
        Default(UnsetValue),
    )
    vmsStatus: list[vmsControllerStatusVmsIndexVmsStatusGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(vmsControllerStatusVmsIndexVmsStatusGInput)),
        Default(UnsetValue),
    )
    vmsControllerFault: list[VmsControllerFaultInput] | UnsetValueType = (
        ListValidator(DataclassValidator(VmsControllerFaultInput)),
        Default(UnsetValue),
    )
    vmsVmsControllerStatusExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
