"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2025 binary butterfly GmbH

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

from unittest.mock import ANY

LOCATIONS_1_RESPONSE = {
    'name': 'Test Location',
    'address': 'Test Street 123',
    'postal_code': '12345',
    'city': 'Test City',
    'country': 'DEU',
    'time_zone': 'Europe/Berlin',
    'last_updated': ANY,
    'id': '1',
    'publish': True,
    'opening_times': {'twentyfourseven': True},
    'coordinates': {'latitude': '52.5200300', 'longitude': '13.4048900'},
    'operator': {'name': 'Electro Inc'},
    'evses': [
        {
            'uid': '1',
            'evse_id': 'EVSE-1',
            'status': 'AVAILABLE',
            'last_updated': ANY,
            'connectors': [
                {
                    'standard': 'IEC_62196_T2',
                    'format': 'SOCKET',
                    'power_type': 'AC_3_PHASE',
                    'max_voltage': 400,
                    'max_amperage': 32,
                    'max_electric_power': 22000,
                    'last_updated': ANY,
                    'id': '1',
                },
            ],
        },
        {
            'uid': '2',
            'evse_id': 'EVSE-1',
            'status': 'AVAILABLE',
            'last_updated': ANY,
            'connectors': [
                {
                    'standard': 'IEC_62196_T2',
                    'format': 'SOCKET',
                    'power_type': 'AC_3_PHASE',
                    'max_voltage': 400,
                    'max_amperage': 32,
                    'max_electric_power': 22000,
                    'last_updated': ANY,
                    'id': '2',
                },
            ],
        },
    ],
}

LOCATIONS_2_RESPONSE = {
    'name': 'Test Location',
    'address': 'Test Street 123',
    'postal_code': '12345',
    'city': 'Test City',
    'country': 'DEU',
    'time_zone': 'Europe/Berlin',
    'last_updated': ANY,
    'id': '2',
    'publish': True,
    'opening_times': {'twentyfourseven': True},
    'coordinates': {'latitude': '52.5200300', 'longitude': '13.4048900'},
    'operator': {'name': 'Electro Inc'},
    'evses': [
        {
            'uid': '3',
            'evse_id': 'EVSE-1',
            'status': 'AVAILABLE',
            'last_updated': ANY,
            'connectors': [
                {
                    'standard': 'IEC_62196_T2_COMBO',
                    'format': 'CABLE',
                    'power_type': 'DC',
                    'max_voltage': 400,
                    'max_amperage': 350,
                    'max_electric_power': 150000,
                    'last_updated': ANY,
                    'id': '3',
                },
            ],
        },
        {
            'uid': '4',
            'evse_id': 'EVSE-1',
            'status': 'AVAILABLE',
            'last_updated': ANY,
            'connectors': [
                {
                    'standard': 'IEC_62196_T2_COMBO',
                    'format': 'CABLE',
                    'power_type': 'DC',
                    'max_voltage': 400,
                    'max_amperage': 350,
                    'max_electric_power': 150000,
                    'last_updated': ANY,
                    'id': '4',
                },
            ],
        },
    ],
}


LOCATIONS_3_RESPONSE = {
    'name': 'Test Location',
    'address': 'Test Street 123',
    'postal_code': '12345',
    'city': 'Test City',
    'country': 'DEU',
    'time_zone': 'Europe/Berlin',
    'last_updated': ANY,
    'id': '3',
    'publish': True,
    'opening_times': {'twentyfourseven': True},
    'coordinates': {'latitude': '52.5200300', 'longitude': '13.4048900'},
    'operator': {'name': 'Power Inc'},
    'evses': [
        {
            'uid': '5',
            'evse_id': 'EVSE-1',
            'status': 'AVAILABLE',
            'last_updated': ANY,
            'connectors': [
                {
                    'standard': 'IEC_62196_T2',
                    'format': 'SOCKET',
                    'power_type': 'AC_3_PHASE',
                    'max_voltage': 400,
                    'max_amperage': 32,
                    'max_electric_power': 22000,
                    'last_updated': ANY,
                    'id': '5',
                },
            ],
        },
        {
            'uid': '6',
            'evse_id': 'EVSE-1',
            'status': 'AVAILABLE',
            'last_updated': ANY,
            'connectors': [
                {
                    'standard': 'IEC_62196_T2',
                    'format': 'SOCKET',
                    'power_type': 'AC_3_PHASE',
                    'max_voltage': 400,
                    'max_amperage': 32,
                    'max_electric_power': 22000,
                    'last_updated': ANY,
                    'id': '6',
                },
            ],
        },
    ],
}


LOCATIONS_RESPONSE = {
    'items': [
        LOCATIONS_1_RESPONSE,
        LOCATIONS_2_RESPONSE,
        LOCATIONS_3_RESPONSE,
    ],
    'total_count': 3,
}
