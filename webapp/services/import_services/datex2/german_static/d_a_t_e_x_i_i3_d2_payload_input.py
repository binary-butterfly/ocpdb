"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .payload_publication_g_input import PayloadPublicationGInput


@validataclass
class DATEXII3D2PayloadInput:
    payload: PayloadPublicationGInput | UnsetValueType = (
        DataclassValidator(PayloadPublicationGInput),
        Default(UnsetValue),
    )
