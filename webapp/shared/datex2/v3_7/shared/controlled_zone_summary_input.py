"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .point_coordinates_input import PointCoordinatesInput


@validataclass
class ControlledZoneSummaryInput(ValidataclassMixin):
    cityName: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    informalName: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    urlForFurtherInformation: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    locationForDisplay: PointCoordinatesInput | UnsetValueType = (
        DataclassValidator(PointCoordinatesInput),
        Default(UnsetValue),
    )
    czControlledZoneSummaryExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
