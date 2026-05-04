"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .temporary_traffic_regulation_order_input import TemporaryTrafficRegulationOrderInput
from .traffic_regulation_order_input import TrafficRegulationOrderInput


@validataclass
class TrafficRegulationOrderGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    troTrafficRegulationOrder: TrafficRegulationOrderInput | UnsetValueType = (
        DataclassValidator(TrafficRegulationOrderInput),
        Default(UnsetValue),
    )
    troTemporaryTrafficRegulationOrder: TemporaryTrafficRegulationOrderInput | UnsetValueType = (
        DataclassValidator(TemporaryTrafficRegulationOrderInput),
        Default(UnsetValue),
    )
