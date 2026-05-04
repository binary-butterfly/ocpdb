"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .device_fault_input import DeviceFaultInput
from .fault_input import FaultInput
from .physical_quantity_fault_input import PhysicalQuantityFaultInput
from .vms_controller_fault_input import VmsControllerFaultInput
from .vms_fault_input import VmsFaultInput


@validataclass
class FaultGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    comFault: FaultInput | UnsetValueType = DataclassValidator(FaultInput), Default(UnsetValue)
    fstDeviceFault: DeviceFaultInput | UnsetValueType = DataclassValidator(DeviceFaultInput), Default(UnsetValue)
    roaPhysicalQuantityFault: PhysicalQuantityFaultInput | UnsetValueType = (
        DataclassValidator(PhysicalQuantityFaultInput),
        Default(UnsetValue),
    )
    vmsVmsFault: VmsFaultInput | UnsetValueType = DataclassValidator(VmsFaultInput), Default(UnsetValue)
    vmsVmsControllerFault: VmsControllerFaultInput | UnsetValueType = (
        DataclassValidator(VmsControllerFaultInput),
        Default(UnsetValue),
    )
