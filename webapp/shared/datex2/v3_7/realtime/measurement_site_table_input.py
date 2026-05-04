"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.international_identifier_input import InternationalIdentifierInput

from .measurement_site_input import MeasurementSiteInput


@validataclass
class MeasurementSiteTableInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    measurementSiteTableIdentification: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    measurementSite: list[MeasurementSiteInput] = ListValidator(DataclassValidator(MeasurementSiteInput))
    informationManager: InternationalIdentifierInput | UnsetValueType = (
        DataclassValidator(InternationalIdentifierInput),
        Default(UnsetValue),
    )
    roaMeasurementSiteTableExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
