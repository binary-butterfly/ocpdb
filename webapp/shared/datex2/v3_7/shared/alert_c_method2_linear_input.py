"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, StringValidator

from .alert_c_direction_input import AlertCDirectionInput
from .alert_c_method2_primary_point_location_input import AlertCMethod2PrimaryPointLocationInput
from .alert_c_method2_secondary_point_location_input import AlertCMethod2SecondaryPointLocationInput
from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class AlertCMethod2LinearInput(ValidataclassMixin):
    alertCLocationCountryCode: str = StringValidator()
    alertCLocationTableNumber: str = StringValidator()
    alertCLocationTableVersion: str = StringValidator()
    alertCDirection: AlertCDirectionInput = DataclassValidator(AlertCDirectionInput)
    alertCMethod2PrimaryPointLocation: AlertCMethod2PrimaryPointLocationInput = DataclassValidator(
        AlertCMethod2PrimaryPointLocationInput
    )
    alertCMethod2SecondaryPointLocation: AlertCMethod2SecondaryPointLocationInput = DataclassValidator(
        AlertCMethod2SecondaryPointLocationInput
    )
    locAlertCLinearExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locAlertCMethod2LinearExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
