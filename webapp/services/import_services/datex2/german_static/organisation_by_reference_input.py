"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .organisation_table_versioned_reference_g_input import OrganisationTableVersionedReferenceGInput
from .overall_period_input import OverallPeriodInput
from .referenceable_organisation_versioned_reference_g_input import ReferenceableOrganisationVersionedReferenceGInput


@validataclass
class OrganisationByReferenceInput:
    organisationReference: ReferenceableOrganisationVersionedReferenceGInput = DataclassValidator(
        ReferenceableOrganisationVersionedReferenceGInput
    )
    organisationTableReference: OrganisationTableVersionedReferenceGInput | UnsetValueType = (
        DataclassValidator(OrganisationTableVersionedReferenceGInput),
        Default(UnsetValue),
    )
    generalTimeValidity: OverallPeriodInput | UnsetValueType = (
        DataclassValidator(OverallPeriodInput),
        Default(UnsetValue),
    )
    afacOrganisationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    afacOrganisationByReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
