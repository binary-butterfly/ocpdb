"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .operator_action_extended_tmplan_input import OperatorActionExtendedTmplanInput


@validataclass
class OperatorActionExtensionTypeGInput(ValidataclassMixin):
    OperatorActionExtendedTmplan: OperatorActionExtendedTmplanInput | UnsetValueType = (
        DataclassValidator(OperatorActionExtendedTmplanInput),
        Default(UnsetValue),
    )
