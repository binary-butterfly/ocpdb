"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .credential_assigned_output import CredentialAssignedOutput
from .credential_output import CredentialOutput


@dataclass(kw_only=True)
class CredentialGOutput:
    """
    Only one of the properties shall be used in an instance.
    """

    afacCredential: CredentialOutput | None = None
    afacCredentialAssigned: CredentialAssignedOutput | None = None
