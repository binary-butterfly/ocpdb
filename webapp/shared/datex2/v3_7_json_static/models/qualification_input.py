"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, ListValidator, StringValidator

from .energy_source_enum_g_input import EnergySourceEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .payment_method_input import PaymentMethodInput
from .rate_table_versioned_reference_g_input import RateTableVersionedReferenceGInput
from .user_qualification_input import UserQualificationInput
from .vehicle_characteristics_input import VehicleCharacteristicsInput


@validataclass
class QualificationInput(ValidataclassMixin):
    """
    A singular set of criteria used to test eligibility for use of a rate table.
    """

    withReservation: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    propulsionEnergyType: list[EnergySourceEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(EnergySourceEnumGInput)),
        Default(UnsetValue),
    )
    noFeeToUse: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    withMembership: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    membershipName: list[MultilingualStringInput] | UnsetValueType = (
        ListValidator(DataclassValidator(MultilingualStringInput)),
        Default(UnsetValue),
    )
    memberOfOtherRateTable: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    rateTableMember: list[RateTableVersionedReferenceGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(RateTableVersionedReferenceGInput)),
        Default(UnsetValue),
    )
    activeAssignedRight: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    paymentMethod: list[PaymentMethodInput] | UnsetValueType = (
        ListValidator(DataclassValidator(PaymentMethodInput)),
        Default(UnsetValue),
    )
    vehicleCharacteristics: list[VehicleCharacteristicsInput] | UnsetValueType = (
        ListValidator(DataclassValidator(VehicleCharacteristicsInput)),
        Default(UnsetValue),
    )
    userQualification: list[UserQualificationInput] | UnsetValueType = (
        ListValidator(DataclassValidator(UserQualificationInput)),
        Default(UnsetValue),
    )
    facQualificationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
