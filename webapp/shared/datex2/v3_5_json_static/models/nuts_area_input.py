"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .nuts_code_type_enum_g_input import NutsCodeTypeEnumGInput


@validataclass
class NutsAreaInput(ValidataclassMixin):
    """
    The NUTS-Code representation for the area (Nomenclature of territorial units for statistics) or its LAU code representation (Local Administrative Unit).
    """

    nutsCodeType: NutsCodeTypeEnumGInput = DataclassValidator(NutsCodeTypeEnumGInput)
    nutsCode: str = StringValidator(max_length=5)
    locxNutsAreaExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
