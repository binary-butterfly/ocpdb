"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .dynamic_traffic_management_input import DynamicTrafficManagementInput


@validataclass
class DynamicTrafficRegulationGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    troDynamicTrafficManagement: DynamicTrafficManagementInput | UnsetValueType = (
        DataclassValidator(DynamicTrafficManagementInput),
        Default(UnsetValue),
    )
