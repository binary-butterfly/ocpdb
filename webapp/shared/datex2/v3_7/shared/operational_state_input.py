"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, DateTimeValidator, ListValidator

from .catalogue_information_input import CatalogueInformationInput
from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .operational_device_state_enum_g_input import OperationalDeviceStateEnumGInput


@validataclass
class OperationalStateInput(ValidataclassMixin):
    operationalDeviceState: OperationalDeviceStateEnumGInput = DataclassValidator(OperationalDeviceStateEnumGInput)
    stateDescription: list[MultilingualStringInput] | UnsetValueType = (
        ListValidator(DataclassValidator(MultilingualStringInput)),
        Default(UnsetValue),
    )
    lastStateChange: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    lastStateUpdate: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    operationalStateCatalogueInformation: CatalogueInformationInput | UnsetValueType = (
        DataclassValidator(CatalogueInformationInput),
        Default(UnsetValue),
    )
    fstOperationalStateExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
