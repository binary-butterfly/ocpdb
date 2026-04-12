"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .energy_source_enum_g_output import EnergySourceEnumGOutput
from .extension_type_g_output import ExtensionTypeGOutput
from .linked_right_specification_output import LinkedRightSpecificationOutput
from .multilingual_string_output import MultilingualStringOutput
from .payment_output import PaymentOutput
from .rate_table_versioned_reference_g_output import RateTableVersionedReferenceGOutput
from .user_qualification_output import UserQualificationOutput
from .vehicle_characteristics_output import VehicleCharacteristicsOutput


@dataclass(kw_only=True)
class QualificationOutput:
    withReservation: bool | None = None
    propulsionEnergyType: list[EnergySourceEnumGOutput] | None = None
    noFeeToUse: bool | None = None
    withMembership: bool | None = None
    membershipName: list[MultilingualStringOutput] | None = None
    memberOfOtherRateTable: bool | None = None
    rateTableMember: list[RateTableVersionedReferenceGOutput] | None = None
    activeAssignedRight: str | None = None
    payment: list[PaymentOutput] | None = None
    vehicleCharacteristics: list[VehicleCharacteristicsOutput] | None = None
    linkedRightSpecification: LinkedRightSpecificationOutput | None = None
    userQualification: list[UserQualificationOutput] | None = None
    afacQualificationExtensionG: ExtensionTypeGOutput | None = None
