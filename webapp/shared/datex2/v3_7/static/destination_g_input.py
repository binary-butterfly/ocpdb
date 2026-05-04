"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from webapp.shared.datex2.v3_7.shared.area_destination_input import AreaDestinationInput

from .point_destination_input import PointDestinationInput


@validataclass
class DestinationGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    locAreaDestination: AreaDestinationInput | UnsetValueType = (
        DataclassValidator(AreaDestinationInput),
        Default(UnsetValue),
    )
    locPointDestination: PointDestinationInput | UnsetValueType = (
        DataclassValidator(PointDestinationInput),
        Default(UnsetValue),
    )
