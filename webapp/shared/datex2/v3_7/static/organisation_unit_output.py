"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from webapp.shared.datex2.v3_7.shared.extension_type_g_output import ExtensionTypeGOutput
from webapp.shared.datex2.v3_7.shared.location_reference_g_output import LocationReferenceGOutput
from webapp.shared.datex2.v3_7.shared.multilingual_string_output import MultilingualStringOutput
from webapp.shared.datex2.v3_7.shared.operating_hours_g_output import OperatingHoursGOutput

from .contact_information_g_output import ContactInformationGOutput


@dataclass(kw_only=True)
class OrganisationUnitOutput:
    name: MultilingualStringOutput | None = None
    function: list[MultilingualStringOutput] | None = None
    locationReference: LocationReferenceGOutput | None = None
    contactInformation: list[ContactInformationGOutput] | None = None
    operatingHours: OperatingHoursGOutput | None = None
    afacOrganisationUnitExtensionG: ExtensionTypeGOutput | None = None
