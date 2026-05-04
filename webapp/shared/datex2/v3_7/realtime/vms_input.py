"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, FloatValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.dedicated_usage_enum_g_input import DedicatedUsageEnumGInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.physical_support_enum_g_input import PhysicalSupportEnumGInput
from webapp.shared.datex2.v3_7.shared.url_link_input import UrlLinkInput
from webapp.shared.datex2.v3_7.shared.vms_configuration_input import VmsConfigurationInput
from webapp.shared.datex2.v3_7.shared.vms_type_enum_g_input import VmsTypeEnumGInput

from .location_g_input import LocationGInput
from .managed_logical_location_input import ManagedLogicalLocationInput


@validataclass
class VmsInput(ValidataclassMixin):
    lanternsPresent: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    description: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    owner: MultilingualStringInput | UnsetValueType = DataclassValidator(MultilingualStringInput), Default(UnsetValue)
    physicalSupport: PhysicalSupportEnumGInput | UnsetValueType = (
        DataclassValidator(PhysicalSupportEnumGInput),
        Default(UnsetValue),
    )
    vmsType: VmsTypeEnumGInput | UnsetValueType = DataclassValidator(VmsTypeEnumGInput), Default(UnsetValue)
    vmsTypeCode: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    dynamicallyConfigurable: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    displayHeight: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    displayWidth: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    heightAboveCarriageway: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    dedicatedUsage: DedicatedUsageEnumGInput | UnsetValueType = (
        DataclassValidator(DedicatedUsageEnumGInput),
        Default(UnsetValue),
    )
    vmsConfiguration: VmsConfigurationInput = DataclassValidator(VmsConfigurationInput)
    vmsLocation: LocationGInput | UnsetValueType = DataclassValidator(LocationGInput), Default(UnsetValue)
    managedLogicalLocation: ManagedLogicalLocationInput | UnsetValueType = (
        DataclassValidator(ManagedLogicalLocationInput),
        Default(UnsetValue),
    )
    imageLink: UrlLinkInput | UnsetValueType = DataclassValidator(UrlLinkInput), Default(UnsetValue)
    vmsVmsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
