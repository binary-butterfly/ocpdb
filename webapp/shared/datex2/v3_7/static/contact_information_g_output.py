"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .contact_information_output import ContactInformationOutput
from .contact_person_output import ContactPersonOutput


@dataclass(kw_only=True)
class ContactInformationGOutput:
    """
    Only one of the properties shall be used in an instance.
    """

    afacContactInformation: ContactInformationOutput | None = None
    afacContactPerson: ContactPersonOutput | None = None
