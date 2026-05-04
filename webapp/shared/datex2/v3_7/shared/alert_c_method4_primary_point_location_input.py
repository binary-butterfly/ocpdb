"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .alert_c_location_input import AlertCLocationInput
from .extension_type_g_input import ExtensionTypeGInput
from .offset_distance_input import OffsetDistanceInput


@validataclass
class AlertCMethod4PrimaryPointLocationInput(ValidataclassMixin):
    alertCLocation: AlertCLocationInput = DataclassValidator(AlertCLocationInput)
    offsetDistance: OffsetDistanceInput = DataclassValidator(OffsetDistanceInput)
    locAlertCMethod4PrimaryPointLocationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
