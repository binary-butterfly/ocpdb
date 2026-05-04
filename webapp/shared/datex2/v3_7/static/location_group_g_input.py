"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from webapp.shared.datex2.v3_7.shared.location_group_by_reference_input import LocationGroupByReferenceInput

from .location_group_by_list_input import LocationGroupByListInput


@validataclass
class LocationGroupGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    locLocationGroupByList: LocationGroupByListInput | UnsetValueType = (
        DataclassValidator(LocationGroupByListInput),
        Default(UnsetValue),
    )
    locLocationGroupByReference: LocationGroupByReferenceInput | UnsetValueType = (
        DataclassValidator(LocationGroupByReferenceInput),
        Default(UnsetValue),
    )
