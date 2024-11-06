"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2024 binary butterfly GmbH

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from validataclass.dataclasses import validataclass, DefaultUnset, Default
from validataclass.helpers import OptionalUnset, UnsetValue
from validataclass.validators import (
    Noneable,
    DataclassValidator,
    ListValidator,
    AllowEmptyString,
    IntegerValidator,
    StringValidator,
)

from webapp.services.import_services.ocpi.ocpi_validators import (
    LocationInput,
    BusinessDetailsInput,
    DisplayTextInput,
    EvseInput,
    ConnectorInput,
)


@validataclass
class SWStuttgartConnectorInput(ConnectorInput):

    max_voltage: int = IntegerValidator(allow_strings=True)
    max_amperage: int = IntegerValidator(allow_strings=True)

    @staticmethod
    def __pre_validate__(input_data: dict) -> dict:

        # SW Stuttgart uses different names for some fields:
        if 'voltage' in input_data.keys() and 'max_voltage' not in input_data.keys():
            input_data['max_voltage'] = input_data['voltage']
        if 'ampere' in input_data.keys() and 'max_amperage' not in input_data.keys():
            input_data['max_amperage'] = input_data['ampere']

        return input_data


@validataclass
class SWStuttgartEvseInput(EvseInput):

    connectors: list[SWStuttgartConnectorInput] = ListValidator(
        DataclassValidator(SWStuttgartConnectorInput),
        min_length=1,
    ), DefaultUnset


    @staticmethod
    def __pre_validate__(input_data: dict) -> dict:

        # SW Stuttgart doesn't provide an 'evse_id' value, but the value of their 'id' field can be used instead
        if 'id' in input_data.keys() and 'evse_id' not in input_data.keys():
            input_data['evse_id'] = input_data['id']

        return input_data



@validataclass
class SWStuttgartLocationInput(LocationInput):

    evses: OptionalUnset[list[SWStuttgartEvseInput]] = ListValidator(DataclassValidator(SWStuttgartEvseInput)), DefaultUnset

    directions: OptionalUnset[list[DisplayTextInput]] = AllowEmptyString(
        ListValidator(DataclassValidator(DisplayTextInput)),
        default=UnsetValue,
    ), DefaultUnset

    owner: OptionalUnset[BusinessDetailsInput] = Noneable(
        DataclassValidator(BusinessDetailsInput),
        default=UnsetValue,
    ), DefaultUnset

    time_zone: str = StringValidator(max_length=255), Default('Europe/Berlin')

    @staticmethod
    def __pre_validate__(input_data: dict) -> dict:

        # SW Stuttgart uses 2-character country codes where the OCPI spec expects length 3
        if 'country' in input_data.keys() and input_data['country'] == 'DE':
            input_data['country'] = 'DEU'

        # SW Stuttgart just uses a string for directions instead of wrapping it in a list of DisplayText objects
        if 'directions' in input_data.keys() \
            and type(input_data['directions']) is str \
            and len(input_data['directions']) > 0:
            input_data['directions'] = [
                {
                    'language': 'DE',
                    'text': input_data['directions'],
                }
            ]

        return input_data
