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
from .referent_type_enum_g_input import ReferentTypeEnumGInput


@validataclass
class ReferentInput(ValidataclassMixin):
    referentIdentifier: str = StringValidator()
    referentName: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    referentType: ReferentTypeEnumGInput = DataclassValidator(ReferentTypeEnumGInput)
    referentDescription: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    pointCoordinates: PointCoordinatesInput | UnsetValueType = (
        DataclassValidator(PointCoordinatesInput),
        Default(UnsetValue),
    )
    locReferentExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
