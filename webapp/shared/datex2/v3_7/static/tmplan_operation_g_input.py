"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .non_predefined_tmplan_operation_input import NonPredefinedTmplanOperationInput
from .predefined_tmplan_operation_input import PredefinedTmplanOperationInput


@validataclass
class TmplanOperationGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    tmpNonPredefinedTmplanOperation: NonPredefinedTmplanOperationInput | UnsetValueType = (
        DataclassValidator(NonPredefinedTmplanOperationInput),
        Default(UnsetValue),
    )
    tmpPredefinedTmplanOperation: PredefinedTmplanOperationInput | UnsetValueType = (
        DataclassValidator(PredefinedTmplanOperationInput),
        Default(UnsetValue),
    )
