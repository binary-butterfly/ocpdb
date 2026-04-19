"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.validators import DataclassValidator, Noneable, StringValidator

from .extension_type_g_output import ExtensionTypeGOutput


@validataclass
class InternationalIdentifierOutput(ValidataclassMixin):
    country: str = StringValidator(max_length=2)
    nationalIdentifier: str = StringValidator(max_length=1024)
    comInternationalIdentifierExtensionG: ExtensionTypeGOutput | None = (
        Noneable(DataclassValidator(ExtensionTypeGOutput)),
        Default(None),
    )
