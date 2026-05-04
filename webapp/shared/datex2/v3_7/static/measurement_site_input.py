"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    DataclassValidator,
    DateTimeValidator,
    IntegerValidator,
    ListValidator,
    StringValidator,
)

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.international_identifier_input import InternationalIdentifierInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput

from .location_reference_g_input import LocationReferenceGInput
from .measurement_site_index_measurement_specific_characteristics_g_input import (
    measurementSiteIndexMeasurementSpecificCharacteristicsGInput,
)


@validataclass
class MeasurementSiteInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    measurementSiteRecordVersionTime: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    measurementEquipmentReference: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    measurementEquipmentTypeUsed: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    measurementSiteName: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    measurementSiteNumberOfLanes: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    measurementSiteIdentification: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    measurementSpecificCharacteristics: (
        list[measurementSiteIndexMeasurementSpecificCharacteristicsGInput] | UnsetValueType
    ) = (
        ListValidator(DataclassValidator(measurementSiteIndexMeasurementSpecificCharacteristicsGInput)),
        Default(UnsetValue),
    )
    measurementSiteLocation: LocationReferenceGInput = DataclassValidator(LocationReferenceGInput)
    informationManagerOverride: InternationalIdentifierInput | UnsetValueType = (
        DataclassValidator(InternationalIdentifierInput),
        Default(UnsetValue),
    )
    roaMeasurementSiteExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
