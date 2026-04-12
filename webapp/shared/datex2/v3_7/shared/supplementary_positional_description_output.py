"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .carriageway_output import CarriagewayOutput
from .direction_purpose_enum_g_output import DirectionPurposeEnumGOutput
from .geographic_characteristic_enum_g_output import GeographicCharacteristicEnumGOutput
from .infrastructure_descriptor_enum_g_output import InfrastructureDescriptorEnumGOutput
from .multilingual_string_output import MultilingualStringOutput
from .named_area_g_output import NamedAreaGOutput
from .relative_position_on_carriageway_enum_g_output import RelativePositionOnCarriagewayEnumGOutput
from .road_information_g_output import RoadInformationGOutput
from .supplementary_positional_description_extension_type_g_output import (
    SupplementaryPositionalDescriptionExtensionTypeGOutput,
)


@dataclass(kw_only=True)
class SupplementaryPositionalDescriptionOutput:
    directionPurpose: DirectionPurposeEnumGOutput | None = None
    geographicDescriptor: GeographicCharacteristicEnumGOutput | None = None
    infrastructureDescriptor: InfrastructureDescriptorEnumGOutput | None = None
    lengthAffected: float | None = None
    locationDescription: MultilingualStringOutput | None = None
    locationPrecision: int | None = None
    positionOnCarriageway: RelativePositionOnCarriagewayEnumGOutput | None = None
    sequentialRampNumber: int | None = None
    carriageway: list[CarriagewayOutput] | None = None
    namedArea: NamedAreaGOutput | None = None
    roadInformation: list[RoadInformationGOutput] | None = None
    locSupplementaryPositionalDescriptionExtensionG: SupplementaryPositionalDescriptionExtensionTypeGOutput | None = (
        None
    )
