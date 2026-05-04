"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    BooleanValidator,
    DataclassValidator,
    DateTimeValidator,
    IntegerValidator,
    ListValidator,
)

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.facility_object_versioned_reference_g_input import (
    FacilityObjectVersionedReferenceGInput,
)
from webapp.shared.datex2.v3_7.shared.measurement_or_calculation_time_input import MeasurementOrCalculationTimeInput
from webapp.shared.datex2.v3_7.shared.measurement_site_versioned_reference_g_input import (
    MeasurementSiteVersionedReferenceGInput,
)

from .vehicle_count_within_interval_input import VehicleCountWithinIntervalInput
from .vehicle_rate_input import VehicleRateInput


@validataclass
class VehicleCountAndRateInput(ValidataclassMixin):
    measurementSiteReference: MeasurementSiteVersionedReferenceGInput | UnsetValueType = (
        DataclassValidator(MeasurementSiteVersionedReferenceGInput),
        Default(UnsetValue),
    )
    measuredValueIndex: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    dedicatedAccess: FacilityObjectVersionedReferenceGInput | UnsetValueType = (
        DataclassValidator(FacilityObjectVersionedReferenceGInput),
        Default(UnsetValue),
    )
    lastCalibration: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    coveringPetrolStationArea: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    vehicleCountWithinInterval: list[VehicleCountWithinIntervalInput] | UnsetValueType = (
        ListValidator(DataclassValidator(VehicleCountWithinIntervalInput)),
        Default(UnsetValue),
    )
    vehicleRate: list[VehicleRateInput] | UnsetValueType = (
        ListValidator(DataclassValidator(VehicleRateInput)),
        Default(UnsetValue),
    )
    measurementTimeDefault: MeasurementOrCalculationTimeInput | UnsetValueType = (
        DataclassValidator(MeasurementOrCalculationTimeInput),
        Default(UnsetValue),
    )
    prkVehicleCountAndRateExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
