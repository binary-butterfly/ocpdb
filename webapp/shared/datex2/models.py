"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2026 binary butterfly GmbH

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from datetime import datetime
from enum import Enum

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.validators import (
    AnythingValidator,
    DataclassValidator,
    DateTimeValidator,
    EnumValidator,
    ListValidator,
    Noneable,
    StringValidator,
)

from webapp.common.validation import MultiValidataclassValidator
from webapp.shared.datex2.v3_5_json_realtime.models.payload_publication_g_input import (
    PayloadPublicationGInput as PayloadPublicationGV35RealtimeInput,
)
from webapp.shared.datex2.v3_5_json_static.models.payload_publication_g_input import (
    PayloadPublicationGInput as PayloadPublicationGV35StaticInput,
)
from webapp.shared.datex2.v3_7.realtime.payload_publication_g_input import (
    PayloadPublicationGInput as PayloadPublicationGV37RealtimeInput,
)
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput as ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.international_identifier_input import InternationalIdentifierInput
from webapp.shared.datex2.v3_7.static.payload_publication_g_input import (
    PayloadPublicationGInput as PayloadPublicationGV37StaticInput,
)


class ProtocolTypeEnum(Enum):
    DELTA_PULL = 'deltaPull'
    DELTA_PUSH = 'deltaPush'
    OTHER = 'other'
    SIMPLE_CIS = 'simpleCIS'
    SIMPLE_PUSH = 'simplePush'
    SNAPSHOT_PULL = 'snapshotPull'
    SNAPSHOT_PUSH = 'snapshotPush'
    STATEFUL_CIS = 'statefulCIS'
    STATEFUL_PUSH = 'statefulPush'
    EXTENDED_G = 'extendedG'


class ExchangeStatusEnum(Enum):
    CLOSING_SESSION = 'closingSession'
    OFFLINE = 'offline'
    ONLINE = 'online'
    OPENING_SESSION = 'openingSession'
    RESUMING = 'resuming'
    UNDEFINED = 'undefined'
    EXTENDED_G = 'extendedG'


@validataclass
class AgentInput(ValidataclassMixin):
    address: str | None = Noneable(StringValidator(max_length=1024)), Default(None)
    name: str | None = Noneable(StringValidator(max_length=1024)), Default(None)
    referenceID: str | None = Noneable(StringValidator(max_length=1024)), Default(None)
    serviceURL: str | None = Noneable(StringValidator(max_length=1024)), Default(None)
    internationalIdentifier: InternationalIdentifierInput | None = (
        Noneable(DataclassValidator(InternationalIdentifierInput)),
        Default(None),
    )
    exAgentExtensionG: ExtensionTypeGInput | None = (
        Noneable(DataclassValidator(ExtensionTypeGInput)),
        Default(None),
    )


@validataclass
class ProtocolTypeEnumGInput(ValidataclassMixin):
    value: ProtocolTypeEnum = EnumValidator(ProtocolTypeEnum)
    extendedValueG: str | None = Noneable(StringValidator(max_length=1024)), Default(None)


@validataclass
class ExchangeContextInput(ValidataclassMixin):
    codedExchangeProtocol: ProtocolTypeEnumGInput = DataclassValidator(ProtocolTypeEnumGInput)
    exchangeSpecificationVersion: str = StringValidator(max_length=1024)
    supplierOrCisRequester: AgentInput = DataclassValidator(AgentInput)


@validataclass
class ExchangeStatusEnumGInput(ValidataclassMixin):
    value: ExchangeStatusEnum = EnumValidator(ExchangeStatusEnum)
    extendedValueG: str | None = Noneable(StringValidator(max_length=1024)), Default(None)


@validataclass
class DynamicInformationInput(ValidataclassMixin):
    exchangeStatus: ExchangeStatusEnumGInput = DataclassValidator(ExchangeStatusEnumGInput)
    messageGenerationTimestamp: datetime = DateTimeValidator()
    exDynamicInformationExtensionG: ExtensionTypeGInput | None = (
        Noneable(AnythingValidator(allowed_types=[ExtensionTypeGInput])),
        Default(None),
    )


@validataclass
class ExchangeInformationInput(ValidataclassMixin):
    exchangeContext: ExchangeContextInput = DataclassValidator(ExchangeContextInput)
    dynamicInformation: DynamicInformationInput = DataclassValidator(DynamicInformationInput)
    exExchangeInformationExtensionG: ExtensionTypeGInput | None = (
        Noneable(DataclassValidator(ExtensionTypeGInput)),
        Default(None),
    )


@validataclass
class MessageContainerInput(ValidataclassMixin):
    payload: (
        list[
            PayloadPublicationGV35StaticInput
            | PayloadPublicationGV35RealtimeInput
            | PayloadPublicationGV37StaticInput
            | PayloadPublicationGV37RealtimeInput
        ]
        | None
    ) = (
        Noneable(
            ListValidator(
                MultiValidataclassValidator(
                    PayloadPublicationGV35StaticInput,
                    PayloadPublicationGV35RealtimeInput,
                ),
            )
        ),
        Default(None),
    )
    exchangeInformation: ExchangeInformationInput = DataclassValidator(ExchangeInformationInput)
    conMessageContainerExtensionG: ExtensionTypeGInput | None = (
        Noneable(DataclassValidator(ExtensionTypeGInput)),
        Default(None),
    )


@validataclass
class MessageContainerWrapperInput(ValidataclassMixin):
    messageContainer: MessageContainerInput | None = (
        Noneable(DataclassValidator(MessageContainerInput)),
        Default(None),
    )
    exchangeInformation: ExchangeInformationInput | None = (
        Noneable(DataclassValidator(ExchangeInformationInput)),
        Default(None),
    )
