"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .rate_line_collection_output import RateLineCollectionOutput
from .relative_time_rates_output import RelativeTimeRatesOutput


@dataclass(kw_only=True)
class RateLineCollectionGOutput:
    """
    Only one of the properties shall be used in an instance.
    """

    afacRateLineCollection: RateLineCollectionOutput | None = None
    afacRelativeTimeRates: RelativeTimeRatesOutput | None = None
