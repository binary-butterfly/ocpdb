"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.owner_type_enum_g_input import OwnerTypeEnumGInput

from .location_reference_g_input import LocationReferenceGInput


@validataclass
class OwnerCharacteristicInput(ValidataclassMixin):
    ownerType: OwnerTypeEnumGInput = DataclassValidator(OwnerTypeEnumGInput)
    locationOfResidency: LocationReferenceGInput | UnsetValueType = (
        DataclassValidator(LocationReferenceGInput),
        Default(UnsetValue),
    )
    comxOwnerCharacteristicExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
