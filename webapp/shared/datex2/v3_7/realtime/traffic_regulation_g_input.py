"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .controlled_zone_regulation_input import ControlledZoneRegulationInput
from .traffic_regulation_input import TrafficRegulationInput


@validataclass
class TrafficRegulationGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    troTrafficRegulation: TrafficRegulationInput | UnsetValueType = (
        DataclassValidator(TrafficRegulationInput),
        Default(UnsetValue),
    )
    czControlledZoneRegulation: ControlledZoneRegulationInput | UnsetValueType = (
        DataclassValidator(ControlledZoneRegulationInput),
        Default(UnsetValue),
    )
