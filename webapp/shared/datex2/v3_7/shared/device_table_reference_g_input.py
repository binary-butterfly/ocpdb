"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .general_device_table_reference_input import GeneralDeviceTableReferenceInput
from .measurement_site_table_reference_input import MeasurementSiteTableReferenceInput
from .vms_unit_table_reference_input import VmsUnitTableReferenceInput


@validataclass
class DeviceTableReferenceGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    fstMeasurementSiteTableReference: MeasurementSiteTableReferenceInput | UnsetValueType = (
        DataclassValidator(MeasurementSiteTableReferenceInput),
        Default(UnsetValue),
    )
    fstGeneralDeviceTableReference: GeneralDeviceTableReferenceInput | UnsetValueType = (
        DataclassValidator(GeneralDeviceTableReferenceInput),
        Default(UnsetValue),
    )
    fstVmsUnitTableReference: VmsUnitTableReferenceInput | UnsetValueType = (
        DataclassValidator(VmsUnitTableReferenceInput),
        Default(UnsetValue),
    )
