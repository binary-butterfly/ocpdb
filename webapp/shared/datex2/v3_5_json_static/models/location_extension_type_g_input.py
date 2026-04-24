"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from typing import Any

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .facility_location_input import FacilityLocationInput


@validataclass
class LocationExtensionTypeGInput(ValidataclassMixin):
    FacilityLocation: FacilityLocationInput | UnsetValueType = (
        DataclassValidator(FacilityLocationInput),
        Default(UnsetValue),
    )

    @staticmethod
    def __pre_validate__(data: Any) -> Any:
        # Fix common error with 'FacilityLocation'
        if isinstance(data, dict) and 'facilityLocation' in data:
            data['FacilityLocation'] = data['facilityLocation']

        return data
