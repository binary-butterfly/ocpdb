"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .tmplan_implementing_action_input import TmplanImplementingActionInput


@validataclass
class OperatorActionExtendedTmplanInput(ValidataclassMixin):
    tmplanImplementingAction: TmplanImplementingActionInput | UnsetValueType = (
        DataclassValidator(TmplanImplementingActionInput),
        Default(UnsetValue),
    )
