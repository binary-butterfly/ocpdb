"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .micrograms_concentration_value_input import MicrogramsConcentrationValueInput
from .pollutant_type_enum_g_input import PollutantTypeEnumGInput


@validataclass
class PollutionInput(ValidataclassMixin):
    pollutantType: PollutantTypeEnumGInput = DataclassValidator(PollutantTypeEnumGInput)
    pollutantConcentration: MicrogramsConcentrationValueInput | UnsetValueType = (
        DataclassValidator(MicrogramsConcentrationValueInput),
        Default(UnsetValue),
    )
    comPollutionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
