"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .device_fault_output import DeviceFaultOutput
from .fault_output import FaultOutput
from .physical_quantity_fault_output import PhysicalQuantityFaultOutput
from .vms_controller_fault_output import VmsControllerFaultOutput
from .vms_fault_output import VmsFaultOutput


@dataclass(kw_only=True)
class FaultGOutput:
    """
    Only one of the properties shall be used in an instance.
    """

    comFault: FaultOutput | None = None
    fstDeviceFault: DeviceFaultOutput | None = None
    roaPhysicalQuantityFault: PhysicalQuantityFaultOutput | None = None
    vmsVmsFault: VmsFaultOutput | None = None
    vmsVmsControllerFault: VmsControllerFaultOutput | None = None
