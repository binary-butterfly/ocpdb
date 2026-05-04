"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import ValidataclassMixin, validataclass
from validataclass.validators import DataclassValidator, IntegerValidator

from .vms_message_input import VmsMessageInput


@validataclass
class vmsStatusMessageIndexVmsMessageGInput(ValidataclassMixin):
    vmsMessage: VmsMessageInput = DataclassValidator(VmsMessageInput)
    messageIndex: int = IntegerValidator()
