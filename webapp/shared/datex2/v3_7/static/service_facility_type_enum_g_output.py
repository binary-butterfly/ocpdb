"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .service_facility_type_enum import ServiceFacilityTypeEnum


@dataclass(kw_only=True)
class ServiceFacilityTypeEnumGOutput:
    value: ServiceFacilityTypeEnum
    extendedValueG: str | None = None
