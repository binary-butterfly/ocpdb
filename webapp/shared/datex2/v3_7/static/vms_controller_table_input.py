"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.international_identifier_input import InternationalIdentifierInput

from .vms_controller_input import VmsControllerInput


@validataclass
class VmsControllerTableInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    vmsControllerTableIdentification: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    informationManager: InternationalIdentifierInput | UnsetValueType = (
        DataclassValidator(InternationalIdentifierInput),
        Default(UnsetValue),
    )
    vmsController: list[VmsControllerInput] = ListValidator(DataclassValidator(VmsControllerInput))
    vmsVmsControllerTableExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
