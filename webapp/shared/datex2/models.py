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

from dataclasses import dataclass
from datetime import datetime
from enum import Enum

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


@dataclass(kw_only=True)
class AgentOutput:
    address: str | None = None
    name: str | None = None
    referenceID: str | None = None
    serviceURL: str | None = None
    internationalIdentifier: InternationalIdentifierOutput | None = None
    exAgentExtensionG: ExtensionTypeGOutput | None = None


@dataclass(kw_only=True)
class ProtocolTypeEnumGOutput:
    value: ProtocolTypeEnum
    extendedValueG: str | None = None


@dataclass(kw_only=True)
class ExchangeContextOutput:
    codedExchangeProtocol: ProtocolTypeEnumGOutput
    exchangeSpecificationVersion: str
    supplierOrCisRequester: AgentOutput


@dataclass(kw_only=True)
class ExchangeStatusEnumGOutput:
    value: ExchangeStatusEnum
    extendedValueG: str | None = None


@dataclass(kw_only=True)
class DynamicInformationOutput:
    exchangeStatus: ExchangeStatusEnumGOutput
    messageGenerationTimestamp: datetime
    exDynamicInformationExtensionG: ExtensionTypeGOutput | None = None


@dataclass(kw_only=True)
class ExchangeInformationOutput:
    exchangeContext: ExchangeContextOutput
    dynamicInformation: DynamicInformationOutput
    exExchangeInformationExtensionG: ExtensionTypeGOutput | None = None


@dataclass(kw_only=True)
class MessageContainerOutput:
    payload: (
        PayloadPublicationGV35StaticOutput
        | PayloadPublicationGV35RealtimeOutput
        | PayloadPublicationGV37StaticOutput
        | PayloadPublicationGV37RealtimeOutput
        | None
    ) = None
    exchangeInformation: ExchangeInformationOutput
    conMessageContainerExtensionG: ExtensionTypeGOutput | None = None


@dataclass(kw_only=True)
class MessageContainerWrapperOutput:
    message_container: MessageContainerOutput | None = None
    exchangeInformation: ExchangeInformationOutput | None = None
