"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class InternationalIdentifierInput:
    country: str = StringValidator(max_length=2)
    nationalIdentifier: str = StringValidator()
    comInternationalIdentifierExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
