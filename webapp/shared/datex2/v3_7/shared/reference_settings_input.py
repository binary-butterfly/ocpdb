"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .predefined_location_group_versioned_reference_g_input import PredefinedLocationGroupVersionedReferenceGInput
from .traffic_status_enum_g_input import TrafficStatusEnumGInput


@validataclass
class ReferenceSettingsInput(ValidataclassMixin):
    predefinedLocationGroupReference: PredefinedLocationGroupVersionedReferenceGInput = DataclassValidator(
        PredefinedLocationGroupVersionedReferenceGInput
    )
    trafficStatusDefault: TrafficStatusEnumGInput | UnsetValueType = (
        DataclassValidator(TrafficStatusEnumGInput),
        Default(UnsetValue),
    )
    roaReferenceSettingsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
