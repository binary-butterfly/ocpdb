"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, RegexValidator

from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class GddPictogramAttributesInput(ValidataclassMixin):
    attributes: str = RegexValidator(pattern=r'^[A-Za-z0-9+/]+={0,2}$')
    vmsGddPictogramAttributesExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
