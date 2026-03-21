"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import StringValidator


@validataclass
class VersionedReferenceInput(ValidataclassMixin):
    """
    A reference to an identifiable version managed object where the combination of the identifier and version is unique. It comprises an identifier (e.g. UUID), a version and a string identifying the class of the referenced object.
    """

    idG: str = StringValidator()
    versionG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
