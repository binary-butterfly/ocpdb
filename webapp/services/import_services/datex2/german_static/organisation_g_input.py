"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .an_organisation_input import AnOrganisationInput
from .organisation_by_reference_input import OrganisationByReferenceInput
from .referenceable_organisation_input import ReferenceableOrganisationInput
from .undefined_organisation_input import UndefinedOrganisationInput
from .unknown_organisation_input import UnknownOrganisationInput


@validataclass
class OrganisationGInput:
    afacAnOrganisation: AnOrganisationInput | UnsetValueType = (
        DataclassValidator(AnOrganisationInput),
        Default(UnsetValue),
    )
    afacReferenceableOrganisation: ReferenceableOrganisationInput | UnsetValueType = (
        DataclassValidator(ReferenceableOrganisationInput),
        Default(UnsetValue),
    )
    afacUndefinedOrganisation: UndefinedOrganisationInput | UnsetValueType = (
        DataclassValidator(UndefinedOrganisationInput),
        Default(UnsetValue),
    )
    afacUnknownOrganisation: UnknownOrganisationInput | UnsetValueType = (
        DataclassValidator(UnknownOrganisationInput),
        Default(UnsetValue),
    )
    afacOrganisationByReference: OrganisationByReferenceInput | UnsetValueType = (
        DataclassValidator(OrganisationByReferenceInput),
        Default(UnsetValue),
    )
