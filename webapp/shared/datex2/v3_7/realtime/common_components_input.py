"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.characteristics_input import CharacteristicsInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.marketing_input import MarketingInput
from webapp.shared.datex2.v3_7.shared.permits_and_prohibitions_input import PermitsAndProhibitionsInput
from webapp.shared.datex2.v3_7.shared.rgb_colour_input import RgbColourInput
from webapp.shared.datex2.v3_7.shared.safety_standard_classification_input import SafetyStandardClassificationInput
from webapp.shared.datex2.v3_7.shared.threshold_configuration_input import ThresholdConfigurationInput

from .additional_characteristics_input import AdditionalCharacteristicsInput
from .operating_pattern_g_input import OperatingPatternGInput
from .parking_route_g_input import ParkingRouteGInput
from .parking_vms_input import ParkingVmsInput


@validataclass
class CommonComponentsInput(ValidataclassMixin):
    rgbColour: list[RgbColourInput] | UnsetValueType = (
        ListValidator(DataclassValidator(RgbColourInput)),
        Default(UnsetValue),
    )
    characteristics: list[CharacteristicsInput] | UnsetValueType = (
        ListValidator(DataclassValidator(CharacteristicsInput)),
        Default(UnsetValue),
    )
    parkingRoute: list[ParkingRouteGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ParkingRouteGInput)),
        Default(UnsetValue),
    )
    marketing: MarketingInput | UnsetValueType = DataclassValidator(MarketingInput), Default(UnsetValue)
    safetyStandardClassification: list[SafetyStandardClassificationInput] | UnsetValueType = (
        ListValidator(DataclassValidator(SafetyStandardClassificationInput)),
        Default(UnsetValue),
    )
    parkingVms: list[ParkingVmsInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ParkingVmsInput)),
        Default(UnsetValue),
    )
    permitsAndProhibitions: list[PermitsAndProhibitionsInput] | UnsetValueType = (
        ListValidator(DataclassValidator(PermitsAndProhibitionsInput)),
        Default(UnsetValue),
    )
    additionalCharacteristics: AdditionalCharacteristicsInput | UnsetValueType = (
        DataclassValidator(AdditionalCharacteristicsInput),
        Default(UnsetValue),
    )
    operatingPattern: list[OperatingPatternGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(OperatingPatternGInput)),
        Default(UnsetValue),
    )
    thresholdConfiguration: ThresholdConfigurationInput | UnsetValueType = (
        DataclassValidator(ThresholdConfigurationInput),
        Default(UnsetValue),
    )
    prkCommonComponentsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
