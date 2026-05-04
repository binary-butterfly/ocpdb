"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from webapp.shared.datex2.v3_7.shared.composite_measure_input import CompositeMeasureInput
from webapp.shared.datex2.v3_7.shared.measure_by_reference_input import MeasureByReferenceInput

from .measure_definition_input import MeasureDefinitionInput


@validataclass
class MeasureGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    tmpMeasureDefinition: MeasureDefinitionInput | UnsetValueType = (
        DataclassValidator(MeasureDefinitionInput),
        Default(UnsetValue),
    )
    tmpCompositeMeasure: CompositeMeasureInput | UnsetValueType = (
        DataclassValidator(CompositeMeasureInput),
        Default(UnsetValue),
    )
    tmpMeasureByReference: MeasureByReferenceInput | UnsetValueType = (
        DataclassValidator(MeasureByReferenceInput),
        Default(UnsetValue),
    )
