"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .international_identifier_input import InternationalIdentifierInput
from .measurement_site_versioned_reference_g_input import MeasurementSiteVersionedReferenceGInput


@validataclass
class MeasurementSiteReferenceInput(ValidataclassMixin):
    externalPublicationIdentifier: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    measurementSiteReference: MeasurementSiteVersionedReferenceGInput = DataclassValidator(
        MeasurementSiteVersionedReferenceGInput
    )
    externalPublisher: InternationalIdentifierInput | UnsetValueType = (
        DataclassValidator(InternationalIdentifierInput),
        Default(UnsetValue),
    )
    comGlobalReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    fstDeviceReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    fstMeasurementSiteReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
