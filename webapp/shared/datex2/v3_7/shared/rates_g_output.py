"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .free_of_charge_output import FreeOfChargeOutput
from .general_rate_information_output import GeneralRateInformationOutput
from .rate_matrix_by_reference_output import RateMatrixByReferenceOutput
from .rate_matrix_output import RateMatrixOutput
from .rate_table_by_reference_output import RateTableByReferenceOutput
from .rate_table_output import RateTableOutput
from .unknown_rates_output import UnknownRatesOutput
from .unspecified_rates_output import UnspecifiedRatesOutput


@dataclass(kw_only=True)
class RatesGOutput:
    """
    Only one of the properties shall be used in an instance.
    """

    afacUnspecifiedRates: UnspecifiedRatesOutput | None = None
    afacGeneralRateInformation: GeneralRateInformationOutput | None = None
    afacRateMatrix: RateMatrixOutput | None = None
    afacRateTableByReference: RateTableByReferenceOutput | None = None
    afacRateTable: RateTableOutput | None = None
    afacFreeOfCharge: FreeOfChargeOutput | None = None
    afacRateMatrixByReference: RateMatrixByReferenceOutput | None = None
    afacUnknownRates: UnknownRatesOutput | None = None
