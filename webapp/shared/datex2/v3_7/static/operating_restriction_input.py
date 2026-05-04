"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.operating_restrictions_enum_g_input import OperatingRestrictionsEnumGInput
from webapp.shared.datex2.v3_7.shared.overall_period_input import OverallPeriodInput

from .related_location_g_input import RelatedLocationGInput


@validataclass
class OperatingRestrictionInput(ValidataclassMixin):
    operatingPatternIndex: int = IntegerValidator()
    context: MultilingualStringInput | UnsetValueType = DataclassValidator(MultilingualStringInput), Default(UnsetValue)
    type: OperatingRestrictionsEnumGInput = DataclassValidator(OperatingRestrictionsEnumGInput)
    relatedLocation: list[RelatedLocationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(RelatedLocationGInput)),
        Default(UnsetValue),
    )
    validity: OverallPeriodInput | UnsetValueType = DataclassValidator(OverallPeriodInput), Default(UnsetValue)
    prkOperatingPatternExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    prkOperatingRestrictionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
