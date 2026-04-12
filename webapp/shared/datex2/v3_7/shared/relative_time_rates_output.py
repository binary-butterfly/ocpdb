"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass
from datetime import datetime

from .extension_type_g_output import ExtensionTypeGOutput
from .rate_line_output import RateLineOutput


@dataclass(kw_only=True)
class RelativeTimeRatesOutput:
    collectionSequence: int
    applicableCurrency: str | None = None
    minValueCollection: float | None = None
    maxValueCollection: float | None = None
    validStart: datetime | None = None
    validEnd: datetime | None = None
    minTime: str | None = None
    maxTime: str | None = None
    resetTime: str | None = None
    taxIncluded: bool | None = None
    taxRate: float | None = None
    taxValue: float | None = None
    relativeTimes: bool | None = None
    referenceTimeStart: datetime | None = None
    referenceTimeEnd: datetime | None = None
    rateLine: list[RateLineOutput]
    afacRateLineCollectionExtensionG: ExtensionTypeGOutput | None = None
    afacRelativeTimeRatesExtensionG: ExtensionTypeGOutput | None = None
