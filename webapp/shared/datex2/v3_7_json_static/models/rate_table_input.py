"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, ListValidator, StringValidator

from .energy_pricing_policy_input import EnergyPricingPolicyInput
from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .organisation_versioned_reference_g_input import OrganisationVersionedReferenceGInput
from .overall_period_input import OverallPeriodInput
from .payment_method_input import PaymentMethodInput
from .rate_availability_type_enum_g_input import RateAvailabilityTypeEnumGInput
from .rate_eligibility_input import RateEligibilityInput
from .rate_line_collection_g_input import RateLineCollectionGInput
from .rate_table_versioned_reference_g_input import RateTableVersionedReferenceGInput
from .rate_type_enum_g_input import RateTypeEnumGInput


@validataclass
class RateTableInput(ValidataclassMixin):
    """
    A specific set of rate charges relating to one or more locations and optionally one set of eligibility criteria.
    """

    idG: str = StringValidator()
    versionG: str = StringValidator()
    applicableCurrency: list[str] | UnsetValueType = ListValidator(StringValidator()), Default(UnsetValue)
    lastUpdated: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    rateTableName: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    activeTimes: list[str] | UnsetValueType = ListValidator(StringValidator()), Default(UnsetValue)
    availability: RateAvailabilityTypeEnumGInput | UnsetValueType = (
        DataclassValidator(RateAvailabilityTypeEnumGInput),
        Default(UnsetValue),
    )
    rateResponsibleParty: OrganisationVersionedReferenceGInput | UnsetValueType = (
        DataclassValidator(OrganisationVersionedReferenceGInput),
        Default(UnsetValue),
    )
    rateSupersedeLink: RateTableVersionedReferenceGInput | UnsetValueType = (
        DataclassValidator(RateTableVersionedReferenceGInput),
        Default(UnsetValue),
    )
    validation: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    rateType: RateTypeEnumGInput | UnsetValueType = DataclassValidator(RateTypeEnumGInput), Default(UnsetValue)
    validityStart: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    validityEnd: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    additionalInformation: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    paymentMethod: PaymentMethodInput | UnsetValueType = DataclassValidator(PaymentMethodInput), Default(UnsetValue)
    overallPeriod: OverallPeriodInput | UnsetValueType = DataclassValidator(OverallPeriodInput), Default(UnsetValue)
    energyPricingPolicy: EnergyPricingPolicyInput | UnsetValueType = (
        DataclassValidator(EnergyPricingPolicyInput),
        Default(UnsetValue),
    )
    rateLineCollection: list[RateLineCollectionGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(RateLineCollectionGInput)),
        Default(UnsetValue),
    )
    rateEligibility: RateEligibilityInput | UnsetValueType = (
        DataclassValidator(RateEligibilityInput),
        Default(UnsetValue),
    )
    facRatesExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    facRateTableExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
