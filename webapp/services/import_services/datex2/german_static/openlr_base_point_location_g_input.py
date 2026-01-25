"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .openlr_poi_with_access_point_input import OpenlrPoiWithAccessPointInput
from .openlr_point_along_line_input import OpenlrPointAlongLineInput


@validataclass
class OpenlrBasePointLocationGInput:
    locOpenlrPointAlongLine: OpenlrPointAlongLineInput | UnsetValueType = (
        DataclassValidator(OpenlrPointAlongLineInput),
        Default(UnsetValue),
    )
    locOpenlrPoiWithAccessPoint: OpenlrPoiWithAccessPointInput | UnsetValueType = (
        DataclassValidator(OpenlrPoiWithAccessPointInput),
        Default(UnsetValue),
    )
