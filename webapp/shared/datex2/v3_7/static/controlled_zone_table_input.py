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
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput

from .controlled_zone_input import ControlledZoneInput


@validataclass
class ControlledZoneTableInput(ValidataclassMixin):
    controlledZoneTableName: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    tableVersionTime: datetime = DateTimeValidator()
    informationManager: InternationalIdentifierInput | UnsetValueType = (
        DataclassValidator(InternationalIdentifierInput),
        Default(UnsetValue),
    )
    controlledZone: list[ControlledZoneInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ControlledZoneInput)),
        Default(UnsetValue),
    )
    uvarZone: list[ControlledZoneInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ControlledZoneInput)),
        Default(UnsetValue),
    )
    czControlledZoneTableExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
