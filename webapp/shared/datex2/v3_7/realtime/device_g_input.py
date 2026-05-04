"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .component_input import ComponentInput
from .device_input import DeviceInput


@validataclass
class DeviceGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    fstDevice: DeviceInput | UnsetValueType = DataclassValidator(DeviceInput), Default(UnsetValue)
    fstComponent: ComponentInput | UnsetValueType = DataclassValidator(ComponentInput), Default(UnsetValue)
