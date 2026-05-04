"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from webapp.shared.datex2.v3_7.shared.free_of_charge_input import FreeOfChargeInput
from webapp.shared.datex2.v3_7.shared.general_rate_information_input import GeneralRateInformationInput
from webapp.shared.datex2.v3_7.shared.rate_matrix_by_reference_input import RateMatrixByReferenceInput
from webapp.shared.datex2.v3_7.shared.rate_table_by_reference_input import RateTableByReferenceInput
from webapp.shared.datex2.v3_7.shared.unknown_rates_input import UnknownRatesInput
from webapp.shared.datex2.v3_7.shared.unspecified_rates_input import UnspecifiedRatesInput

from .rate_matrix_input import RateMatrixInput
from .rate_table_input import RateTableInput


@validataclass
class RatesGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    afacUnspecifiedRates: UnspecifiedRatesInput | UnsetValueType = (
        DataclassValidator(UnspecifiedRatesInput),
        Default(UnsetValue),
    )
    afacGeneralRateInformation: GeneralRateInformationInput | UnsetValueType = (
        DataclassValidator(GeneralRateInformationInput),
        Default(UnsetValue),
    )
    afacRateMatrix: RateMatrixInput | UnsetValueType = DataclassValidator(RateMatrixInput), Default(UnsetValue)
    afacRateTableByReference: RateTableByReferenceInput | UnsetValueType = (
        DataclassValidator(RateTableByReferenceInput),
        Default(UnsetValue),
    )
    afacRateTable: RateTableInput | UnsetValueType = DataclassValidator(RateTableInput), Default(UnsetValue)
    afacFreeOfCharge: FreeOfChargeInput | UnsetValueType = DataclassValidator(FreeOfChargeInput), Default(UnsetValue)
    afacRateMatrixByReference: RateMatrixByReferenceInput | UnsetValueType = (
        DataclassValidator(RateMatrixByReferenceInput),
        Default(UnsetValue),
    )
    afacUnknownRates: UnknownRatesInput | UnsetValueType = DataclassValidator(UnknownRatesInput), Default(UnsetValue)
