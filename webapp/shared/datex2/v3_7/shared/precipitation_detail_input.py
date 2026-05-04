"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .floating_point_metre_distance_value_input import FloatingPointMetreDistanceValueInput
from .precipitation_intensity_enum_g_input import PrecipitationIntensityEnumGInput
from .precipitation_intensity_value_input import PrecipitationIntensityValueInput
from .precipitation_type_enum_g_input import PrecipitationTypeEnumGInput


@validataclass
class PrecipitationDetailInput(ValidataclassMixin):
    precipitationType: PrecipitationTypeEnumGInput | UnsetValueType = (
        DataclassValidator(PrecipitationTypeEnumGInput),
        Default(UnsetValue),
    )
    precipitationIntensityGrade: PrecipitationIntensityEnumGInput | UnsetValueType = (
        DataclassValidator(PrecipitationIntensityEnumGInput),
        Default(UnsetValue),
    )
    precipitationIntensity: PrecipitationIntensityValueInput | UnsetValueType = (
        DataclassValidator(PrecipitationIntensityValueInput),
        Default(UnsetValue),
    )
    depositionDepth: FloatingPointMetreDistanceValueInput | UnsetValueType = (
        DataclassValidator(FloatingPointMetreDistanceValueInput),
        Default(UnsetValue),
    )
    comPrecipitationDetailExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
