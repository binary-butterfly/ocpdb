"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import ValidataclassMixin, validataclass
from validataclass.validators import RegexValidator, StringValidator


@validataclass
class MultiLingualStringValueInput(ValidataclassMixin):
    lang: str = RegexValidator(pattern=r'^[a-z]{2}$')
    value: str = StringValidator()
