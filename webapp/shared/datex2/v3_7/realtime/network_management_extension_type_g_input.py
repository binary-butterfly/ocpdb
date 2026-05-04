"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from webapp.shared.datex2.v3_7.shared.network_management_extended_urban_input import NetworkManagementExtendedUrbanInput

from .capacity_management_input import CapacityManagementInput
from .rerouting_management_enhanced_input import ReroutingManagementEnhancedInput
from .sign_setting_input import SignSettingInput


@validataclass
class NetworkManagementExtensionTypeGInput(ValidataclassMixin):
    NetworkManagementExtendedUrban: NetworkManagementExtendedUrbanInput | UnsetValueType = (
        DataclassValidator(NetworkManagementExtendedUrbanInput),
        Default(UnsetValue),
    )
    ReroutingManagementEnhanced: ReroutingManagementEnhancedInput | UnsetValueType = (
        DataclassValidator(ReroutingManagementEnhancedInput),
        Default(UnsetValue),
    )
    SignSetting: SignSettingInput | UnsetValueType = DataclassValidator(SignSettingInput), Default(UnsetValue)
    CapacityManagement: CapacityManagementInput | UnsetValueType = (
        DataclassValidator(CapacityManagementInput),
        Default(UnsetValue),
    )
