"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import ValidataclassMixin, validataclass
from validataclass.validators import DataclassValidator

from .sign_setting_definition_input import SignSettingDefinitionInput


@validataclass(reject_unknown_fields=True)
class SignSettingInput(ValidataclassMixin):
    signSettingDefinition: SignSettingDefinitionInput = DataclassValidator(SignSettingDefinitionInput)
