"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .tpeg_framed_point_input import TpegFramedPointInput
from .tpeg_simple_point_input import TpegSimplePointInput


@validataclass
class TpegPointLocationGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    locTpegFramedPoint: TpegFramedPointInput | UnsetValueType = (
        DataclassValidator(TpegFramedPointInput),
        Default(UnsetValue),
    )
    locTpegSimplePoint: TpegSimplePointInput | UnsetValueType = (
        DataclassValidator(TpegSimplePointInput),
        Default(UnsetValue),
    )
