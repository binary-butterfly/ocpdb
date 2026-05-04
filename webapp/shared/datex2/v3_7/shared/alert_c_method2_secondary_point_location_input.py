"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .alert_c_location_input import AlertCLocationInput
from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class AlertCMethod2SecondaryPointLocationInput(ValidataclassMixin):
    alertCLocation: AlertCLocationInput = DataclassValidator(AlertCLocationInput)
    locAlertCMethod2SecondaryPointLocationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
