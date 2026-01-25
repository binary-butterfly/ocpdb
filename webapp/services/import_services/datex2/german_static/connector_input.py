"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator, ListValidator, StringValidator

from .connector_format_type_enum_g_input import ConnectorFormatTypeEnumGInput
from .connector_type_enum_g_input import ConnectorTypeEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .external_identifier_input import ExternalIdentifierInput


@validataclass
class ConnectorInput:
    connectorType: ConnectorTypeEnumGInput = DataclassValidator(ConnectorTypeEnumGInput)
    otherConnector: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    countryOfDomesticSocket: list[str] | UnsetValueType = (
        ListValidator(StringValidator(max_length=2)),
        Default(UnsetValue),
    )
    connectorFormat: ConnectorFormatTypeEnumGInput | UnsetValueType = (
        DataclassValidator(ConnectorFormatTypeEnumGInput),
        Default(UnsetValue),
    )
    maxPowerAtSocket: int = FloatValidator()
    voltage: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    maximumCurrent: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    externalIdentifier: list[ExternalIdentifierInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ExternalIdentifierInput)),
        Default(UnsetValue),
    )
    aegiConnectorExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
