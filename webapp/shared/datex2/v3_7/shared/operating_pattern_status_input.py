"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .operation_status_enum_g_input import OperationStatusEnumGInput
from .public_transport_schedule_input import PublicTransportScheduleInput


@validataclass
class OperatingPatternStatusInput(ValidataclassMixin):
    operatingPatternIndex: int = IntegerValidator()
    operationStatus: OperationStatusEnumGInput = DataclassValidator(OperationStatusEnumGInput)
    ptScheduleUpdate: list[PublicTransportScheduleInput] | UnsetValueType = (
        ListValidator(DataclassValidator(PublicTransportScheduleInput)),
        Default(UnsetValue),
    )
    prkOperatingPatternStatusExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
