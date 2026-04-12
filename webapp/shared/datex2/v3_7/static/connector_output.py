"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from webapp.shared.datex2.v3_7.shared.extension_type_g_output import ExtensionTypeGOutput

from .connector_format_type_enum_g_output import ConnectorFormatTypeEnumGOutput
from .connector_type_enum_g_output import ConnectorTypeEnumGOutput
from .external_identifier_output import ExternalIdentifierOutput


@dataclass(kw_only=True)
class ConnectorOutput:
    connectorType: ConnectorTypeEnumGOutput
    otherConnector: str | None = None
    countryOfDomesticSocket: list[str] | None = None
    connectorFormat: ConnectorFormatTypeEnumGOutput | None = None
    maxPowerAtSocket: float
    voltage: float | None = None
    maximumCurrent: float | None = None
    externalIdentifier: list[ExternalIdentifierOutput] | None = None
    aegiConnectorExtensionG: ExtensionTypeGOutput | None = None
