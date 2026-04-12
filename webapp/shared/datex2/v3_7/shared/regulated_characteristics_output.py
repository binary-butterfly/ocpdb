"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .eu_bodywork_code_enum_g_output import EuBodyworkCodeEnumGOutput
from .eu_bodywork_supplementary_digit_g_output import EuBodyworkSupplementaryDigitGOutput
from .eu_special_purpose_vehicle_enum_g_output import EuSpecialPurposeVehicleEnumGOutput
from .eu_vehicle_category_enum_g_output import EuVehicleCategoryEnumGOutput
from .extension_type_g_output import ExtensionTypeGOutput
from .multilingual_string_output import MultilingualStringOutput


@dataclass(kw_only=True)
class RegulatedCharacteristicsOutput:
    euVehicleCategory: list[EuVehicleCategoryEnumGOutput] | None = None
    euSpecialPurposeVehicle: EuSpecialPurposeVehicleEnumGOutput | None = None
    nationalSpecialPurposeVehicle: MultilingualStringOutput | None = None
    offroadVehicle: bool | None = None
    specialPurposeVehicle: bool | None = None
    euBodyworkCode: EuBodyworkCodeEnumGOutput | None = None
    euBodyworkSupplementaryDigit: EuBodyworkSupplementaryDigitGOutput | None = None
    comxRegulatedCharacteristicsExtensionG: ExtensionTypeGOutput | None = None
