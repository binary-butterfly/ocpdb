"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .age_characteristic_input import AgeCharacteristicInput
from .regulated_characteristics_input import RegulatedCharacteristicsInput
from .trailer_characteristics_input import TrailerCharacteristicsInput


@validataclass
class VehicleCharacteristicsExtendedInput(ValidataclassMixin):
    """
    Extension class for vehicle characteristics.
    """

    ageCharacteristic: list[AgeCharacteristicInput] | UnsetValueType = (
        ListValidator(DataclassValidator(AgeCharacteristicInput)),
        Default(UnsetValue),
    )
    trailerCharacteristics: TrailerCharacteristicsInput | UnsetValueType = (
        DataclassValidator(TrailerCharacteristicsInput),
        Default(UnsetValue),
    )
    regulatedCharacteristics: list[RegulatedCharacteristicsInput] | UnsetValueType = (
        ListValidator(DataclassValidator(RegulatedCharacteristicsInput)),
        Default(UnsetValue),
    )
