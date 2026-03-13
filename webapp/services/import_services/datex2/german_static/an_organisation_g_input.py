"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .an_organisation_input import AnOrganisationInput
from .referenceable_organisation_input import ReferenceableOrganisationInput


@validataclass
class AnOrganisationGInput:
    afacAnOrganisation: AnOrganisationInput | UnsetValueType = (
        DataclassValidator(AnOrganisationInput),
        Default(UnsetValue),
    )
    afacReferenceableOrganisation: ReferenceableOrganisationInput | UnsetValueType = (
        DataclassValidator(ReferenceableOrganisationInput),
        Default(UnsetValue),
    )
