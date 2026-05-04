"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, FloatValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.overall_period_input import OverallPeriodInput
from webapp.shared.datex2.v3_7.shared.reservation_type_enum_g_input import ReservationTypeEnumGInput

from .eligibility_input import EligibilityInput


@validataclass
class AssignmentInput(ValidataclassMixin):
    maximumParkingDuration: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    minimumParkingDuration: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    parkingAllowed: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    reservation: ReservationTypeEnumGInput | UnsetValueType = (
        DataclassValidator(ReservationTypeEnumGInput),
        Default(UnsetValue),
    )
    assignmentValidity: OverallPeriodInput | UnsetValueType = (
        DataclassValidator(OverallPeriodInput),
        Default(UnsetValue),
    )
    exclusivelyAssignedFor: EligibilityInput | UnsetValueType = (
        DataclassValidator(EligibilityInput),
        Default(UnsetValue),
    )
    prohibitedFor: EligibilityInput | UnsetValueType = DataclassValidator(EligibilityInput), Default(UnsetValue)
    applicableFor: EligibilityInput | UnsetValueType = DataclassValidator(EligibilityInput), Default(UnsetValue)
    prkAssignmentExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
