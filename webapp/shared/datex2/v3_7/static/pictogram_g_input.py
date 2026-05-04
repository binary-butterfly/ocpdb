"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .composite_pictogram_input import CompositePictogramInput
from .regular_pictogram_input import RegularPictogramInput


@validataclass
class PictogramGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    vmsCompositePictogram: CompositePictogramInput | UnsetValueType = (
        DataclassValidator(CompositePictogramInput),
        Default(UnsetValue),
    )
    vmsRegularPictogram: RegularPictogramInput | UnsetValueType = (
        DataclassValidator(RegularPictogramInput),
        Default(UnsetValue),
    )
