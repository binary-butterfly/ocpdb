"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from webapp.shared.datex2.v3_7.shared.computation_method_enum_g_output import ComputationMethodEnumGOutput
from webapp.shared.datex2.v3_7.shared.extension_type_g_output import ExtensionTypeGOutput
from webapp.shared.datex2.v3_7.shared.multilingual_string_output import MultilingualStringOutput


@dataclass(kw_only=True)
class DurationValueOutput:
    dataError: bool | None = None
    reasonForDataError: MultilingualStringOutput | None = None
    accuracy: float | None = None
    computationalMethod: ComputationMethodEnumGOutput | None = None
    numberOfIncompleteInputs: int | None = None
    numberOfInputValuesUsed: int | None = None
    smoothingFactor: float | None = None
    standardDeviation: float | None = None
    supplierCalculatedDataQuality: float | None = None
    duration: float
    comDataValueExtensionG: ExtensionTypeGOutput | None = None
    afacDurationValueExtensionG: ExtensionTypeGOutput | None = None
