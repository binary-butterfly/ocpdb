"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .free_of_charge_input import FreeOfChargeInput
from .general_rate_information_input import GeneralRateInformationInput
from .rate_table_input import RateTableInput
from .rates_by_reference_input import RatesByReferenceInput
from .unknown_rates_input import UnknownRatesInput
from .unspecified_rates_input import UnspecifiedRatesInput


@validataclass
class RatesGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    facUnknownRates: UnknownRatesInput | UnsetValueType = DataclassValidator(UnknownRatesInput), Default(UnsetValue)
    facGeneralRateInformation: GeneralRateInformationInput | UnsetValueType = (
        DataclassValidator(GeneralRateInformationInput),
        Default(UnsetValue),
    )
    facRatesByReference: RatesByReferenceInput | UnsetValueType = (
        DataclassValidator(RatesByReferenceInput),
        Default(UnsetValue),
    )
    facUnspecifiedRates: UnspecifiedRatesInput | UnsetValueType = (
        DataclassValidator(UnspecifiedRatesInput),
        Default(UnsetValue),
    )
    facRateTable: RateTableInput | UnsetValueType = DataclassValidator(RateTableInput), Default(UnsetValue)
    facFreeOfCharge: FreeOfChargeInput | UnsetValueType = DataclassValidator(FreeOfChargeInput), Default(UnsetValue)
