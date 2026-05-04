"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, DateTimeValidator, ListValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.international_identifier_input import InternationalIdentifierInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.operating_hours_specification_input import OperatingHoursSpecificationInput


@validataclass
class OperatingHoursTableInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    name: MultilingualStringInput | UnsetValueType = DataclassValidator(MultilingualStringInput), Default(UnsetValue)
    versionTime: datetime = DateTimeValidator()
    informationManager: InternationalIdentifierInput | UnsetValueType = (
        DataclassValidator(InternationalIdentifierInput),
        Default(UnsetValue),
    )
    operatingHoursSpecification: list[OperatingHoursSpecificationInput] = ListValidator(
        DataclassValidator(OperatingHoursSpecificationInput)
    )
    afacOperatingHoursTableExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
