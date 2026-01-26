"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .vehicle_to_grid_communication_type_enum import VehicleToGridCommunicationTypeEnum


@validataclass
class VehicleToGridCommunicationTypeEnumGInput:
    value: VehicleToGridCommunicationTypeEnum = EnumValidator(VehicleToGridCommunicationTypeEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
