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
from .predefined_condition_versioned_reference_g_input import PredefinedConditionVersionedReferenceGInput
from .validity_input import ValidityInput


@validataclass
class PredefinedConditionActivationInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    activationTime: datetime = DateTimeValidator()
    activationVersionTime: datetime = DateTimeValidator()
    controlledZoneReference: ControlledZoneVersionedReferenceGInput = DataclassValidator(
        ControlledZoneVersionedReferenceGInput
    )
    predefinedConditionReference: PredefinedConditionVersionedReferenceGInput = DataclassValidator(
        PredefinedConditionVersionedReferenceGInput
    )
    validity: ValidityInput = DataclassValidator(ValidityInput)
    czActivationStatusExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    czPredefinedConditionActivationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
