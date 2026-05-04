"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import ValidataclassMixin, validataclass
from validataclass.validators import DataclassValidator

from .street_works_type_enum_g_input import StreetWorksTypeEnumGInput


@validataclass
class StreetWorksInput(ValidataclassMixin):
    streetWorksType: StreetWorksTypeEnumGInput = DataclassValidator(StreetWorksTypeEnumGInput)
