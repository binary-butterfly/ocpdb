"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator

from .charging_mode_enum_g_input import ChargingModeEnumGInput
from .connector_format_type_enum_g_input import ConnectorFormatTypeEnumGInput
from .connector_type_enum_g_input import ConnectorTypeEnumGInput
from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class ConnectorInput(ValidataclassMixin):
    """
    Parameters and description of an interface that is available at the given electric charging point to connect vehicles
    """

    connectorType: ConnectorTypeEnumGInput = DataclassValidator(ConnectorTypeEnumGInput)
    chargingMode: ChargingModeEnumGInput | UnsetValueType = (
        DataclassValidator(ChargingModeEnumGInput),
        Default(UnsetValue),
    )
    connectorFormat: ConnectorFormatTypeEnumGInput | UnsetValueType = (
        DataclassValidator(ConnectorFormatTypeEnumGInput),
        Default(UnsetValue),
    )
    maxPowerAtSocket: int = FloatValidator()
    voltage: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    maximumCurrent: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    egiConnectorExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
