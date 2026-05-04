"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, DateTimeValidator, ListValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.header_information_input import HeaderInformationInput
from webapp.shared.datex2.v3_7.shared.international_identifier_input import InternationalIdentifierInput
from webapp.shared.datex2.v3_7.shared.severity_enum_g_input import SeverityEnumGInput
from webapp.shared.datex2.v3_7.shared.situation_reference_input import SituationReferenceInput

from .situation_record_g_input import SituationRecordGInput


@validataclass
class SituationInput(ValidataclassMixin):
    idG: str = StringValidator()
    overallSeverity: SeverityEnumGInput | UnsetValueType = DataclassValidator(SeverityEnumGInput), Default(UnsetValue)
    situationVersionTime: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    headerInformation: HeaderInformationInput = DataclassValidator(HeaderInformationInput)
    situationRecord: list[SituationRecordGInput] = ListValidator(DataclassValidator(SituationRecordGInput))
    relatedSituation: list[SituationReferenceInput] | UnsetValueType = (
        ListValidator(DataclassValidator(SituationReferenceInput)),
        Default(UnsetValue),
    )
    informationManager: InternationalIdentifierInput | UnsetValueType = (
        DataclassValidator(InternationalIdentifierInput),
        Default(UnsetValue),
    )
    situationSummary: SituationRecordGInput | UnsetValueType = (
        DataclassValidator(SituationRecordGInput),
        Default(UnsetValue),
    )
    sitSituationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
