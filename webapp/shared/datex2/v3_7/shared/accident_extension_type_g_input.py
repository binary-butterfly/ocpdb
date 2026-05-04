"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .accident_extended_urban_input import AccidentExtendedUrbanInput


@validataclass
class AccidentExtensionTypeGInput(ValidataclassMixin):
    AccidentExtendedUrban: AccidentExtendedUrbanInput | UnsetValueType = (
        DataclassValidator(AccidentExtendedUrbanInput),
        Default(UnsetValue),
    )
