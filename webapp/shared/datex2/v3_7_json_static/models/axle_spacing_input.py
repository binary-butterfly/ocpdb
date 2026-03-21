"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator, IntegerValidator

from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class AxleSpacingInput(ValidataclassMixin):
    """
    The spacing details between the axle sets of an individual vehicle numbered from the front to the back of the vehicle.
    """

    axleSpacing: int = FloatValidator()
    axleSpacingSequenceIdentifier: int = IntegerValidator(min_value=0)
    comAxleSpacingExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
