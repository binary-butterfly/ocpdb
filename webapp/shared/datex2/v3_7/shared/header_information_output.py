"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .confidentiality_value_enum_g_output import ConfidentialityValueEnumGOutput
from .extension_type_g_output import ExtensionTypeGOutput
from .information_delivery_services_enum_g_output import InformationDeliveryServicesEnumGOutput
from .information_status_enum_g_output import InformationStatusEnumGOutput


@dataclass(kw_only=True)
class HeaderInformationOutput:
    confidentiality: ConfidentialityValueEnumGOutput | None = None
    allowedDeliveryChannel: list[InformationDeliveryServicesEnumGOutput] | None = None
    informationStatus: InformationStatusEnumGOutput
    comHeaderInformationExtensionG: ExtensionTypeGOutput | None = None
