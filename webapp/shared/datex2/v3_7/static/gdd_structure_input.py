"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.gdd_pictogram_attributes_input import GddPictogramAttributesInput

from .gdd_pictogram_identification_input import GddPictogramIdentificationInput


@validataclass
class GddStructureInput(ValidataclassMixin):
    gddPictogramIdentification: GddPictogramIdentificationInput = DataclassValidator(GddPictogramIdentificationInput)
    gddPictogramAttributes: GddPictogramAttributesInput | UnsetValueType = (
        DataclassValidator(GddPictogramAttributesInput),
        Default(UnsetValue),
    )
    vmsGddStructureExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
