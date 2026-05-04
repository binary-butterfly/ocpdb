"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import ValidataclassMixin, validataclass
from validataclass.validators import DataclassValidator, IntegerValidator

from .measurement_specific_characteristics_input import MeasurementSpecificCharacteristicsInput


@validataclass
class measurementSiteIndexMeasurementSpecificCharacteristicsGInput(ValidataclassMixin):
    measurementSpecificCharacteristics: MeasurementSpecificCharacteristicsInput = DataclassValidator(
        MeasurementSpecificCharacteristicsInput
    )
    index: int = IntegerValidator()
