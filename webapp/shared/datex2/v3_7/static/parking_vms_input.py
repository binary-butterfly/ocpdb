"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.vms_controller_versioned_reference_g_input import (
    VmsControllerVersionedReferenceGInput,
)

from .organisation_g_input import OrganisationGInput


@validataclass
class ParkingVmsInput(ValidataclassMixin):
    vmsUsedToManageParking: VmsControllerVersionedReferenceGInput = DataclassValidator(
        VmsControllerVersionedReferenceGInput
    )
    vmsOperator: OrganisationGInput | UnsetValueType = DataclassValidator(OrganisationGInput), Default(UnsetValue)
    prkParkingVmsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
