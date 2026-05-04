"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, StringValidator

from .alert_c_direction_input import AlertCDirectionInput
from .alert_c_method4_primary_point_location_input import AlertCMethod4PrimaryPointLocationInput
from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class AlertCMethod4PointInput(ValidataclassMixin):
    alertCLocationCountryCode: str = StringValidator()
    alertCLocationTableNumber: str = StringValidator()
    alertCLocationTableVersion: str = StringValidator()
    alertCDirection: AlertCDirectionInput = DataclassValidator(AlertCDirectionInput)
    alertCMethod4PrimaryPointLocation: AlertCMethod4PrimaryPointLocationInput = DataclassValidator(
        AlertCMethod4PrimaryPointLocationInput
    )
    locAlertCPointExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locAlertCMethod4PointExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
