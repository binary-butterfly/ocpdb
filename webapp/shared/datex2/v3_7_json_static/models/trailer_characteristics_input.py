"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .gross_trailer_weight_characteristics_input import GrossTrailerWeightCharacteristicsInput


@validataclass
class TrailerCharacteristicsInput(ValidataclassMixin):
    """
    The characteristics of a trailer e.g. gross weight of trailer.
    """

    grossTrailerWeightCharacteristics: list[GrossTrailerWeightCharacteristicsInput] | UnsetValueType = (
        ListValidator(DataclassValidator(GrossTrailerWeightCharacteristicsInput)),
        Default(UnsetValue),
    )
    comxTrailerCharacteristicsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
