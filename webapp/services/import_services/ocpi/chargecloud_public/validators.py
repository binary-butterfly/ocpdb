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

from datetime import datetime

from validataclass.dataclasses import Default, validataclass
from validataclass.validators import (
    AllowEmptyString,
    DataclassValidator,
    IntegerValidator,
    ListValidator,
    Noneable,
    StringValidator,
)

from webapp.services.import_services.ocpi.ocpi_validators import (
    BusinessDetailsInput,
    ConnectorInput,
    DisplayTextInput,
    EvseInput,
    LocationInput,
)


@validataclass
class ChargecloudPublicConnectorInput(ConnectorInput):
    max_voltage: int = IntegerValidator(allow_strings=True)
    max_amperage: int = IntegerValidator(allow_strings=True)
    last_updated: datetime | None = Default(None)

    @staticmethod
    def __pre_validate__(input_data: dict) -> dict:
        # SW Stuttgart uses different names for some fields:
        if 'voltage' in input_data.keys() and 'max_voltage' not in input_data.keys():
            input_data['max_voltage'] = input_data['voltage']
        if 'ampere' in input_data.keys() and 'max_amperage' not in input_data.keys():
            input_data['max_amperage'] = input_data['ampere']
        if 'max_power' in input_data.keys() and 'max_electric_power' not in input_data.keys():
            input_data['max_electric_power'] = input_data['max_power'] * 1000

        return input_data


@validataclass
class ChargecloudPublicEvseInput(EvseInput):
    connectors: list[ChargecloudPublicConnectorInput] = (
        ListValidator(
            DataclassValidator(ChargecloudPublicConnectorInput),
            min_length=1,
        ),
        Default([]),
    )
    last_updated: datetime | None = Default(None)

    @staticmethod
    def __pre_validate__(input_data: dict) -> dict:
        # SW Stuttgart doesn't provide an 'evse_id' value, but the value of their 'id' field can be used instead
        if 'id' in input_data.keys() and 'evse_id' not in input_data.keys():
            input_data['evse_id'] = input_data['id']

        # Chargecloud public often puts too many chars in a floor_level. Sometimes, one can split it up at space.
        if 'floor_level' in input_data.keys() and isinstance(input_data['floor_level'], str):
            if ' ' in input_data['floor_level']:
                input_data['floor_level'] = input_data['floor_level'].split(' ')[-1]
            input_data['floor_level'] = input_data['floor_level'][:4]

        return input_data


@validataclass
class ChargecloudPublicLocationInput(LocationInput):
    evses: list[ChargecloudPublicEvseInput] = (
        ListValidator(DataclassValidator(ChargecloudPublicEvseInput)),
        Default([]),
    )

    directions: list[DisplayTextInput] | None = (
        AllowEmptyString(
            ListValidator(DataclassValidator(DisplayTextInput)),
            default=None,
        ),
        Default(None),
    )
    last_updated: datetime | None = Default(None)

    owner: BusinessDetailsInput | None = Noneable(DataclassValidator(BusinessDetailsInput)), Default(None)

    time_zone: str = StringValidator(max_length=255), Default('Europe/Berlin')

    @staticmethod
    def __pre_validate__(input_data: dict) -> dict:
        # Chargecloud public uses 2-character country codes where the OCPI spec expects length 3
        if 'country' in input_data.keys() and input_data['country'] == 'DE':
            input_data['country'] = 'DEU'

        # Chargecloud public just uses a string for directions instead of wrapping it in a list of DisplayText objects
        if (
            'directions' in input_data.keys()
            and type(input_data['directions']) is str
            and len(input_data['directions']) > 0
        ):
            input_data['directions'] = [
                {
                    'language': 'DE',
                    'text': input_data['directions'],
                }
            ]

        return input_data
