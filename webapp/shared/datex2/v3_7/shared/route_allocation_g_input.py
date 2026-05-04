"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .basic_allocation_input import BasicAllocationInput
from .detailed_allocation_input import DetailedAllocationInput
from .route_allocation_input import RouteAllocationInput


@validataclass
class RouteAllocationGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    rerRouteAllocation: RouteAllocationInput | UnsetValueType = (
        DataclassValidator(RouteAllocationInput),
        Default(UnsetValue),
    )
    rerDetailedAllocation: DetailedAllocationInput | UnsetValueType = (
        DataclassValidator(DetailedAllocationInput),
        Default(UnsetValue),
    )
    rerBasicAllocation: BasicAllocationInput | UnsetValueType = (
        DataclassValidator(BasicAllocationInput),
        Default(UnsetValue),
    )
