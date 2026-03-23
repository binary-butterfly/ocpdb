"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import ValidataclassMixin, validataclass
from validataclass.validators import StringValidator


@validataclass
class ReferenceInput(ValidataclassMixin):
    """
    A reference to an identifiable managed object where the identifier is unique.  It comprises an identifier (e.g. UUID) and a string identifying the class of the referenced object.
    """

    idG: str = StringValidator()
