"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, DateTimeValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .facility_object_reference_g_input import FacilityObjectReferenceGInput
from .occupancy_level_input import OccupancyLevelInput


@validataclass
class DemandSpaceTypeInput(ValidataclassMixin):
    spaceId: list[FacilityObjectReferenceGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(FacilityObjectReferenceGInput)),
        Default(UnsetValue),
    )
    actualStart: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    actualEnd: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    detectionUpdateTime: datetime = DateTimeValidator()
    estimatedStart: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    estimatedEnd: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    occupancyLevel: OccupancyLevelInput | UnsetValueType = DataclassValidator(OccupancyLevelInput), Default(UnsetValue)
    prkDemandSpaceTypeExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
