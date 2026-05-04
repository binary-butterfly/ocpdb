"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput

from .gdd_service_category_enum_g_input import GddServiceCategoryEnumGInput


@validataclass
class GddPictogramIdentificationInput(ValidataclassMixin):
    country: str = StringValidator(max_length=2)
    serviceCategory: GddServiceCategoryEnumGInput = DataclassValidator(GddServiceCategoryEnumGInput)
    pictogramCategoryCode: int = IntegerValidator()
    vmsGddPictogramIdentificationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
