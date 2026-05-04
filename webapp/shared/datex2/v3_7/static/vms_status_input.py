"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    BooleanValidator,
    DataclassValidator,
    DateTimeValidator,
    FloatValidator,
    ListValidator,
)

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.vms_configuration_input import VmsConfigurationInput
from webapp.shared.datex2.v3_7.shared.vms_fault_input import VmsFaultInput
from webapp.shared.datex2.v3_7.shared.working_status_enum_g_input import WorkingStatusEnumGInput

from .location_g_input import LocationGInput
from .managed_logical_location_input import ManagedLogicalLocationInput
from .vms_status_message_index_vms_message_g_input import vmsStatusMessageIndexVmsMessageGInput


@validataclass
class VmsStatusInput(ValidataclassMixin):
    flashingLightsOn: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    remainingPowerCapacity: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    statusUpdateTime: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    sequencingInterval: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    workingStatus: WorkingStatusEnumGInput | UnsetValueType = (
        DataclassValidator(WorkingStatusEnumGInput),
        Default(UnsetValue),
    )
    vmsDynamicConfiguration: VmsConfigurationInput | UnsetValueType = (
        DataclassValidator(VmsConfigurationInput),
        Default(UnsetValue),
    )
    vmsMessage: list[vmsStatusMessageIndexVmsMessageGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(vmsStatusMessageIndexVmsMessageGInput)),
        Default(UnsetValue),
    )
    vmsLocationOverride: LocationGInput | UnsetValueType = DataclassValidator(LocationGInput), Default(UnsetValue)
    managedLogicalLocationOverride: ManagedLogicalLocationInput | UnsetValueType = (
        DataclassValidator(ManagedLogicalLocationInput),
        Default(UnsetValue),
    )
    vmsFault: list[VmsFaultInput] | UnsetValueType = (
        ListValidator(DataclassValidator(VmsFaultInput)),
        Default(UnsetValue),
    )
    vmsVmsStatusExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
