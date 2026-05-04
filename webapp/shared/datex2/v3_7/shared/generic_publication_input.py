"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, DateTimeValidator, RegexValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .international_identifier_input import InternationalIdentifierInput
from .multilingual_string_input import MultilingualStringInput


@validataclass
class GenericPublicationInput(ValidataclassMixin):
    lang: str = RegexValidator(pattern=r'^[a-z]{2}$')
    feedDescription: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    feedType: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    publicationTime: datetime = DateTimeValidator()
    genericPublicationName: str = StringValidator()
    publicationCreator: InternationalIdentifierInput = DataclassValidator(InternationalIdentifierInput)
    comPayloadPublicationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    comGenericPublicationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
