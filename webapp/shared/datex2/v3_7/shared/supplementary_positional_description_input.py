"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator, IntegerValidator, ListValidator

from .carriageway_input import CarriagewayInput
from .direction_purpose_enum_g_input import DirectionPurposeEnumGInput
from .geographic_characteristic_enum_g_input import GeographicCharacteristicEnumGInput
from .infrastructure_descriptor_enum_g_input import InfrastructureDescriptorEnumGInput
from .multilingual_string_input import MultilingualStringInput
from .named_area_g_input import NamedAreaGInput
from .relative_position_on_carriageway_enum_g_input import RelativePositionOnCarriagewayEnumGInput
from .road_information_g_input import RoadInformationGInput
from .supplementary_positional_description_extension_type_g_input import (
    SupplementaryPositionalDescriptionExtensionTypeGInput,
)


@validataclass
class SupplementaryPositionalDescriptionInput(ValidataclassMixin):
    directionPurpose: DirectionPurposeEnumGInput | UnsetValueType = (
        DataclassValidator(DirectionPurposeEnumGInput),
        Default(UnsetValue),
    )
    geographicDescriptor: GeographicCharacteristicEnumGInput | UnsetValueType = (
        DataclassValidator(GeographicCharacteristicEnumGInput),
        Default(UnsetValue),
    )
    infrastructureDescriptor: InfrastructureDescriptorEnumGInput | UnsetValueType = (
        DataclassValidator(InfrastructureDescriptorEnumGInput),
        Default(UnsetValue),
    )
    lengthAffected: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    locationDescription: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    locationPrecision: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    positionOnCarriageway: RelativePositionOnCarriagewayEnumGInput | UnsetValueType = (
        DataclassValidator(RelativePositionOnCarriagewayEnumGInput),
        Default(UnsetValue),
    )
    sequentialRampNumber: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    carriageway: list[CarriagewayInput] | UnsetValueType = (
        ListValidator(DataclassValidator(CarriagewayInput)),
        Default(UnsetValue),
    )
    namedArea: NamedAreaGInput | UnsetValueType = DataclassValidator(NamedAreaGInput), Default(UnsetValue)
    roadInformation: list[RoadInformationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(RoadInformationGInput)),
        Default(UnsetValue),
    )
    locSupplementaryPositionalDescriptionExtensionG: (
        SupplementaryPositionalDescriptionExtensionTypeGInput | UnsetValueType
    ) = DataclassValidator(SupplementaryPositionalDescriptionExtensionTypeGInput), Default(UnsetValue)
