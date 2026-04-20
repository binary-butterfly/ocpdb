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
    PayloadPublicationGInput as PayloadPublicationGV35RealtimeOutput,
)
from webapp.shared.datex2.v3_5_json_static.models.payload_publication_g_input import (
    PayloadPublicationGInput as PayloadPublicationGV35StaticOutput,
)
from webapp.shared.datex2.v3_7.realtime.payload_publication_g_output import (
    PayloadPublicationGOutput as PayloadPublicationGV37RealtimeOutput,
)
from webapp.shared.datex2.v3_7.shared.extension_type_g_output import ExtensionTypeGOutput
from webapp.shared.datex2.v3_7.shared.international_identifier_output import InternationalIdentifierOutput
from webapp.shared.datex2.v3_7.static.payload_publication_g_output import (
    PayloadPublicationGOutput as PayloadPublicationGV37StaticOutput,
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
class AgentOutput(ValidataclassMixin):
    address: str | None = Noneable(StringValidator(max_length=1024)), Default(None)
    name: str | None = Noneable(StringValidator(max_length=1024)), Default(None)
    referenceID: str | None = Noneable(StringValidator(max_length=1024)), Default(None)
    serviceURL: str | None = Noneable(StringValidator(max_length=1024)), Default(None)
    internationalIdentifier: InternationalIdentifierOutput | None = (
        Noneable(DataclassValidator(InternationalIdentifierOutput)),
        Default(None),
    )
    exAgentExtensionG: ExtensionTypeGOutput | None = (
        Noneable(DataclassValidator(ExtensionTypeGOutput)),
        Default(None),
    )


@validataclass
class ProtocolTypeEnumGOutput(ValidataclassMixin):
    value: ProtocolTypeEnum = EnumValidator(ProtocolTypeEnum)
    extendedValueG: str | None = Noneable(StringValidator(max_length=1024)), Default(None)


@validataclass
class ExchangeContextOutput(ValidataclassMixin):
    codedExchangeProtocol: ProtocolTypeEnumGOutput = DataclassValidator(ProtocolTypeEnumGOutput)
    exchangeSpecificationVersion: str = StringValidator(max_length=1024)
    supplierOrCisRequester: AgentOutput = DataclassValidator(AgentOutput)


@validataclass
class ExchangeStatusEnumGOutput(ValidataclassMixin):
    value: ExchangeStatusEnum = EnumValidator(ExchangeStatusEnum)
    extendedValueG: str | None = Noneable(StringValidator(max_length=1024)), Default(None)


@validataclass
class DynamicInformationOutput(ValidataclassMixin):
    exchangeStatus: ExchangeStatusEnumGOutput = DataclassValidator(ExchangeStatusEnumGOutput)
    messageGenerationTimestamp: datetime = DateTimeValidator()
    exDynamicInformationExtensionG: ExtensionTypeGOutput | None = (
        Noneable(AnythingValidator(allowed_types=[ExtensionTypeGOutput])),
        Default(None),
    )


@validataclass
class ExchangeInformationOutput(ValidataclassMixin):
    exchangeContext: ExchangeContextOutput = DataclassValidator(ExchangeContextOutput)
    dynamicInformation: DynamicInformationOutput = DataclassValidator(DynamicInformationOutput)
    exExchangeInformationExtensionG: ExtensionTypeGOutput | None = (
        Noneable(DataclassValidator(ExtensionTypeGOutput)),
        Default(None),
    )


@validataclass
class MessageContainerOutput(ValidataclassMixin):
    payload: (
        list[
            PayloadPublicationGV35StaticOutput
            | PayloadPublicationGV35RealtimeOutput
            | PayloadPublicationGV37StaticOutput
            | PayloadPublicationGV37RealtimeOutput
        ]
        | None
    ) = (
        Noneable(
            ListValidator(
                MultiValidataclassValidator(
                    PayloadPublicationGV35StaticOutput,
                    PayloadPublicationGV35RealtimeOutput,
                ),
            )
        ),
        Default(None),
    )
    exchangeInformation: ExchangeInformationOutput = DataclassValidator(ExchangeInformationOutput)
    conMessageContainerExtensionG: ExtensionTypeGOutput | None = (
        Noneable(DataclassValidator(ExtensionTypeGOutput)),
        Default(None),
    )


@validataclass
class MessageContainerWrapperOutput(ValidataclassMixin):
    messageContainer: MessageContainerOutput | None = (
        Noneable(DataclassValidator(MessageContainerOutput)),
        Default(None),
    )
    exchangeInformation: ExchangeInformationOutput | None = (
        Noneable(DataclassValidator(ExchangeInformationOutput)),
        Default(None),
    )
