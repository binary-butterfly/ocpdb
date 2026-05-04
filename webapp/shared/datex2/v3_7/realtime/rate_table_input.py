"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    BooleanValidator,
    DataclassValidator,
    DateTimeValidator,
    ListValidator,
    StringValidator,
)

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.overall_period_input import OverallPeriodInput
from webapp.shared.datex2.v3_7.shared.payment_input import PaymentInput
from webapp.shared.datex2.v3_7.shared.rate_availability_type_enum_g_input import RateAvailabilityTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.rate_line_collection_g_input import RateLineCollectionGInput
from webapp.shared.datex2.v3_7.shared.rate_table_versioned_reference_g_input import RateTableVersionedReferenceGInput
from webapp.shared.datex2.v3_7.shared.rate_type_enum_g_input import RateTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.referenceable_organisation_versioned_reference_g_input import (
    ReferenceableOrganisationVersionedReferenceGInput,
)

from .eligibility_input import EligibilityInput


@validataclass
class RateTableInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    applicableCurrency: list[str] | UnsetValueType = ListValidator(StringValidator()), Default(UnsetValue)
    lastUpdated: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    rateTableName: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    activeTimes: list[str] | UnsetValueType = ListValidator(StringValidator()), Default(UnsetValue)
    availability: RateAvailabilityTypeEnumGInput | UnsetValueType = (
        DataclassValidator(RateAvailabilityTypeEnumGInput),
        Default(UnsetValue),
    )
    rateResponsibleParty: ReferenceableOrganisationVersionedReferenceGInput | UnsetValueType = (
        DataclassValidator(ReferenceableOrganisationVersionedReferenceGInput),
        Default(UnsetValue),
    )
    rateSupersedeLink: RateTableVersionedReferenceGInput | UnsetValueType = (
        DataclassValidator(RateTableVersionedReferenceGInput),
        Default(UnsetValue),
    )
    validation: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    rateType: RateTypeEnumGInput | UnsetValueType = DataclassValidator(RateTypeEnumGInput), Default(UnsetValue)
    validityStart: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    validityEnd: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    additionalInformation: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    payment: PaymentInput | UnsetValueType = DataclassValidator(PaymentInput), Default(UnsetValue)
    overallPeriod: OverallPeriodInput | UnsetValueType = DataclassValidator(OverallPeriodInput), Default(UnsetValue)
    rateLineCollection: list[RateLineCollectionGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(RateLineCollectionGInput)),
        Default(UnsetValue),
    )
    eligibility: EligibilityInput | UnsetValueType = DataclassValidator(EligibilityInput), Default(UnsetValue)
    afacRatesExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    afacRateTableExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
