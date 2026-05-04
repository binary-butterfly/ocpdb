"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .general_device_reference_input import GeneralDeviceReferenceInput
from .measurement_site_reference_input import MeasurementSiteReferenceInput
from .vms_unit_reference_input import VmsUnitReferenceInput


@validataclass
class DeviceReferenceGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    fstVmsUnitReference: VmsUnitReferenceInput | UnsetValueType = (
        DataclassValidator(VmsUnitReferenceInput),
        Default(UnsetValue),
    )
    fstMeasurementSiteReference: MeasurementSiteReferenceInput | UnsetValueType = (
        DataclassValidator(MeasurementSiteReferenceInput),
        Default(UnsetValue),
    )
    fstGeneralDeviceReference: GeneralDeviceReferenceInput | UnsetValueType = (
        DataclassValidator(GeneralDeviceReferenceInput),
        Default(UnsetValue),
    )
