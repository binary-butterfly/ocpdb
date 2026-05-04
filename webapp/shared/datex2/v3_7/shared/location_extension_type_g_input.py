"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .afir_facility_location_input import AfirFacilityLocationInput


@validataclass
class LocationExtensionTypeGInput(ValidataclassMixin):
    AfirFacilityLocation: AfirFacilityLocationInput | UnsetValueType = (
        DataclassValidator(AfirFacilityLocationInput),
        Default(UnsetValue),
    )
