"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .information_delivery_services_enum import InformationDeliveryServicesEnum


@validataclass
class InformationDeliveryServicesEnumGInput(ValidataclassMixin):
    value: InformationDeliveryServicesEnum = EnumValidator(InformationDeliveryServicesEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
