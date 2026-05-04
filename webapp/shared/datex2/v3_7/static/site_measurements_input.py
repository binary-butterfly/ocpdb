"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.measurement_or_calculation_time_input import MeasurementOrCalculationTimeInput
from webapp.shared.datex2.v3_7.shared.measurement_site_versioned_reference_g_input import (
    MeasurementSiteVersionedReferenceGInput,
)

from .site_measurements_index_physical_quantity_g_input import siteMeasurementsIndexPhysicalQuantityGInput


@validataclass
class SiteMeasurementsInput(ValidataclassMixin):
    measurementSiteReference: MeasurementSiteVersionedReferenceGInput = DataclassValidator(
        MeasurementSiteVersionedReferenceGInput
    )
    physicalQuantity: list[siteMeasurementsIndexPhysicalQuantityGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(siteMeasurementsIndexPhysicalQuantityGInput)),
        Default(UnsetValue),
    )
    measurementTimeDefault: MeasurementOrCalculationTimeInput = DataclassValidator(MeasurementOrCalculationTimeInput)
    roaSiteMeasurementsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
