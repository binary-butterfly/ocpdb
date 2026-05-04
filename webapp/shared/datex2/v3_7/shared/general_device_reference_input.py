"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, StringValidator

from .device_versioned_reference_g_input import DeviceVersionedReferenceGInput
from .extension_type_g_input import ExtensionTypeGInput
from .international_identifier_input import InternationalIdentifierInput


@validataclass
class GeneralDeviceReferenceInput(ValidataclassMixin):
    externalPublicationIdentifier: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    deviceReference: DeviceVersionedReferenceGInput = DataclassValidator(DeviceVersionedReferenceGInput)
    externalPublisher: InternationalIdentifierInput | UnsetValueType = (
        DataclassValidator(InternationalIdentifierInput),
        Default(UnsetValue),
    )
    comGlobalReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    fstDeviceReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    fstGeneralDeviceReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
