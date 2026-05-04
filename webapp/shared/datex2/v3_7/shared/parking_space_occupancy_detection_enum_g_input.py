"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .parking_space_occupancy_detection_enum import ParkingSpaceOccupancyDetectionEnum


@validataclass
class ParkingSpaceOccupancyDetectionEnumGInput(ValidataclassMixin):
    value: ParkingSpaceOccupancyDetectionEnum = EnumValidator(ParkingSpaceOccupancyDetectionEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
