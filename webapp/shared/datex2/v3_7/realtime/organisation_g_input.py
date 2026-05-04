"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from webapp.shared.datex2.v3_7.shared.organisation_by_reference_input import OrganisationByReferenceInput
from webapp.shared.datex2.v3_7.shared.undefined_organisation_input import UndefinedOrganisationInput
from webapp.shared.datex2.v3_7.shared.unknown_organisation_input import UnknownOrganisationInput

from .an_organisation_input import AnOrganisationInput
from .referenceable_organisation_input import ReferenceableOrganisationInput


@validataclass
class OrganisationGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    afacUndefinedOrganisation: UndefinedOrganisationInput | UnsetValueType = (
        DataclassValidator(UndefinedOrganisationInput),
        Default(UnsetValue),
    )
    afacOrganisationByReference: OrganisationByReferenceInput | UnsetValueType = (
        DataclassValidator(OrganisationByReferenceInput),
        Default(UnsetValue),
    )
    afacUnknownOrganisation: UnknownOrganisationInput | UnsetValueType = (
        DataclassValidator(UnknownOrganisationInput),
        Default(UnsetValue),
    )
    afacAnOrganisation: AnOrganisationInput | UnsetValueType = (
        DataclassValidator(AnOrganisationInput),
        Default(UnsetValue),
    )
    afacReferenceableOrganisation: ReferenceableOrganisationInput | UnsetValueType = (
        DataclassValidator(ReferenceableOrganisationInput),
        Default(UnsetValue),
    )
