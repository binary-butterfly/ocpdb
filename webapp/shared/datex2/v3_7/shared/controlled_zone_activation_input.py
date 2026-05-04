"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, DateTimeValidator, StringValidator

from .controlled_zone_versioned_reference_g_input import ControlledZoneVersionedReferenceGInput
from .extension_type_g_input import ExtensionTypeGInput
from .validity_input import ValidityInput


@validataclass
class ControlledZoneActivationInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    activationTime: datetime = DateTimeValidator()
    activationVersionTime: datetime = DateTimeValidator()
    controlledZoneReference: ControlledZoneVersionedReferenceGInput = DataclassValidator(
        ControlledZoneVersionedReferenceGInput
    )
    validity: ValidityInput = DataclassValidator(ValidityInput)
    czActivationStatusExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    czControlledZoneActivationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
