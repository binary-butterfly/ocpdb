"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .openlr_last_location_reference_point_input import OpenlrLastLocationReferencePointInput
from .openlr_location_reference_point_input import OpenlrLocationReferencePointInput


@validataclass
class OpenlrBaseReferencePointGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    locOpenlrLocationReferencePoint: OpenlrLocationReferencePointInput | UnsetValueType = (
        DataclassValidator(OpenlrLocationReferencePointInput),
        Default(UnsetValue),
    )
    locOpenlrLastLocationReferencePoint: OpenlrLastLocationReferencePointInput | UnsetValueType = (
        DataclassValidator(OpenlrLastLocationReferencePointInput),
        Default(UnsetValue),
    )
