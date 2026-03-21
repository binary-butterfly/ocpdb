"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .tpeg_geometric_area_input import TpegGeometricAreaInput
from .tpeg_named_only_area_input import TpegNamedOnlyAreaInput


@validataclass
class TpegAreaLocationGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    locTpegNamedOnlyArea: TpegNamedOnlyAreaInput | UnsetValueType = (
        DataclassValidator(TpegNamedOnlyAreaInput),
        Default(UnsetValue),
    )
    locTpegGeometricArea: TpegGeometricAreaInput | UnsetValueType = (
        DataclassValidator(TpegGeometricAreaInput),
        Default(UnsetValue),
    )
