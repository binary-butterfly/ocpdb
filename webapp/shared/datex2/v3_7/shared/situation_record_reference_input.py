"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .international_identifier_input import InternationalIdentifierInput
from .situation_record_versioned_reference_g_input import SituationRecordVersionedReferenceGInput


@validataclass
class SituationRecordReferenceInput(ValidataclassMixin):
    externalPublicationIdentifier: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    objectReference: SituationRecordVersionedReferenceGInput = DataclassValidator(
        SituationRecordVersionedReferenceGInput
    )
    externalPublisher: InternationalIdentifierInput | UnsetValueType = (
        DataclassValidator(InternationalIdentifierInput),
        Default(UnsetValue),
    )
    comGlobalReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    sitSituationRecordReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
