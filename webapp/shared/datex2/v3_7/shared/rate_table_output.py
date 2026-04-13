"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass
from datetime import datetime

from .eligibility_output import EligibilityOutput
from .extension_type_g_output import ExtensionTypeGOutput
from .multilingual_string_output import MultilingualStringOutput
from .overall_period_output import OverallPeriodOutput
from .payment_output import PaymentOutput
from .rate_availability_type_enum_g_output import RateAvailabilityTypeEnumGOutput
from .rate_line_collection_g_output import RateLineCollectionGOutput
from .rate_table_versioned_reference_g_output import RateTableVersionedReferenceGOutput
from .rate_type_enum_g_output import RateTypeEnumGOutput
from .referenceable_organisation_versioned_reference_g_output import ReferenceableOrganisationVersionedReferenceGOutput


@dataclass(kw_only=True)
class RateTableOutput:
    idG: str
    versionG: str
    applicableCurrency: list[str] | None = None
    lastUpdated: datetime | None = None
    rateTableName: MultilingualStringOutput | None = None
    activeTimes: list[str] | None = None
    availability: RateAvailabilityTypeEnumGOutput | None = None
    rateResponsibleParty: ReferenceableOrganisationVersionedReferenceGOutput | None = None
    rateSupersedeLink: RateTableVersionedReferenceGOutput | None = None
    validation: bool | None = None
    rateType: RateTypeEnumGOutput | None = None
    validityStart: datetime | None = None
    validityEnd: datetime | None = None
    additionalInformation: str | None = None
    payment: PaymentOutput | None = None
    overallPeriod: OverallPeriodOutput | None = None
    rateLineCollection: list[RateLineCollectionGOutput] | None = None
    eligibility: EligibilityOutput | None = None
    afacRatesExtensionG: ExtensionTypeGOutput | None = None
    afacRateTableExtensionG: ExtensionTypeGOutput | None = None
