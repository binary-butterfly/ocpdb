"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from webapp.shared.datex2.v3_7.shared.action_by_reference_input import ActionByReferenceInput

from .action_definition_input import ActionDefinitionInput


@validataclass
class ActionGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    tmpActionByReference: ActionByReferenceInput | UnsetValueType = (
        DataclassValidator(ActionByReferenceInput),
        Default(UnsetValue),
    )
    tmpActionDefinition: ActionDefinitionInput | UnsetValueType = (
        DataclassValidator(ActionDefinitionInput),
        Default(UnsetValue),
    )
