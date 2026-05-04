"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class PhysicalDeviceDetailsInput(ValidataclassMixin):
    barcode: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    installationDate: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    manufactureDate: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    manufacturer: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    model: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    name: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    serialNumber: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    stockCode: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    fstPhysicalDeviceDetailsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
