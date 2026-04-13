"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .extension_type_g_output import ExtensionTypeGOutput
from .external_referencing_output import ExternalReferencingOutput
from .location_extension_type_g_output import LocationExtensionTypeGOutput
from .point_by_coordinates_output import PointByCoordinatesOutput
from .point_coordinates_output import PointCoordinatesOutput
from .supplementary_positional_description_output import SupplementaryPositionalDescriptionOutput


@dataclass(kw_only=True)
class PointLocationOutput:
    externalReferencing: list[ExternalReferencingOutput] | None = None
    coordinatesForDisplay: PointCoordinatesOutput | None = None
    supplementaryPositionalDescription: SupplementaryPositionalDescriptionOutput | None = None
    pointByCoordinates: PointByCoordinatesOutput | None = None
    locLocationExtensionG: LocationExtensionTypeGOutput | None = None
    locNetworkLocationExtensionG: ExtensionTypeGOutput | None = None
    locPointLocationExtensionG: ExtensionTypeGOutput | None = None
