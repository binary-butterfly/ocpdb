"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.international_identifier_input import InternationalIdentifierInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.physical_quantity_fault_input import PhysicalQuantityFaultInput
from webapp.shared.datex2.v3_7.shared.source_input import SourceInput

from .basic_data_g_input import BasicDataGInput
from .location_reference_g_input import LocationReferenceGInput


@validataclass
class SinglePhysicalQuantityInput(ValidataclassMixin):
    forecast: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    measurementEquipmentTypeUsed: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    pertinentLocation: LocationReferenceGInput | UnsetValueType = (
        DataclassValidator(LocationReferenceGInput),
        Default(UnsetValue),
    )
    physicalQuantityFault: list[PhysicalQuantityFaultInput] | UnsetValueType = (
        ListValidator(DataclassValidator(PhysicalQuantityFaultInput)),
        Default(UnsetValue),
    )
    source: SourceInput | UnsetValueType = DataclassValidator(SourceInput), Default(UnsetValue)
    informationManagerOverride: InternationalIdentifierInput | UnsetValueType = (
        DataclassValidator(InternationalIdentifierInput),
        Default(UnsetValue),
    )
    basicData: BasicDataGInput | UnsetValueType = DataclassValidator(BasicDataGInput), Default(UnsetValue)
    roaPhysicalQuantityExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    roaSinglePhysicalQuantityExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
