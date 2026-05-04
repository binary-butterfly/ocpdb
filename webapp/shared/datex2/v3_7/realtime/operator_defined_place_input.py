"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput

from .organisation_g_input import OrganisationGInput


@validataclass
class OperatorDefinedPlaceInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    identifier: str = StringValidator()
    organisation: list[OrganisationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(OrganisationGInput)),
        Default(UnsetValue),
    )
    prkOperatorDefinedPlaceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
