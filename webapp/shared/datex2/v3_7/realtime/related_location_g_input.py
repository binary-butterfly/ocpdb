"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .point_of_interest_input import PointOfInterestInput
from .public_transport_stop_input import PublicTransportStopInput


@validataclass
class RelatedLocationGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    prkPointOfInterest: PointOfInterestInput | UnsetValueType = (
        DataclassValidator(PointOfInterestInput),
        Default(UnsetValue),
    )
    prkPublicTransportStop: PublicTransportStopInput | UnsetValueType = (
        DataclassValidator(PublicTransportStopInput),
        Default(UnsetValue),
    )
