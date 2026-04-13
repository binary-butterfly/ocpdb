"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .information_delivery_services_enum import InformationDeliveryServicesEnum


@dataclass(kw_only=True)
class InformationDeliveryServicesEnumGOutput:
    value: InformationDeliveryServicesEnum
    extendedValueG: str | None = None
