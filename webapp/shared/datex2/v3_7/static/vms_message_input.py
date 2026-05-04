"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    BooleanValidator,
    DataclassValidator,
    DateTimeValidator,
    FloatValidator,
    ListValidator,
    StringValidator,
)

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.image_input import ImageInput
from webapp.shared.datex2.v3_7.shared.message_information_type_enum_g_input import MessageInformationTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.setting_reason_enum_g_input import SettingReasonEnumGInput
from webapp.shared.datex2.v3_7.shared.situation_record_versioned_reference_g_input import (
    SituationRecordVersionedReferenceGInput,
)
from webapp.shared.datex2.v3_7.shared.situation_versioned_reference_g_input import SituationVersionedReferenceGInput

from .vms_message_display_area_index_display_area_settings_g_input import (
    vmsMessageDisplayAreaIndexDisplayAreaSettingsGInput,
)


@validataclass
class VmsMessageInput(ValidataclassMixin):
    associatedTrafficManagementPlan: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    messageSetBy: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    setBySystem: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    reasonForSetting: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    codedReasonForSetting: SettingReasonEnumGInput | UnsetValueType = (
        DataclassValidator(SettingReasonEnumGInput),
        Default(UnsetValue),
    )
    messageInformationType: list[MessageInformationTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(MessageInformationTypeEnumGInput)),
        Default(UnsetValue),
    )
    primarySetting: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    mareNostrumCompliant: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    timeLastSet: datetime = DateTimeValidator()
    requestedBy: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    relatedSituation: list[SituationVersionedReferenceGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(SituationVersionedReferenceGInput)),
        Default(UnsetValue),
    )
    relatedSituationRecord: list[SituationRecordVersionedReferenceGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(SituationRecordVersionedReferenceGInput)),
        Default(UnsetValue),
    )
    distanceFromClosestSituationRecord: float | UnsetValueType = (
        FloatValidator(allow_integers=True),
        Default(UnsetValue),
    )
    sequencingInterval: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    displayAreaSettings: list[vmsMessageDisplayAreaIndexDisplayAreaSettingsGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(vmsMessageDisplayAreaIndexDisplayAreaSettingsGInput)),
        Default(UnsetValue),
    )
    image: ImageInput | UnsetValueType = DataclassValidator(ImageInput), Default(UnsetValue)
    vmsVmsMessageExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
