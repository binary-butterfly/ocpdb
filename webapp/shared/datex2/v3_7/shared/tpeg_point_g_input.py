"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .tpeg_junction_input import TpegJunctionInput
from .tpeg_non_junction_point_input import TpegNonJunctionPointInput


@validataclass
class TpegPointGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    locTpegNonJunctionPoint: TpegNonJunctionPointInput | UnsetValueType = (
        DataclassValidator(TpegNonJunctionPointInput),
        Default(UnsetValue),
    )
    locTpegJunction: TpegJunctionInput | UnsetValueType = DataclassValidator(TpegJunctionInput), Default(UnsetValue)
