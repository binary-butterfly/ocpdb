"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, ListValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.permit_owner_type_enum_g_input import PermitOwnerTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.permit_subject_to_fee_input import PermitSubjectToFeeInput
from webapp.shared.datex2.v3_7.shared.permit_type_enum_g_input import PermitTypeEnumGInput

from .point_location_g_input import PointLocationGInput


@validataclass
class PermitInformationInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    applicationRequired: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    description: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    locationRelatedPermit: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    maxDurationOfPermit: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    whereToApplyForPermit: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    whereToCallForPermit: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    permitOwnerType: PermitOwnerTypeEnumGInput | UnsetValueType = (
        DataclassValidator(PermitOwnerTypeEnumGInput),
        Default(UnsetValue),
    )
    urlForFurtherInformation: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    howToObtainPermit: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    permitType: PermitTypeEnumGInput = DataclassValidator(PermitTypeEnumGInput)
    disabledParkingPermit: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    minimumTimeToNextEntry: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    permitSubjectToFee: PermitSubjectToFeeInput | UnsetValueType = (
        DataclassValidator(PermitSubjectToFeeInput),
        Default(UnsetValue),
    )
    locationOfRegistrationMachine: list[PointLocationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(PointLocationGInput)),
        Default(UnsetValue),
    )
    troPermitInformationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
