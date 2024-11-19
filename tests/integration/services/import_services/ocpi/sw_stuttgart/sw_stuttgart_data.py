# ruff: noqa: Q000 E501

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

sw_stuttgart_response_json = {
  "languages": {
    "de_DE": "German (Germany)",
    "en_GB": "English (United Kingdom)",
    "nl_NL": "Dutch (Netherlands)",
    "pl_PL": "Polski (Polska)",
    "fr_FR": "French (France)"
  },
  "localesLanguageMap": {
    "de_DE": {
      "flag": "de",
      "text": "Deutsch"
    },
    "en_GB": {
      "flag": "gb",
      "text": "English"
    },
    "es_ES": {
      "flag": "es",
      "text": "Español"
    },
    "nl_NL": {
      "flag": "nl",
      "text": "Nederlands"
    },
    "fr_FR": {
      "flag": "fr",
      "text": "Français"
    },
    "it_IT": {
      "flag": "it",
      "text": "Italiano"
    },
    "pl_PL": {
      "flag": "pl",
      "text": "Polski"
    }
  },
  "currentLocale": "de_DE",
  "data": [
    {
      "id": "493558",
      "name": "Affalterstr. 9 LADE / 341-N-01",
      "status": "active",
      "address": "Affalterstr. 9",
      "city": "Stuttgart",
      "postal_code": "70469",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.816269",
        "longitude": "9.171917"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141623",
          "id": "DE*STR*E10001*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797559",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141683",
          "id": "DE*STR*E10001*002",
          "status": "CHARGING",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797619",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493559",
      "name": "Vollmoellerstr. 17 LADE / 715-N-02 ",
      "status": "active",
      "address": "Vollmoellerstr. 17",
      "city": "Stuttgart",
      "postal_code": "70563",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.727399",
        "longitude": "9.108671"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141624",
          "id": "DE*STR*E10002*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797560",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141684",
          "id": "DE*STR*E10002*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797620",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493560",
      "name": "Meluner Str. 3 LADE / 717-N-01",
      "status": "active",
      "address": "Meluner Str. 3",
      "city": "Stuttgart",
      "postal_code": "70569",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.738418",
        "longitude": "9.092729"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141625",
          "id": "DE*STR*E10003*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": " ",
          "roaming": False,
          "connectors": [
            {
              "id": "189797561",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141685",
          "id": "DE*STR*E10003*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": " ",
          "roaming": False,
          "connectors": [
            {
              "id": "189797621",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493561",
      "name": "Solitudestr. 197 LADE / 801-N-04",
      "status": "active",
      "address": "Solitudestr. 197",
      "city": "Stuttgart",
      "postal_code": "70499",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.812430",
        "longitude": "9.110370"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141626",
          "id": "DE*STR*E10004*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797562",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141686",
          "id": "DE*STR*E10004*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797622",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493563",
      "name": "Flamingoweg 33 LADE / 481-N-01 ",
      "status": "active",
      "address": "Flamingoweg  33",
      "city": "Stuttgart",
      "postal_code": "70378",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.830380",
        "longitude": "9.230750"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141628",
          "id": "DE*STR*E10006*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797564",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141688",
          "id": "DE*STR*E10006*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797624",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493564",
      "name": "Revaler Str. 3 LADE / 441-N-01 ",
      "status": "active",
      "address": "Revaler Str. 3",
      "city": "Stuttgart",
      "postal_code": "70378",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.842360",
        "longitude": "9.228291"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141629",
          "id": "DE*STR*E10007*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797565",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141689",
          "id": "DE*STR*E10007*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797625",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493565",
      "name": "Wiederholdstr. 2 LADE / 121-N-02",
      "status": "active",
      "address": "Wiederholdstr. 2",
      "city": "Stuttgart",
      "postal_code": "70174",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.785452",
        "longitude": "9.166607"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141630",
          "id": "DE*STR*E10008*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797566",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141690",
          "id": "DE*STR*E10008*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797626",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493566",
      "name": "Hoffeldstr. 193 LADE / 321-N-01",
      "status": "active",
      "address": "Hoffeldstr. 193",
      "city": "Stuttgart",
      "postal_code": "70597",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.735085",
        "longitude": "9.180107"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141631",
          "id": "DE*STR*E10009*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797567",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141691",
          "id": "DE*STR*E10009*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797627",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493567",
      "name": "Bertramstr. 13 LADE / 662-N-01",
      "status": "active",
      "address": "Bertramstr. 13",
      "city": "Stuttgart",
      "postal_code": "70327",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.790423",
        "longitude": "9.255330"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141632",
          "id": "DE*STR*E10010*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797568",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141692",
          "id": "DE*STR*E10010*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797628",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493568",
      "name": "Filderhauptstr. 36 LADE / 551-N-02",
      "status": "active",
      "address": "Filderhauptstr. 36",
      "city": "Stuttgart",
      "postal_code": "70599",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.701301",
        "longitude": "9.210003"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141633",
          "id": "DE*STR*E10011*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797569",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "16",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141693",
          "id": "DE*STR*E10011*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797629",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493569",
      "name": "Taubenheimstr. 60 LADE / 206-N-01",
      "status": "active",
      "address": "Taubenheimstr. 60",
      "city": "Stuttgart",
      "postal_code": "70372",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.802553",
        "longitude": "9.228851"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141634",
          "id": "DE*STR*E10012*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797570",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141694",
          "id": "DE*STR*E10012*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797630",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493570",
      "name": "Rosentalstr. 4 LADE / 715-N-01",
      "status": "active",
      "address": "Rosentalstr. 4",
      "city": "Stuttgart",
      "postal_code": "70563",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.728598",
        "longitude": "9.102043"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141635",
          "id": "DE*STR*E10013*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797571",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141695",
          "id": "DE*STR*E10013*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797631",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493571",
      "name": "Arlbergstr. 38/1 LADE / 663-N-03",
      "status": "active",
      "address": "Arlbergstr. 38",
      "city": "Stuttgart ",
      "postal_code": "70327",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.780294",
        "longitude": "9.250937"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141636",
          "id": "DE*STR*E10014*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797572",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141696",
          "id": "DE*STR*E10014*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797632",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493572",
      "name": "Hasenbergstr. 54 LADE / 184-N-02",
      "status": "active",
      "address": "Hasenbergstr. 54",
      "city": "Stuttgart",
      "postal_code": "70176",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.774120",
        "longitude": "9.159370"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141637",
          "id": "DE*STR*E10015*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797573",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141697",
          "id": "DE*STR*E10015*002",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797633",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493573",
      "name": "Wilhelmstr. 7 LADE / 110-N-01",
      "status": "active",
      "address": "Wilhelmstr. 7",
      "city": "Stuttgart",
      "postal_code": "70182",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.770651",
        "longitude": "9.179983"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141638",
          "id": "DE*STR*E10016*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797574",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141698",
          "id": "DE*STR*E10016*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797634",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493574",
      "name": "Weilimdorfer Str.  77 LADE / 345-N-02",
      "status": "active",
      "address": "Weilimdorfer Str. 77",
      "city": "Stuttgart",
      "postal_code": "70469",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.812771",
        "longitude": "9.143475"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141699",
          "id": "DE*STR*E10017*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797635",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493575",
      "name": "Steinhaldenstr. 165 LADE / 241-N-01",
      "status": "active",
      "address": "Steinhaldenstr. 165",
      "city": "Stuttgart",
      "postal_code": "70378",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.826981",
        "longitude": "9.231830"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141640",
          "id": "DE*STR*E10018*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797576",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141700",
          "id": "DE*STR*E10018*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797636",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493576",
      "name": "Wagenburgstr. 28 LADE / 142-N-01",
      "status": "active",
      "address": "Wagenburgstr. 28",
      "city": "Stuttgart",
      "postal_code": "70184",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.779343",
        "longitude": "9.195020"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141641",
          "id": "DE*STR*E10019*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797577",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141701",
          "id": "DE*STR*E10019*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797637",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493577",
      "name": "Hornbergstr. 77 LADE / 146-N-01",
      "status": "active",
      "address": "Hornbergstr. 77",
      "city": "Stuttgart",
      "postal_code": "70188",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.783140",
        "longitude": "9.217139"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141642",
          "id": "DE*STR*E10020*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797578",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141702",
          "id": "DE*STR*E10020*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797638",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493578",
      "name": "Stuttgarter Str. 176 LADE / 345-N-03",
      "status": "active",
      "address": "Stuttgarter Str. 176",
      "city": "Stuttgart",
      "postal_code": "70469",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.810309",
        "longitude": "9.150072"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141643",
          "id": "DE*STR*E10021*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797579",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141703",
          "id": "DE*STR*E10021*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797639",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493579",
      "name": "Korianderstraße 35 LADE / 611-N-03",
      "status": "active",
      "address": "Korianderstr. 35",
      "city": "Stuttgart",
      "postal_code": "70619",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.744939",
        "longitude": "9.234658"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141644",
          "id": "DE*STR*E10022*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797580",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141704",
          "id": "DE*STR*E10022*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797640",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493580",
      "name": "Amstetter Str. 26 LADE / 361-N-01",
      "status": "active",
      "address": "Amstetter Str. 26",
      "city": "Stuttgart H",
      "postal_code": "70329",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.757806",
        "longitude": "9.255843"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141645",
          "id": "DE*STR*E10023*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797581",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141705",
          "id": "DE*STR*E10023*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797641",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493581",
      "name": "Ernst-Reuter-Platz 4 LADE / 821-N-02",
      "status": "active",
      "address": "Ernst-Reuter-Platz  4",
      "city": "Stuttgart",
      "postal_code": "70499",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.803328",
        "longitude": "9.092047"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141646",
          "id": "DE*STR*E10024*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797582",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141706",
          "id": "DE*STR*E10024*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797642",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493582",
      "name": "Rosensteinstr. 14 LADE / 129-N-01",
      "status": "active",
      "address": "Rosensteinstr. 14",
      "city": "Stuttgart",
      "postal_code": "70191",
      "country": "DE",
      "directions": "Aufgrund von Bauarbeiten in der Straße wird diese Ladestation vom 27.11 - 15.12.2023 nicht erreichbar sein. ",
      "comment": "",
      "coordinates": {
        "latitude": "48.792876",
        "longitude": "9.190240"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141647",
          "id": "DE*STR*E10025*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797583",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141707",
          "id": "DE*STR*E10025*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797643",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493583",
      "name": "Feuerbacher Weg 123 LADE / 124-N-01",
      "status": "active",
      "address": "Feuerbacher Weg  123",
      "city": "Stuttgart",
      "postal_code": "70192",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.800302",
        "longitude": "9.162312"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141648",
          "id": "DE*STR*E10026*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797584",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141708",
          "id": "DE*STR*E10026*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797644",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493584",
      "name": "König-Karl-Str. 43 LADE / 205-N-01",
      "status": "active",
      "address": "König-Karl-Str. 43",
      "city": "Stuttgart",
      "postal_code": "70372",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.804461",
        "longitude": "9.218079"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141649",
          "id": "DE*STR*E10027*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797585",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141709",
          "id": "DE*STR*E10027*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797645",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493585",
      "name": "Balinger Str. 55 LADE / 401-N-01",
      "status": "active",
      "address": "Balinger Str. 55",
      "city": "Stuttgart",
      "postal_code": "70567",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.732046",
        "longitude": "9.141594"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141650",
          "id": "DE*STR*E10028*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797586",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141710",
          "id": "DE*STR*E10028*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797646",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493586",
      "name": "Giebelstr. 30 LADE / 821-N-01",
      "status": "active",
      "address": "Giebelstr. 30",
      "city": "Stuttgart",
      "postal_code": "70499",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.805824",
        "longitude": "9.089488"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141651",
          "id": "DE*STR*E10029*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797587",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141711",
          "id": "DE*STR*E10029*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797647",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493587",
      "name": "Urachstr. 1 LADE / 145-N-01",
      "status": "active",
      "address": "Urachstr. 1",
      "city": "Stuttgart",
      "postal_code": "70190",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.786188",
        "longitude": "9.197759"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141652",
          "id": "DE*STR*E10030*001",
          "status": "UNKNOWN",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797588",
              "status": "UNKNOWN",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141712",
          "id": "DE*STR*E10030*002",
          "status": "UNKNOWN",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797648",
              "status": "UNKNOWN",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493588",
      "name": "Zeppelinstr. 87 LADE / 181-N-01 ",
      "status": "active",
      "address": "Zeppelinstr. 87",
      "city": "Stuttgart",
      "postal_code": "70193",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.778747",
        "longitude": "9.148019"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141653",
          "id": "DE*STR*E10034*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797589",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141713",
          "id": "DE*STR*E10034*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797649",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493589",
      "name": "Augsburger Straße 581 LADE / 521-N-02",
      "status": "active",
      "address": "Augsburger Straße 581",
      "city": "Stuttgart",
      "postal_code": "70329",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.768106",
        "longitude": "9.264407"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141654",
          "id": "DE*STR*E10032*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797590",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141714",
          "id": "DE*STR*E10032*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797650",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493590",
      "name": "Olgastr. 32 LADE / 101-N-01",
      "status": "active",
      "address": "Olgastr. 32",
      "city": "Stuttgart",
      "postal_code": "70182",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.775006",
        "longitude": "9.185871"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141655",
          "id": "DE*STR*E10033*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797591",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141715",
          "id": "DE*STR*E10033*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797651",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493591",
      "name": "Zeppelinstr. 156 LADE / 181-N-02",
      "status": "active",
      "address": "Zeppelinstr. 156",
      "city": "Stuttgart",
      "postal_code": "70193",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.783753",
        "longitude": "9.147563"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141656",
          "id": "DE*STR*E10031*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797592",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141716",
          "id": "DE*STR*E10031*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797652",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493592",
      "name": "Alexanderstr. 42 LADE / 109-N-01",
      "status": "active",
      "address": "Alexanderstr. 42",
      "city": "Stuttgart",
      "postal_code": "70182",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.773027",
        "longitude": "9.186534"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141657",
          "id": "DE*STR*E10035*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797593",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141717",
          "id": "DE*STR*E10035*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797653",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493593",
      "name": "Nordbahnhofstr. 62 LADE / 126-N-01",
      "status": "active",
      "address": "Nordbahnhofstr. 62",
      "city": "Stuttgart",
      "postal_code": "70191",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.795742",
        "longitude": "9.190102"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141658",
          "id": "DE*STR*E10036*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797594",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141718",
          "id": "DE*STR*E10036*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797654",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493594",
      "name": "Morsestr. 4 LADE / 861-N-01",
      "status": "active",
      "address": "Morsestr. 4",
      "city": "Stuttgart",
      "postal_code": "70435",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.830105",
        "longitude": "9.162097"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141659",
          "id": "DE*STR*E10037*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797595",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141719",
          "id": "DE*STR*E10037*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797655",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493595",
      "name": "Spechtweg 40 LADE / 841-N-01 ",
      "status": "active",
      "address": "Spechtweg  40",
      "city": "Stuttgart",
      "postal_code": "70499",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.803964",
        "longitude": "9.105861"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141660",
          "id": "DE*STR*E10038*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797596",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141720",
          "id": "DE*STR*E10038*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797656",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493596",
      "name": "Ingersheimer Str. 12 LADE / 802-N-02",
      "status": "active",
      "address": "Ingersheimer Str. 12",
      "city": "Stuttgart",
      "postal_code": "70499",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.822193",
        "longitude": "9.094768"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141661",
          "id": "DE*STR*E10039*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797597",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141721",
          "id": "DE*STR*E10039*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797657",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493597",
      "name": "Kaiserslauterer Str. 6 LADE / 801-N-02",
      "status": "active",
      "address": "Kaiserslauterer Str. 6",
      "city": "Stuttgart",
      "postal_code": "70499",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.812845",
        "longitude": "9.119118"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141662",
          "id": "DE*STR*E10040*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797598",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141722",
          "id": "DE*STR*E10040*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797658",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493598",
      "name": "Schönbergstr. 1 LADE / 271-N-01",
      "status": "active",
      "address": "Schönbergstr. 1",
      "city": "Stuttgart",
      "postal_code": "70599",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.732801",
        "longitude": "9.201982"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141663",
          "id": "DE*STR*E10041*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797599",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141723",
          "id": "DE*STR*E10041*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797659",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493599",
      "name": "Steigstr. 1 LADE / 731-N-02",
      "status": "active",
      "address": "Steigstr. 1",
      "city": "Stuttgart",
      "postal_code": "70565",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.718984",
        "longitude": "9.107137"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141664",
          "id": "DE*STR*E10042*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797600",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141724",
          "id": "DE*STR*E10042*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797660",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493601",
      "name": "Schneewittchenweg 31 LADE / 404-N-01",
      "status": "active",
      "address": "Schneewittchenweg  31",
      "city": "Stuttgart",
      "postal_code": "70567",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.722228",
        "longitude": "9.149927"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141666",
          "id": "DE*STR*E10044*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797602",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "16",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141726",
          "id": "DE*STR*E10044*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797662",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "16",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493602",
      "name": "Lambertweg 36 LADE / 741-N-01",
      "status": "active",
      "address": "Lambertweg 36",
      "city": "Stuttgart",
      "postal_code": "70565",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.717040",
        "longitude": "9.122477"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141667",
          "id": "DE*STR*E10045*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797603",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141727",
          "id": "DE*STR*E10045*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797663",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493603",
      "name": "Mendelssohnstr. 92 LADE / 601-N-02",
      "status": "active",
      "address": "Mendelssohnstr. 92",
      "city": "Stuttgart",
      "postal_code": "70619",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.745776",
        "longitude": "9.208535"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141668",
          "id": "DE*STR*E10046*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797604",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141728",
          "id": "DE*STR*E10046*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797664",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493604",
      "name": "Sonatenweg 3 LADE / 642-N-01",
      "status": "active",
      "address": "Sonatenweg  3",
      "city": "Stuttgart",
      "postal_code": "70439",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.848762",
        "longitude": "9.163503"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141669",
          "id": "DE*STR*E10047*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797605",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141729",
          "id": "DE*STR*E10047*002",
          "status": "OUTOFORDER",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797665",
              "status": "OUTOFORDER",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848",
        "10434"
      ]
    },
    {
      "id": "493605",
      "name": "Rotweg 170 LADE / 881-N-01",
      "status": "active",
      "address": "Rotweg 170",
      "city": "Stuttgart",
      "postal_code": "70437",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.835076",
        "longitude": "9.195070"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141670",
          "id": "DE*STR*E10048*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797606",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141730",
          "id": "DE*STR*E10048*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797666",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493606",
      "name": "Gehrenwaldstr. 5 LADE / 661-N-01",
      "status": "active",
      "address": "Gehrenwaldstr. 5",
      "city": "Stuttgart",
      "postal_code": "70327",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.783438",
        "longitude": "9.257355"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141671",
          "id": "DE*STR*E10049*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797607",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141731",
          "id": "DE*STR*E10049*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797667",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493607",
      "name": "Wildensteinstr. 21 LADE / 347-N-01",
      "status": "active",
      "address": "Wildensteinstr. 21",
      "city": "Stuttgart",
      "postal_code": "70469",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.804841",
        "longitude": "9.155713"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141672",
          "id": "DE*STR*E10050*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797608",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141732",
          "id": "DE*STR*E10050*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797668",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493608",
      "name": "Rohrackerstr. 178 LADE / 381-N-02",
      "status": "active",
      "address": "Rohrackerstr. 178",
      "city": "Stuttgart",
      "postal_code": "70329",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.758437",
        "longitude": "9.237790"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141673",
          "id": "DE*STR*E10051*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797609",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141733",
          "id": "DE*STR*E10051*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797669",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493609",
      "name": "Friedrich-Ebert-Str. 39 LADE / 125-N-01",
      "status": "active",
      "address": "Friedrich-Ebert-Str. 39",
      "city": "Stuttgart",
      "postal_code": "70191",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.802166",
        "longitude": "9.181750"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141674",
          "id": "DE*STR*E10052*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797610",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141734",
          "id": "DE*STR*E10052*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797670",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493610",
      "name": "Deidesheimer Str. 46 LADE / 801-N-03",
      "status": "active",
      "address": "Deidesheimer Str. 46",
      "city": "Stuttgart",
      "postal_code": "70499",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.809857",
        "longitude": "9.118144"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141675",
          "id": "DE*STR*E10053*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797611",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141735",
          "id": "DE*STR*E10053*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797671",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493611",
      "name": "Rankestr. 54 LADE / 601-N-01",
      "status": "active",
      "address": "Rankestr. 54",
      "city": "Stuttgart",
      "postal_code": "70619",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.749480",
        "longitude": "9.215419"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141676",
          "id": "DE*STR*E10054*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797612",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141736",
          "id": "DE*STR*E10054*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797672",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493612",
      "name": "Nobileweg 6 LADE / 641-N-01",
      "status": "active",
      "address": "Nobileweg 6",
      "city": "Stuttgart",
      "postal_code": "70439",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.841763",
        "longitude": "9.151181"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141677",
          "id": "DE*STR*E10258*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797613",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141737",
          "id": "DE*STR*E10258*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797673",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848",
        "10434"
      ]
    },
    {
      "id": "493613",
      "name": "Rückertstr. 7 LADE / 181-N-03 ",
      "status": "active",
      "address": "Rückertstr. 7",
      "city": "Stuttgart",
      "postal_code": "70197",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.774160",
        "longitude": "9.145965"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141678",
          "id": "DE*STR*E10056*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797614",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141738",
          "id": "DE*STR*E10056*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797674",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493614",
      "name": "Johannesstr. 53 LADE / 183-N-01",
      "status": "active",
      "address": "Johannesstr. 53",
      "city": "Stuttgart",
      "postal_code": "70176",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.778790",
        "longitude": "9.160436"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141679",
          "id": "DE*STR*E10057*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797615",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141739",
          "id": "DE*STR*E10057*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797675",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493615",
      "name": "Supperstr. 28 LADE / 731-N-01",
      "status": "active",
      "address": "Supperstr. 28",
      "city": "Stuttgart",
      "postal_code": "70565",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.718730",
        "longitude": "9.098482"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141680",
          "id": "DE*STR*E10058*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797616",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141740",
          "id": "DE*STR*E10058*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797676",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493616",
      "name": "Helfferichstr. 5 LADE / 130-N-01",
      "status": "active",
      "address": "Helfferichstr. 5",
      "city": "Stuttgart",
      "postal_code": "70192",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.790100",
        "longitude": "9.170601"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141681",
          "id": "DE*STR*E10059*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797617",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141741",
          "id": "DE*STR*E10059*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797677",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "493617",
      "name": "Hackstr. 33 LADE / 143-N-01",
      "status": "active",
      "address": "Hackstr. 33",
      "city": "Stuttgart",
      "postal_code": "70190",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.789323",
        "longitude": "9.201694"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1141682",
          "id": "DE*STR*E10060*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797618",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1141742",
          "id": "DE*STR*E10060*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "189797678",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "495215",
      "name": "Auf der Altenburg 13/1 LADE / 213-N-01",
      "status": "active",
      "address": "Auf der Altenburg  13/1",
      "city": "Stuttgart",
      "postal_code": "70376",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.810499",
        "longitude": "9.208057"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1145331",
          "id": "DE*STR*E10061*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "190697563",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1518052",
          "id": "DE*STR*E10061*002",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "216477876",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "586173",
      "name": "Ferdinand-Hanauer-Str. 10 LADE / 201-N-01",
      "status": "active",
      "address": "Ferdinand-Hanauer-Str.  10",
      "city": "Stuttgart",
      "postal_code": "70374",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.818409",
        "longitude": "9.234548"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "1500255",
          "id": "DE*STR*E10062*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "215438242",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "1500256",
          "id": "DE*STR*E10062*002",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "215438244",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "736048",
      "name": "Beim Fasanengarten 46/1 LADE / 831-N-01",
      "status": "active",
      "address": "Beim Fasanengarten 46/1",
      "city": "Stuttgart",
      "postal_code": "70499",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.817190",
        "longitude": "9.089610"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2019794",
          "id": "DE*STR*E10063*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478736",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2019795",
          "id": "DE*STR*E10063*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478737",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "736049",
      "name": "Hausenring 86 LADE / 831-N-02",
      "status": "active",
      "address": "Hausenring 86",
      "city": "Stuttgart",
      "postal_code": "70499",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.816030",
        "longitude": "9.084810"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2019796",
          "id": "DE*STR*E10064*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478738",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2019797",
          "id": "DE*STR*E10064*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478739",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "736050",
      "name": "Kahlhieb 23 LADE / 841-N-02",
      "status": "active",
      "address": "Kahlhieb 23",
      "city": "Stuttgart",
      "postal_code": "70499",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.803640",
        "longitude": "9.111690"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2019798",
          "id": "DE*STR*E10065*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478740",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2019799",
          "id": "DE*STR*E10065*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478741",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "736051",
      "name": "Kimmichstraße 8 LADE / 801-N-06",
      "status": "active",
      "address": "Kimmichstr. 8",
      "city": "Stuttgart",
      "postal_code": "70499",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.816350",
        "longitude": "9.112200"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2019800",
          "id": "DE*STR*E10066*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478742",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2019801",
          "id": "DE*STR*E10066*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478743",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "736052",
      "name": "Krokodilweg 27 LADE / 811-N-02",
      "status": "active",
      "address": "Krokodilweg 27",
      "city": "Stuttgart",
      "postal_code": "70499",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.802000",
        "longitude": "9.089890"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2019802",
          "id": "DE*STR*E10067*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478744",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2019803",
          "id": "DE*STR*E10067*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478745",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "736053",
      "name": "Krötenweg 32 LADE / 821-N-03",
      "status": "active",
      "address": "Krötenweg 32",
      "city": "Stuttgart",
      "postal_code": "70499",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.803790",
        "longitude": "9.087930"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2019804",
          "id": "DE*STR*E10068*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478746",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2019805",
          "id": "DE*STR*E10068*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478747",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "736054",
      "name": "Maierwaldstraße 13 LADE / 801-N-05",
      "status": "active",
      "address": "Maierwaldstr. 13",
      "city": "Stuttgart",
      "postal_code": "70499",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.817870",
        "longitude": "9.121040"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2019806",
          "id": "DE*STR*E10069*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478748",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2019807",
          "id": "DE*STR*E10069*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478749",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "736055",
      "name": "Pforzheimer Straße 371A LADE / 801-N-07",
      "status": "active",
      "address": "Pforzheimer Str. 371A",
      "city": "Stuttgart",
      "postal_code": "70499",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.813770",
        "longitude": "9.114090"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2019808",
          "id": "DE*STR*E10070*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478750",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2019809",
          "id": "DE*STR*E10070*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478751",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "736056",
      "name": "Solitudestraße 68 LADE / 811-N-01",
      "status": "active",
      "address": "Solitudestr. 68",
      "city": "Stuttgart",
      "postal_code": "70499",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.803910",
        "longitude": "9.101820"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2019810",
          "id": "DE*STR*E10071*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478752",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2019811",
          "id": "DE*STR*E10071*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478753",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "736057",
      "name": "Fleckenweinberg 27/1 LADE / 348-N-01",
      "status": "active",
      "address": "Fleckenweinberg 27/1",
      "city": "Stuttgart",
      "postal_code": "70192",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.802570",
        "longitude": "9.162500"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2019812",
          "id": "DE*STR*E10072*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478754",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2019813",
          "id": "DE*STR*E10072*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478755",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "736058",
      "name": "Im Gaizen 40 LADE / 345-N-04",
      "status": "active",
      "address": "Im Gaizen 40",
      "city": "Stuttgart",
      "postal_code": "70469",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.817730",
        "longitude": "9.156730"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2019814",
          "id": "DE*STR*E10073*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478756",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2019815",
          "id": "DE*STR*E10073*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478757",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "736061",
      "name": "Linzer Straße 82A LADE / 345-N-05",
      "status": "active",
      "address": "Linzer Str: 82A",
      "city": "Stuttgart",
      "postal_code": "70469",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.815110",
        "longitude": "9.153710"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2019820",
          "id": "DE*STR*E10076*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478762",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2019821",
          "id": "DE*STR*E10076*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478763",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "736063",
      "name": "Siegelbergstraße 50 LADE / 342-N-05",
      "status": "active",
      "address": "Siegelbergstr. 50",
      "city": "Stuttgart",
      "postal_code": "70469",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.821770",
        "longitude": "9.165280"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2019824",
          "id": "DE*STR*E10078*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478766",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2019825",
          "id": "DE*STR*E10078*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478767",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "736064",
      "name": "Stuttgarter Straße 107 LADE / 344-N-05 ",
      "status": "active",
      "address": "Stuttgarter Str. 107",
      "city": "Stuttgart",
      "postal_code": "70469",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.808870",
        "longitude": "9.155780"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2019826",
          "id": "DE*STR*E10079*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478768",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2019827",
          "id": "DE*STR*E10079*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478769",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "736065",
      "name": "Triebweg 95 LADE / 346-N-02",
      "status": "active",
      "address": "Triebweg 95",
      "city": "Stuttgart",
      "postal_code": "70469",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.808020",
        "longitude": "9.140190"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2019828",
          "id": "DE*STR*E10080*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478770",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2019829",
          "id": "DE*STR*E10080*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478771",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "736066",
      "name": "Triebweg 95 LADE / 346-N-03",
      "status": "active",
      "address": "Triebweg 95",
      "city": "Stuttgart",
      "postal_code": "70469",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.808020",
        "longitude": "9.140190"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2019830",
          "id": "DE*STR*E10081*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478772",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2019831",
          "id": "DE*STR*E10081*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "238478773",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "750408",
      "name": "Achardweg 9 LADE / 861-N-02",
      "status": "active",
      "address": "Achardweg 9",
      "city": "Stuttgart",
      "postal_code": "70435",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.831333",
        "longitude": "9.158252"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084477",
          "id": "DE*STR*E10084*001",
          "status": "OUTOFORDER",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116808",
              "status": "OUTOFORDER",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084478",
          "id": "DE*STR*E10084*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116807",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "750409",
      "name": "Adalbert-Stifter-Straße 50 LADE / 451-N-03",
      "status": "active",
      "address": "Adalbert-Stifter-Str. 50",
      "city": "Stuttgart",
      "postal_code": "70437",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.838206",
        "longitude": "9.208116"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084479",
          "id": "DE*STR*E10085*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116806",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084480",
          "id": "DE*STR*E10085*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116805",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751342",
      "name": "Hospitalstr. 21b LADE / 103-N-08",
      "status": "active",
      "address": "Hospitalstr. 21B",
      "city": "Stuttgart",
      "postal_code": "70174",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.776802",
        "longitude": "9.172061"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084483",
          "id": "DE*STR*E10087*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116802",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084484",
          "id": "DE*STR*E10087*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116801",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751343",
      "name": "Altenbergstraße 3 LADE / 162-N-08",
      "status": "active",
      "address": "Altenbergstr. 3",
      "city": "Stuttgart",
      "postal_code": "70180",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.764160",
        "longitude": "9.177620"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084485",
          "id": "DE*STR*E10088*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116800",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084486",
          "id": "DE*STR*E10088*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116799",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751344",
      "name": "Feuerbacher Heide 60 LADE / 123-N-01",
      "status": "active",
      "address": "Feuerbacher Heide 60",
      "city": "Stuttgart",
      "postal_code": "70192",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.791384",
        "longitude": "9.156738"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084487",
          "id": "DE*STR*E10089*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116798",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084488",
          "id": "DE*STR*E10089*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116797",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751346",
      "name": "Am Schattwald 59 LADE / 721-N-02",
      "status": "active",
      "address": "Am Schattwald 59",
      "city": "Stuttgart",
      "postal_code": "70569",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.750550",
        "longitude": "9.077360"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084491",
          "id": "DE*STR*E10091*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116794",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084492",
          "id": "DE*STR*E10091*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116793",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751347",
      "name": "Obere Heckenstr. 5 LADE / 361-N-04",
      "status": "active",
      "address": "Obere Heckenstr. 5",
      "city": "Stuttgart",
      "postal_code": "70329",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.755650",
        "longitude": "9.253491"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084493",
          "id": "DE*STR*E10092*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116792",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084494",
          "id": "DE*STR*E10092*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116791",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751348",
      "name": "Arnoldstraße 87 LADE / 441-N-04",
      "status": "active",
      "address": "Arnoldstr. 87",
      "city": "Stuttgart",
      "postal_code": "70378",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.840074",
        "longitude": "9.222008"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084495",
          "id": "DE*STR*E10093*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116790",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084496",
          "id": "DE*STR*E10093*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116789",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751349",
      "name": "Augsburger Straße 187 LADE / 663-N-04",
      "status": "active",
      "address": "Augsburger Str. 187",
      "city": "Stuttgart",
      "postal_code": "70327",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.794210",
        "longitude": "9.242070"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084497",
          "id": "DE*STR*E10094*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116788",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084498",
          "id": "DE*STR*E10094*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116787",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751350",
      "name": "Augsburger Straße 656 LADE / 521-N-03",
      "status": "active",
      "address": "Augsburger Str. 656",
      "city": "Stuttgart",
      "postal_code": "70329",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.764270",
        "longitude": "9.267730"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084499",
          "id": "DE*STR*E10095*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116786",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084500",
          "id": "DE*STR*E10095*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116785",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751351",
      "name": "Darmstädter Str. 2 LADE / 215-N-01",
      "status": "active",
      "address": "Darmstädter Str. 2",
      "city": "Stuttgart",
      "postal_code": "70376",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.811976",
        "longitude": "9.200131"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084501",
          "id": "DE*STR*E10246*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116784",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084502",
          "id": "DE*STR*E10246*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116783",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751352",
      "name": "Augustenstraße 22 LADE / 184-N-07",
      "status": "active",
      "address": "Augustenstr. 22",
      "city": "Stuttgart",
      "postal_code": "70178",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.772180",
        "longitude": "9.167350"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084503",
          "id": "DE*STR*E10097*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116782",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084504",
          "id": "DE*STR*E10097*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116781",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751353",
      "name": "Badstraße 46/1 LADE / 205-N-04",
      "status": "active",
      "address": "Badstr. 46/1",
      "city": "Stuttgart",
      "postal_code": "70372",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.805060",
        "longitude": "9.212420"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084505",
          "id": "DE*STR*E10098*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116780",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084506",
          "id": "DE*STR*E10098*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116779",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751354",
      "name": "Beethovenstraße 12/1 LADE / 293-N-02",
      "status": "active",
      "address": "Beethovenstr. 12/1",
      "city": "Stuttgart",
      "postal_code": "70195",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.776800",
        "longitude": "9.132360"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084507",
          "id": "DE*STR*E10099*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116778",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084508",
          "id": "DE*STR*E10099*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116777",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751355",
      "name": "Müllerstr. 2 LADE / 165-N-04",
      "status": "active",
      "address": "Müllerstr. 2",
      "city": "Stuttgart",
      "postal_code": "70199",
      "country": "DE",
      "directions": "Müllerstraße/ Ecke Böblinger Str 181 A",
      "comment": "",
      "coordinates": {
        "latitude": "48.758836",
        "longitude": "9.150431"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084509",
          "id": "DE*STR*E10221*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116776",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084510",
          "id": "DE*STR*E10221*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116775",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751356",
      "name": "Bernsteinstraße 120 LADE / 611-N-06",
      "status": "active",
      "address": "Bernsteinstr. 120",
      "city": "Stuttgart",
      "postal_code": "70619",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.736450",
        "longitude": "9.226930"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084511",
          "id": "DE*STR*E10151*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116774",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084512",
          "id": "DE*STR*E10151*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116773",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751357",
      "name": "Birkenwaldstraße 214 LADE / 130-N-02",
      "status": "active",
      "address": "Birkenwaldstr. 214",
      "city": "Stuttgart",
      "postal_code": "70191",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.798550",
        "longitude": "9.175700"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084513",
          "id": "DE*STR*E10157*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116772",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084514",
          "id": "DE*STR*E10157*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116771",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751358",
      "name": "Bismarckstraße 42 LADE / 186-N-04",
      "status": "active",
      "address": "Bismarckstr. 42",
      "city": "Stuttgart",
      "postal_code": "70197",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.772310",
        "longitude": "9.152760"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084515",
          "id": "DE*STR*E10227*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116770",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084516",
          "id": "DE*STR*E10227*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116769",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751359",
      "name": "Böblinger Straße 203 LADE / 166-N-02",
      "status": "active",
      "address": "Böblinger Str. 203",
      "city": "Stuttgart",
      "postal_code": "70199",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.757480",
        "longitude": "9.148010"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084517",
          "id": "DE*STR*E10181*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116768",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084518",
          "id": "DE*STR*E10181*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116767",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751360",
      "name": "Burgstr. 4 LADE / 171-N-02",
      "status": "active",
      "address": "Burgstr.  4",
      "city": "Stuttgart",
      "postal_code": "70569",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.739789",
        "longitude": "9.130650"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084519",
          "id": "DE*STR*E10247*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116766",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084520",
          "id": "DE*STR*E10247*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116765",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751361",
      "name": "Bockelstraße 119 LADE / 611-N-05",
      "status": "active",
      "address": "Bockelstr. 119",
      "city": "Stuttgart",
      "postal_code": "70619",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.742020",
        "longitude": "9.228980"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084521",
          "id": "DE*STR*E10055*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116764",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084522",
          "id": "DE*STR*E10055*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116763",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751362",
      "name": "Bonhoefferweg 2 LADE / 411-N-04",
      "status": "active",
      "address": "Bonhoefferweg 2",
      "city": "Stuttgart",
      "postal_code": "70565",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.711100",
        "longitude": "9.153200"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084523",
          "id": "DE*STR*E10107*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116762",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084524",
          "id": "DE*STR*E10107*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116761",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751364",
      "name": "Breitscheidstraße 36 LADE / 183-N-04",
      "status": "active",
      "address": "Breitscheidstr. 36",
      "city": "Stuttgart",
      "postal_code": "70176",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.777473",
        "longitude": "9.164311"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084527",
          "id": "DE*STR*E10109*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116758",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084528",
          "id": "DE*STR*E10109*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116757",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751365",
      "name": "In der Au 15 LADE / 665-N-02",
      "status": "active",
      "address": "In der Au 15",
      "city": "Stuttgart",
      "postal_code": "70327",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.776585",
        "longitude": "9.250079"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084529",
          "id": "DE*STR*E10110*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116756",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084530",
          "id": "DE*STR*E10110*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116755",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751366",
      "name": "Straßburgerstr. 45 LADE / 866-N-02",
      "status": "active",
      "address": "Straßburgerstr. 45",
      "city": "Stuttgart",
      "postal_code": "70435",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.831220",
        "longitude": "9.167410"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084531",
          "id": "DE*STR*E10111*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116754",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084532",
          "id": "DE*STR*E10111*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116753",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751367",
      "name": "Dachswaldweg 74 LADE / 718-N-03",
      "status": "active",
      "address": "Dachswaldweg 74",
      "city": "Stuttgart",
      "postal_code": "70569",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.744640",
        "longitude": "9.116400"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084533",
          "id": "DE*STR*E10112*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116752",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084534",
          "id": "DE*STR*E10112*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116751",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751368",
      "name": "Dattelweg 17 LADE / 621-N-04",
      "status": "active",
      "address": "Dattelweg 17",
      "city": "Stuttgart",
      "postal_code": "70619",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.738810",
        "longitude": "9.211090"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084535",
          "id": "DE*STR*E10113*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116750",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084536",
          "id": "DE*STR*E10113*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116749",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751369",
      "name": "Delpweg 14/1 LADE / 411-N-01",
      "status": "active",
      "address": "Delpweg 14/1",
      "city": "Stuttgart",
      "postal_code": "70565",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.712570",
        "longitude": "9.156471"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084537",
          "id": "DE*STR*E10114*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116748",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084538",
          "id": "DE*STR*E10114*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116747",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751370",
      "name": "Drackensteinstraße 12 LADE / 146-N-06",
      "status": "active",
      "address": "Drackensteinstr. 12",
      "city": "Stuttgart",
      "postal_code": "70186",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.780470",
        "longitude": "9.218710"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084539",
          "id": "DE*STR*E10115*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116746",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084540",
          "id": "DE*STR*E10115*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116745",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751371",
      "name": "Dreysestraße 19 LADE / 861-N-03",
      "status": "active",
      "address": "Dreysestr. 19",
      "city": "Stuttgart",
      "postal_code": "70435",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.830370",
        "longitude": "9.158930"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084541",
          "id": "DE*STR*E10116*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116744",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084542",
          "id": "DE*STR*E10116*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116743",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751372",
      "name": "Elbestraße 160 LADE / 501-N-03",
      "status": "active",
      "address": "Elbestr. 160",
      "city": "Stuttgart",
      "postal_code": "70376",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.825050",
        "longitude": "9.212590"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084543",
          "id": "DE*STR*E10117*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116742",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084544",
          "id": "DE*STR*E10117*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116741",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751373",
      "name": "Erikastraße 2 LADE / 671-N-02",
      "status": "active",
      "address": "Erikastr. 2",
      "city": "Stuttgart",
      "postal_code": "70327",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.793510",
        "longitude": "9.258100"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084545",
          "id": "DE*STR*E10118*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116740",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084546",
          "id": "DE*STR*E10118*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116739",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751374",
      "name": "Eugenstraße 16 LADE / 108-N-01",
      "status": "active",
      "address": "Eugenstr. 16",
      "city": "Stuttgart",
      "postal_code": "70182",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.778700",
        "longitude": "9.187790"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084547",
          "id": "DE*STR*E10119*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116738",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084548",
          "id": "DE*STR*E10119*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116737",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751375",
      "name": "Falbenhennenstr. 3 LADE / 162-N-06",
      "status": "active",
      "address": "Falbenhennenstr. 3",
      "city": "Stuttgart",
      "postal_code": "70180",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.766770",
        "longitude": "9.176090"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084549",
          "id": "DE*STR*E10120*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116736",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084550",
          "id": "DE*STR*E10120*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116735",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751376",
      "name": "Falchstraße 8 LADE / 241-N-02",
      "status": "active",
      "address": "Falchstr. 8",
      "city": "Stuttgart",
      "postal_code": "70378",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.826230",
        "longitude": "9.235290"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084551",
          "id": "DE*STR*E10121*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116734",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084552",
          "id": "DE*STR*E10121*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116733",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751377",
      "name": "Farrenstraße 50 LADE / 147-N-07",
      "status": "active",
      "address": "Farrenstr. 50",
      "city": "Stuttgart",
      "postal_code": "70186",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.771170",
        "longitude": "9.199250"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084553",
          "id": "DE*STR*E10122*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116732",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084554",
          "id": "DE*STR*E10122*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116731",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751379",
      "name": "Fellbacher Str. 132 LADE / 671-N-01",
      "status": "active",
      "address": "Fellbacher Str 132",
      "city": "Stuttgart",
      "postal_code": "70327",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.791530",
        "longitude": "9.260509"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084557",
          "id": "DE*STR*E10124*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116728",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084558",
          "id": "DE*STR*E10124*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116727",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751381",
      "name": "Filderstraße 25 LADE / 162-N-05",
      "status": "active",
      "address": "Filderstraße 25",
      "city": "Stuttgart",
      "postal_code": "70180",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.764410",
        "longitude": "9.173690"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084561",
          "id": "DE*STR*E10126*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116724",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084562",
          "id": "DE*STR*E10126*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116723",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751382",
      "name": "Flamingoweg 1 LADE / 481-N-05",
      "status": "active",
      "address": "Flamingoweg 1",
      "city": "Stuttgart",
      "postal_code": "70378",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.830420",
        "longitude": "9.231870"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084563",
          "id": "DE*STR*E10127*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116722",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084564",
          "id": "DE*STR*E10127*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116721",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751383",
      "name": "Föhrstraße 7 LADE / 871-N-01",
      "status": "active",
      "address": "Föhrstr. 7",
      "city": "Stuttgart",
      "postal_code": "70439",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.836390",
        "longitude": "9.142050"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084565",
          "id": "DE*STR*E10128*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116720",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084566",
          "id": "DE*STR*E10128*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116719",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751384",
      "name": "Forststraße 179/1 LADE / 186-N-05",
      "status": "active",
      "address": "Forststr. 179/1",
      "city": "Stuttgart",
      "postal_code": "70193",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.775530",
        "longitude": "9.148080"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084567",
          "id": "DE*STR*E10129*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116718",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084568",
          "id": "DE*STR*E10129*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116717",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751385",
      "name": "Franz-Wachter-Straße 18 LADE / 146-N-04",
      "status": "active",
      "address": "Franz-Wachter-Str. 18",
      "city": "Stuttgart",
      "postal_code": "70188",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.783810",
        "longitude": "9.222380"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084569",
          "id": "DE*STR*E10130*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116716",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084570",
          "id": "DE*STR*E10130*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116715",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751386",
      "name": "Eselweg (Frauenkopfstraße 63) LADE / 151-N-01",
      "status": "active",
      "address": "Eselweg ggü. 5",
      "city": "Stuttgart",
      "postal_code": "70184",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.761085",
        "longitude": "9.219441"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084571",
          "id": "DE*STR*E10131*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116714",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084572",
          "id": "DE*STR*E10131*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116713",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751387",
      "name": "Freihofstraße 23 LADE / 642-N-04",
      "status": "active",
      "address": "Freihofstr. 23",
      "city": "Stuttgart",
      "postal_code": "70439",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.847650",
        "longitude": "9.156340"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084573",
          "id": "DE*STR*E10132*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116712",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084574",
          "id": "DE*STR*E10132*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116711",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848",
        "10434"
      ]
    },
    {
      "id": "751388",
      "name": "Fritz-Ulrich-Weg 1 LADE / 406-N-03",
      "status": "active",
      "address": "Fritz-Ulrich-Weg 1",
      "city": "Stuttgart",
      "postal_code": "70567",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.719408",
        "longitude": "9.164896"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084575",
          "id": "DE*STR*E10133*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116710",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084576",
          "id": "DE*STR*E10133*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116709",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751389",
      "name": "Haldenrainstr. ggü. 31 LADE 881-N-08 (1. LS)",
      "status": "active",
      "address": "Haldenrainstr. 31",
      "city": "Stuttgart",
      "postal_code": "70437",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.829835",
        "longitude": "9.180109"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084577",
          "id": "DE*STR*E10134*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116708",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084578",
          "id": "DE*STR*E10134*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116707",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751390",
      "name": "Gablenberger Weg 24 LADE / 147-N-04",
      "status": "active",
      "address": "Gablenberger Weg 24",
      "city": "Stuttgart",
      "postal_code": "70186",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.770320",
        "longitude": "9.201660"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084579",
          "id": "DE*STR*E10135*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116706",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084580",
          "id": "DE*STR*E10135*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116705",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751391",
      "name": "Gänsheidestraße 62 LADE / 141-N-02",
      "status": "active",
      "address": "Gänsheidestr. 62",
      "city": "Stuttgart",
      "postal_code": "70184",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.771440",
        "longitude": "9.194990"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084581",
          "id": "DE*STR*E10136*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116704",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084582",
          "id": "DE*STR*E10136*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116703",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751393",
      "name": "Graugansstraße 32 LADE / 481-N-04",
      "status": "active",
      "address": "Graugansstr. 32",
      "city": "Stuttgart",
      "postal_code": "70378",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.832780",
        "longitude": "9.240480"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084585",
          "id": "DE*STR*E10138*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116700",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084586",
          "id": "DE*STR*E10138*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116699",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751394",
      "name": "Haldenrainstraße 184 LADE / 881-N-04",
      "status": "active",
      "address": "Haldenrainstr. 184",
      "city": "Stuttgart",
      "postal_code": "70437",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.834040",
        "longitude": "9.195860"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084587",
          "id": "DE*STR*E10139*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116698",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084588",
          "id": "DE*STR*E10139*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116697",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751395",
      "name": "Heerstraße 108 LADE / 716-N-03",
      "status": "active",
      "address": "Heerstr. 108",
      "city": "Stuttgart",
      "postal_code": "70563",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.737960",
        "longitude": "9.105830"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084589",
          "id": "DE*STR*E10140*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116696",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084590",
          "id": "DE*STR*E10140*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116695",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751396",
      "name": "Heerstraße ggü. 28 LADE / 716-N-02",
      "status": "active",
      "address": "Heerstr. 28",
      "city": "Stuttgart",
      "postal_code": "70563",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.731357",
        "longitude": "9.098193"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084591",
          "id": "DE*STR*E10141*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116694",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084592",
          "id": "DE*STR*E10141*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116693",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751398",
      "name": "Heilbronner Straße 128/1 LADE / 131-N-02",
      "status": "active",
      "address": "Heilbronner Str. 128/1",
      "city": "Stuttgart",
      "postal_code": "70191",
      "country": "DE",
      "directions": "Hedwig-Dohm-Straße 1 Parkplatz ",
      "comment": "",
      "coordinates": {
        "latitude": "48.797846",
        "longitude": "9.182833"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084595",
          "id": "DE*STR*E10143*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116690",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084596",
          "id": "DE*STR*E10143*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116689",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751400",
      "name": "Heumadener Straße 70 LADE / 361-N-02",
      "status": "active",
      "address": "Heumadener Str. 70",
      "city": "Stuttgart",
      "postal_code": "70329",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.756650",
        "longitude": "9.249630"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084599",
          "id": "DE*STR*E10145*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116686",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084600",
          "id": "DE*STR*E10145*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116685",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751402",
      "name": "Hirschsprungallee 2 LADE / 861-N-04",
      "status": "active",
      "address": "Hirschsprungallee 2",
      "city": "Stuttgart",
      "postal_code": "70435",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.828850",
        "longitude": "9.151720"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084603",
          "id": "DE*STR*E10147*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116682",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084604",
          "id": "DE*STR*E10147*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116681",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751403",
      "name": "Hoffeldstraße 215/1 LADE / 321-N-02",
      "status": "active",
      "address": "Hoffeldstraße 215/1",
      "city": "Stuttgart",
      "postal_code": "70597",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.733530",
        "longitude": "9.184010"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084605",
          "id": "DE*STR*E10148*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116680",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084606",
          "id": "DE*STR*E10148*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116679",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751404",
      "name": "Hohentwielstraße 34 LADE / 165-N-05",
      "status": "active",
      "address": "Hohentwielstraße 34",
      "city": "Stuttgart",
      "postal_code": "70199",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.764190",
        "longitude": "9.154430"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084607",
          "id": "DE*STR*E10149*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116678",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084608",
          "id": "DE*STR*E10149*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116677",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751405",
      "name": "Hoppenlaustraße 9 LADE / 104-N-03",
      "status": "active",
      "address": "Hoppenlaustraße 9",
      "city": "Stuttgart",
      "postal_code": "70174",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.782790",
        "longitude": "9.166240"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084609",
          "id": "DE*STR*E10150*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116676",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084610",
          "id": "DE*STR*E10150*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116675",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751406",
      "name": "Hornissenweg 102 LADE / 642-N-03",
      "status": "active",
      "address": "Hornissenweg 102",
      "city": "Stuttgart",
      "postal_code": "70439",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.853290",
        "longitude": "9.152030"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084611",
          "id": "DE*STR*E10101*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116674",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084612",
          "id": "DE*STR*E10101*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116673",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751407",
      "name": "Burggrafenweg LADE / 171-N-04",
      "status": "active",
      "address": "Burgggrafenweg 1",
      "city": "Stuttgart",
      "postal_code": "70569",
      "country": "DE",
      "directions": "Ecke Hummelwiesenweg",
      "comment": "",
      "coordinates": {
        "latitude": "48.741198",
        "longitude": "9.136817"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084613",
          "id": "DE*STR*E10152*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116672",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084614",
          "id": "DE*STR*E10152*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116671",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751408",
      "name": "Im Chausseefeld 17 LADE / 552-N-01",
      "status": "active",
      "address": "Im Chausseefeld 17",
      "city": "Stuttgart",
      "postal_code": "70599",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.714356",
        "longitude": "9.196937"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084615",
          "id": "DE*STR*E10153*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116670",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084616",
          "id": "DE*STR*E10153*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116669",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751409",
      "name": "In den Obstwiesen 11 LADE / 891-N-02",
      "status": "active",
      "address": "In den Obstwiesen 11",
      "city": "Stuttgart",
      "postal_code": "70437",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.839480",
        "longitude": "9.189080"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084617",
          "id": "DE*STR*E10154*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116668",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084618",
          "id": "DE*STR*E10154*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116667",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751410",
      "name": "Johannesstraße 6 LADE / 184-N-09",
      "status": "active",
      "address": "Johannesstr. 6",
      "city": "Stuttgart",
      "postal_code": "70176",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.774700",
        "longitude": "9.164040"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084619",
          "id": "DE*STR*E10155*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116666",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084620",
          "id": "DE*STR*E10155*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116665",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751411",
      "name": "Johannesstraße 87 LADE / 183-N-02",
      "status": "active",
      "address": "Johannesstr. 87",
      "city": "Stuttgart",
      "postal_code": "70176",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.781400",
        "longitude": "9.158380"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084621",
          "id": "DE*STR*E10156*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116664",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084622",
          "id": "DE*STR*E10156*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116663",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751412",
      "name": "Kolbäcker Straße 2 LADE / 405-N-03",
      "status": "active",
      "address": "Kolbäcker Str. 2",
      "city": "Stuttgart",
      "postal_code": "70567",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.730180",
        "longitude": "9.155540"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084623",
          "id": "DE*STR*E10102*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116662",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084624",
          "id": "DE*STR*E10102*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116661",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751413",
      "name": "Kölner Straße 32 LADE / 501-N-02",
      "status": "active",
      "address": "Kölner Str. 32",
      "city": "Stuttgart",
      "postal_code": "70376",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.821460",
        "longitude": "9.203020"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084625",
          "id": "DE*STR*E10158*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116660",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084626",
          "id": "DE*STR*E10158*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116659",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751414",
      "name": "König-Karl-Straße 5 (1) LADE / 204-N-03 ",
      "status": "active",
      "address": "König-Karl-Str. 5 (1)",
      "city": "Stuttgart",
      "postal_code": "70372",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.807636",
        "longitude": "9.222274"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084627",
          "id": "DE*STR*E10159*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116658",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084628",
          "id": "DE*STR*E10159*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116657",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751415",
      "name": "König-Karl-Straße 5 (2) LADE / 204-N-01",
      "status": "active",
      "address": "König-Karl-Str. 5 (2)",
      "city": "Stuttgart",
      "postal_code": "70372",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.807649",
        "longitude": "9.222340"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084629",
          "id": "DE*STR*E10160*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116656",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084630",
          "id": "DE*STR*E10160*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116655",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751416",
      "name": "Auerbachstr. 200 LADE / 221-N-02",
      "status": "active",
      "address": "Auerbachstr. 200",
      "city": "Stuttgart",
      "postal_code": "70376",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.818975",
        "longitude": "9.194482"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084631",
          "id": "DE*STR*E10161*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116654",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084632",
          "id": "DE*STR*E10161*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116653",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751417",
      "name": "Krefelder Straße 35 (Ecke Haldenstr.) LADE / 211-N-03",
      "status": "active",
      "address": "Krefelder Str. 35",
      "city": "Stuttgart",
      "postal_code": "70376",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.811430",
        "longitude": "9.212330"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084633",
          "id": "DE*STR*E10162*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116652",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084634",
          "id": "DE*STR*E10162*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116651",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751418",
      "name": "Laustraße 20 LADE / 421-N-02",
      "status": "active",
      "address": "Laustr. 20",
      "city": "Stuttgart",
      "postal_code": "70597",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.743179",
        "longitude": "9.153758"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084635",
          "id": "DE*STR*E10163*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116650",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084636",
          "id": "DE*STR*E10163*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116649",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751419",
      "name": "Laustraße 63 LADE / 421-N-03",
      "status": "active",
      "address": "Laustr. 63",
      "city": "Stuttgart",
      "postal_code": "70597",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.746960",
        "longitude": "9.155340"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084637",
          "id": "DE*STR*E10164*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116648",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084638",
          "id": "DE*STR*E10164*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116647",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751420",
      "name": "Lenzhalde 41 LADE / 122-N-02",
      "status": "active",
      "address": "Lenzhalde 41",
      "city": "Stuttgart",
      "postal_code": "70192",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.790170",
        "longitude": "9.159230"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084639",
          "id": "DE*STR*E10165*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116646",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084640",
          "id": "DE*STR*E10165*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116645",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751422",
      "name": "Ludwigstraße 128 LADE / 185-N-05",
      "status": "active",
      "address": "Ludwigstr. 128",
      "city": "Stuttgart",
      "postal_code": "70197",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.771160",
        "longitude": "9.151340"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084643",
          "id": "DE*STR*E10167*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116642",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084644",
          "id": "DE*STR*E10167*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116641",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751423",
      "name": "Lüglensheidestraße 8 LADE / 481-N-06",
      "status": "active",
      "address": "Lüglensheidestr. 8",
      "city": "Stuttgart",
      "postal_code": "70378",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.832470",
        "longitude": "9.226120"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084645",
          "id": "DE*STR*E10168*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116640",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084646",
          "id": "DE*STR*E10168*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116639",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751424",
      "name": "Luzernestraße 13 LADE / 551-N-04",
      "status": "active",
      "address": "Luzernestr. 13",
      "city": "Stuttgart",
      "postal_code": "70599",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.699170",
        "longitude": "9.213950"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084647",
          "id": "DE*STR*E10169*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116638",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084648",
          "id": "DE*STR*E10169*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116637",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751426",
      "name": "Marbacherstraße 59 LADE / 865-N-05",
      "status": "active",
      "address": "Marbacherstr. 59",
      "city": "Stuttgart",
      "postal_code": "70435",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.834390",
        "longitude": "9.176634"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084651",
          "id": "DE*STR*E10171*001",
          "status": "OUTOFORDER",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116634",
              "status": "OUTOFORDER",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084652",
          "id": "DE*STR*E10171*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116633",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751427",
      "name": "Martha-Schmidtmann-Straße 2 LADE / 203-N-03",
      "status": "active",
      "address": "Martha-Schmidtmann-Str. 2",
      "city": "Stuttgart",
      "postal_code": "70374",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.807770",
        "longitude": "9.234330"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084653",
          "id": "DE*STR*E10172*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116632",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084654",
          "id": "DE*STR*E10172*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116631",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751428",
      "name": "Martin-Luther-Str. 95 LADE / 206-N-03",
      "status": "active",
      "address": "Martin-Luther-Str. 95",
      "city": "Stuttgart",
      "postal_code": "70372",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.800840",
        "longitude": "9.226130"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084655",
          "id": "DE*STR*E10173*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116630",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084656",
          "id": "DE*STR*E10173*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116629",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751429",
      "name": "Masurenstraße 2 LADE / 203-N-02",
      "status": "active",
      "address": "Masurenstr. 2",
      "city": "Stuttgart",
      "postal_code": "70374",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.810040",
        "longitude": "9.249260"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084657",
          "id": "DE*STR*E10174*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116628",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084658",
          "id": "DE*STR*E10174*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116627",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751430",
      "name": "Max-Brod-Weg 6 LADE / 451-N-04",
      "status": "active",
      "address": "Max-Brod-Weg 6",
      "city": "Stuttgart",
      "postal_code": "70437",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.835490",
        "longitude": "9.203900"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084659",
          "id": "DE*STR*E10175*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116626",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084660",
          "id": "DE*STR*E10175*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116625",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751431",
      "name": "Melanchtonstraße 30 LADE / 202-N-01",
      "status": "active",
      "address": "Melanchtonstr. 30",
      "city": "Stuttgart",
      "postal_code": "70374",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.808160",
        "longitude": "9.231550"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084661",
          "id": "DE*STR*E10176*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116624",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084662",
          "id": "DE*STR*E10176*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116623",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751432",
      "name": "Mimosenweg 21 LADE / 231-N-03",
      "status": "active",
      "address": "Mimosenweg 21",
      "city": "Stuttgart",
      "postal_code": "70374",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.818430",
        "longitude": "9.244190"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084663",
          "id": "DE*STR*E10177*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116622",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084664",
          "id": "DE*STR*E10177*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116621",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751433",
      "name": "Mönchhof 4 LADE / 551-N-05",
      "status": "active",
      "address": "Mönchhof 4",
      "city": "Stuttgart",
      "postal_code": "70599",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.700952",
        "longitude": "9.215622"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084665",
          "id": "DE*STR*E10178*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116620",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084666",
          "id": "DE*STR*E10178*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116619",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751434",
      "name": "Mönchsbergstraße 109 LADE / 867-N-02",
      "status": "active",
      "address": "Mönchsbergstr. 109",
      "city": "Stuttgart",
      "postal_code": "70435",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.829060",
        "longitude": "9.185840"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084667",
          "id": "DE*STR*E10179*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116618",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084668",
          "id": "DE*STR*E10179*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116617",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751435",
      "name": "Moselstraße 86 LADE / 501-N-04",
      "status": "active",
      "address": "Moselstr. 86",
      "city": "Stuttgart",
      "postal_code": "70376",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.823700",
        "longitude": "9.217160"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084669",
          "id": "DE*STR*E10180*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116616",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084670",
          "id": "DE*STR*E10180*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116615",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751436",
      "name": "Münchinger Straße 60 LADE / 642-N-05",
      "status": "active",
      "address": "Münchinger Str. 60",
      "city": "Stuttgart",
      "postal_code": "70439",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.849740",
        "longitude": "9.149720"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084671",
          "id": "DE*STR*E10104*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116614",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084672",
          "id": "DE*STR*E10104*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116613",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751438",
      "name": "Nähterstraße 67 LADE / 761-N-05",
      "status": "active",
      "address": "Nähterstr. 67",
      "city": "Stuttgart",
      "postal_code": "70327",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.774816",
        "longitude": "9.236829"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084675",
          "id": "DE*STR*E10183*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116610",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084676",
          "id": "DE*STR*E10183*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116609",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751439",
      "name": "Neue Weinsteige 5 LADE / 162-N-09",
      "status": "active",
      "address": "Neue Weinsteige 5",
      "city": "Stuttgart",
      "postal_code": "70180",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.766520",
        "longitude": "9.178900"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084677",
          "id": "DE*STR*E10105*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116608",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084678",
          "id": "DE*STR*E10105*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116607",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751440",
      "name": "Nürnberger Straße 38 LADE / 210-N-03",
      "status": "active",
      "address": "Nürnberger Str. 38",
      "city": "Stuttgart",
      "postal_code": "70374",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.806800",
        "longitude": "9.236740"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084679",
          "id": "DE*STR*E10185*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116606",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084680",
          "id": "DE*STR*E10185*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116605",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751441",
      "name": "Ob dem Steinbach 11 LADE / 721-N-01",
      "status": "active",
      "address": "Ob dem Steinbach 11",
      "city": "Stuttgart",
      "postal_code": "70569",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.749660",
        "longitude": "9.082280"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084681",
          "id": "DE*STR*E10186*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116604",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084682",
          "id": "DE*STR*E10186*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116603",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751442",
      "name": "Obere Waiblinger Straße 110 LADE / 202-N-02",
      "status": "active",
      "address": "Obere Waiblinger Str. 110",
      "city": "Stuttgart",
      "postal_code": "70374",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.806430",
        "longitude": "9.231650"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084683",
          "id": "DE*STR*E10187*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116602",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084684",
          "id": "DE*STR*E10187*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116601",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751443",
      "name": "Oberwiesenstraße 69 LADE / 601-N-05",
      "status": "active",
      "address": "Oberwiesenstr. 69",
      "city": "Stuttgart",
      "postal_code": "70619",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.745520",
        "longitude": "9.214970"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084685",
          "id": "DE*STR*E10188*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116600",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084686",
          "id": "DE*STR*E10188*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116599",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751445",
      "name": "Friedrichshafener Str. 9 LADE / 361-N-03",
      "status": "active",
      "address": "Friedrichshafener Str. 9",
      "city": "Stuttgart",
      "postal_code": "70329",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.758842",
        "longitude": "9.256443"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084689",
          "id": "DE*STR*E10190*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116596",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084690",
          "id": "DE*STR*E10190*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116595",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751446",
      "name": "Paracelsusstraße 37 LADE / 551-N-06",
      "status": "active",
      "address": "Paracelsusstr. 37",
      "city": "Stuttgart",
      "postal_code": "70599",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.705880",
        "longitude": "9.210380"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084691",
          "id": "DE*STR*E10191*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116594",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084692",
          "id": "DE*STR*E10191*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116593",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751447",
      "name": "Pfarrer-Georgii-Str. LADE / 146-N-03",
      "status": "active",
      "address": "Pfarrer-Georgii-Str. 1",
      "city": "Stuttgart",
      "postal_code": "70188",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.782450",
        "longitude": "9.226370"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084693",
          "id": "DE*STR*E10192*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116592",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084694",
          "id": "DE*STR*E10192*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116591",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751448",
      "name": "Haldenrainstr. ggü. 31 LADE / 881-N-09 (2. LS)",
      "status": "active",
      "address": "Haldenrainstr. ggü. 31",
      "city": "Stuttgart",
      "postal_code": "70437",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.829854",
        "longitude": "9.180246"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084695",
          "id": "DE*STR*E10193*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116590",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084696",
          "id": "DE*STR*E10193*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116589",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751449",
      "name": "Salzäckerstr. 149/5 LADE / 406-N-01",
      "status": "active",
      "address": "Salzäckerstr. 149/5 149/5",
      "city": "Stuttgart",
      "postal_code": "70567",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.719121",
        "longitude": "9.160420"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084697",
          "id": "DE*STR*E10194*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116588",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084698",
          "id": "DE*STR*E10194*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116587",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751450",
      "name": "Quellenstraße 7 LADE / 212-N-01",
      "status": "active",
      "address": "Quellenstr. 7",
      "city": "Stuttgart",
      "postal_code": "70376",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.808170",
        "longitude": "9.199830"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084699",
          "id": "DE*STR*E10195*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116586",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084700",
          "id": "DE*STR*E10195*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116585",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751451",
      "name": "Raingärtlesweg LADE / 471-N-02",
      "status": "active",
      "address": "Raingärtlesweg 1",
      "city": "Stuttgart",
      "postal_code": "70378",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.836030",
        "longitude": "9.222917"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084701",
          "id": "DE*STR*E10196*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116584",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084702",
          "id": "DE*STR*E10196*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116583",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751452",
      "name": "Räpplenstraße 17 LADE / 131-N-03",
      "status": "active",
      "address": "Räpplenstr. 17",
      "city": "Stuttgart",
      "postal_code": "70191",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.789930",
        "longitude": "9.179270"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084703",
          "id": "DE*STR*E10197*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116582",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084704",
          "id": "DE*STR*E10197*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116581",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751453",
      "name": "Reinsburgstraße 185B LADE / 187-N-02",
      "status": "active",
      "address": "Reinsburgstr. 185B",
      "city": "Stuttgart",
      "postal_code": "70197",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.769210",
        "longitude": "9.147190"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084705",
          "id": "DE*STR*E10198*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116580",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084706",
          "id": "DE*STR*E10198*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116579",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751454",
      "name": "Reutlinger Straße 50 LADE / 312-N-03",
      "status": "active",
      "address": "Reutlinger Str. 50",
      "city": "Stuttgart",
      "postal_code": "70597",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.745950",
        "longitude": "9.175520"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084707",
          "id": "DE*STR*E10199*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116578",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084708",
          "id": "DE*STR*E10199*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116577",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751455",
      "name": "Richterstraße 23 LADE / 402-N-07",
      "status": "active",
      "address": "Richterstr. 23",
      "city": "Stuttgart",
      "postal_code": "70567",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.727730",
        "longitude": "9.149470"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084709",
          "id": "DE*STR*E10200*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116576",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084710",
          "id": "DE*STR*E10200*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116575",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751456",
      "name": "Rotebühlstraße 121 LADE / 185-N-08",
      "status": "active",
      "address": "Rotebühlstr. 121",
      "city": "Stuttgart",
      "postal_code": "70178",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.770980",
        "longitude": "9.159640"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084711",
          "id": "DE*STR*E10201*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116574",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084712",
          "id": "DE*STR*E10201*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116573",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751457",
      "name": "Rotweg 90a LADE / 881-N-03",
      "status": "active",
      "address": "Rotweg 90A",
      "city": "Stuttgart",
      "postal_code": "70437",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.834163",
        "longitude": "9.187623"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084713",
          "id": "DE*STR*E10202*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116572",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084714",
          "id": "DE*STR*E10202*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116571",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751458",
      "name": "Äckerwaldstr. 15 LADE / 601-N-06",
      "status": "active",
      "address": "Äckerwaldstr. 15",
      "city": "Stuttgart",
      "postal_code": "70619",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.745336",
        "longitude": "9.206430"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084715",
          "id": "DE*STR*E10203*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116570",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084716",
          "id": "DE*STR*E10203*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116569",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751460",
      "name": "Rümelinstraße 69 LADE / 129-N-04",
      "status": "active",
      "address": "Rümelinstr. 69",
      "city": "Stuttgart",
      "postal_code": "70191",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.799180",
        "longitude": "9.193160"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084719",
          "id": "DE*STR*E10205*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116566",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084720",
          "id": "DE*STR*E10205*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116565",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751461",
      "name": "Scharrstraße 21 LADE / 711-N-05",
      "status": "active",
      "address": "Scharrstr. 21",
      "city": "Stuttgart",
      "postal_code": "70563",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.730240",
        "longitude": "9.115440"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084721",
          "id": "DE*STR*E10206*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116564",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084722",
          "id": "DE*STR*E10206*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116563",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751462",
      "name": "Schemppstraße 85 LADE / 621-N-02",
      "status": "active",
      "address": "Schemppstr. 85",
      "city": "Stuttgart",
      "postal_code": "70619",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.739850",
        "longitude": "9.219750"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084723",
          "id": "DE*STR*E10207*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116562",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084724",
          "id": "DE*STR*E10207*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116561",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751463",
      "name": "Schildfarnweg 1 LADE / 371-N-01",
      "status": "active",
      "address": "Schildfarnweg 1",
      "city": "Stuttgart",
      "postal_code": "70619",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.751940",
        "longitude": "9.242140"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084725",
          "id": "DE*STR*E10208*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116560",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084726",
          "id": "DE*STR*E10208*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116559",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751464",
      "name": "Schneideräckerstraße 15 LADE / 481-N-03",
      "status": "active",
      "address": "Schneideräckerstr. 15",
      "city": "Stuttgart",
      "postal_code": "70378",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.834870",
        "longitude": "9.237320"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084727",
          "id": "DE*STR*E10209*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116558",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084728",
          "id": "DE*STR*E10209*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116557",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751465",
      "name": "Schockenriedstraße 4 LADE / 714-N-02",
      "status": "active",
      "address": "Schockenriedstr. 4",
      "city": "Stuttgart",
      "postal_code": "70565",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.726360",
        "longitude": "9.116030"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084729",
          "id": "DE*STR*E10210*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116556",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084730",
          "id": "DE*STR*E10210*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116555",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751466",
      "name": "Schrozberger Straße 5 LADE / 867-N-03",
      "status": "active",
      "address": "Schrozbergerstr. 5",
      "city": "Stuttgart",
      "postal_code": "70435",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.825970",
        "longitude": "9.174110"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084732",
          "id": "DE*STR*E10211*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116554",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084733",
          "id": "DE*STR*E10211*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116553",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751467",
      "name": "Langobardenstr. 36 LADE / 862-N-05",
      "status": "active",
      "address": "Langobardenstr. 36",
      "city": "Stuttgart",
      "postal_code": "70435",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.834410",
        "longitude": "9.161170"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084734",
          "id": "DE*STR*E10252*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116552",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084735",
          "id": "DE*STR*E10252*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116551",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751468",
      "name": "Schützenbühlstraße 53 (LS rechts) LADE / 862-N-02",
      "status": "active",
      "address": "Schützenbühlstr. 53",
      "city": "Stuttgart",
      "postal_code": "70435",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.834360",
        "longitude": "9.159110"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084736",
          "id": "DE*STR*E10213*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116550",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084737",
          "id": "DE*STR*E10213*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116549",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751469",
      "name": "Schützenbühlstraße 53 (LS links) LADE / 862-N-03",
      "status": "active",
      "address": "Schützenbühlstr. 53",
      "city": "Stuttgart",
      "postal_code": "70435",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.834400",
        "longitude": "9.157080"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084738",
          "id": "DE*STR*E10214*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116548",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084739",
          "id": "DE*STR*E10214*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116547",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751470",
      "name": "Schwabstraße 159 LADE / 182-N-03",
      "status": "active",
      "address": "Schwabstr. 159",
      "city": "Stuttgart",
      "postal_code": "70193",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.779970",
        "longitude": "9.155890"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084740",
          "id": "DE*STR*E10215*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116546",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084741",
          "id": "DE*STR*E10215*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116545",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751471",
      "name": "Schwarenbergstraße 153 LADE / 147-N-06",
      "status": "active",
      "address": "Schwarenbergstr. 153",
      "city": "Stuttgart",
      "postal_code": "70184",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.779940",
        "longitude": "9.202730"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084742",
          "id": "DE*STR*E10216*001",
          "status": "OUTOFORDER",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116544",
              "status": "OUTOFORDER",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084743",
          "id": "DE*STR*E10216*002",
          "status": "OUTOFORDER",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116543",
              "status": "OUTOFORDER",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751472",
      "name": "Schwarzwaldstraße 51 LADE / 171-N-03",
      "status": "active",
      "address": "Schwarzwaldstr. 51",
      "city": "Stuttgart",
      "postal_code": "70569",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.741390",
        "longitude": "9.126680"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084744",
          "id": "DE*STR*E10217*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116542",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084745",
          "id": "DE*STR*E10217*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116541",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751473",
      "name": "Seeadlerstraße 7/1 LADE / 481-N-02",
      "status": "active",
      "address": "Seeadlerstr: 7/1",
      "city": "Stuttgart",
      "postal_code": "70378",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.832514",
        "longitude": "9.228835"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084746",
          "id": "DE*STR*E10218*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116540",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084747",
          "id": "DE*STR*E10218*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116539",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751474",
      "name": "Seerosenstraße 13 LADE / 711-N-04",
      "status": "active",
      "address": "Seerosenstr. 13",
      "city": "Stuttgart",
      "postal_code": "70563",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.731010",
        "longitude": "9.106810"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084749",
          "id": "DE*STR*E10219*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116538",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084750",
          "id": "DE*STR*E10219*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116537",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751475",
      "name": "Seidenstraße 21 LADE / 183-N-05",
      "status": "active",
      "address": "Seidenstr. 21",
      "city": "Stuttgart",
      "postal_code": "70174",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.779670",
        "longitude": "9.166330"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084751",
          "id": "DE*STR*E10220*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116536",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084752",
          "id": "DE*STR*E10220*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116535",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751476",
      "name": "Sofie-Reis-Straße 13 LADE / 641-N-03",
      "status": "active",
      "address": "Sofie-Reis-Str. 13",
      "city": "Stuttgart",
      "postal_code": "70439",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.845033",
        "longitude": "9.160453"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084753",
          "id": "DE*STR*E10100*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116534",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084754",
          "id": "DE*STR*E10100*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116533",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751477",
      "name": "Sonnenbergstraße 30 LADE / 161-N-02",
      "status": "active",
      "address": "Sonnenbergstr. 30",
      "city": "Stuttgart",
      "postal_code": "70184",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.768320",
        "longitude": "9.189690"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084755",
          "id": "DE*STR*E10222*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116532",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084756",
          "id": "DE*STR*E10222*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116531",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751478",
      "name": "Sophie-Tschorn-Str. 1 LADE / 201-N-02  (Z45988/005)",
      "status": "active",
      "address": "Sophie-Tschom-Str. 1",
      "city": "Stuttgart",
      "postal_code": "70374",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.816930",
        "longitude": "9.237920"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084757",
          "id": "DE*STR*E10223*001",
          "status": "OUTOFORDER",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116530",
              "status": "OUTOFORDER",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084758",
          "id": "DE*STR*E10223*002",
          "status": "OUTOFORDER",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116529",
              "status": "OUTOFORDER",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751479",
      "name": "Lammgasse 7 LADE / 205-N-02",
      "status": "active",
      "address": "Lammgasse. 7",
      "city": "Stuttgart",
      "postal_code": "70327",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.805571",
        "longitude": "9.214197"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084759",
          "id": "DE*STR*E10224*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116528",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084760",
          "id": "DE*STR*E10224*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116527",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751480",
      "name": "Stammheimer Straße ggü. 20 LADE / 862-N-04",
      "status": "active",
      "address": "Stammheimer Str. 20",
      "city": "Stuttgart",
      "postal_code": "70435",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.835262",
        "longitude": "9.163832"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084761",
          "id": "DE*STR*E10225*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116526",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084762",
          "id": "DE*STR*E10225*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116525",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751481",
      "name": "Steinäcker 2 LADE / 621-N-03",
      "status": "active",
      "address": "Steinäcker 2",
      "city": "Stuttgart",
      "postal_code": "70619",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.734460",
        "longitude": "9.213290"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084763",
          "id": "DE*STR*E10226*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116524",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084764",
          "id": "DE*STR*E10226*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116523",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751482",
      "name": "Steinwaldstraße 92 LADE / 561-N-03",
      "status": "active",
      "address": "Steinwaldstr. 92",
      "city": "Stuttgart",
      "postal_code": "70599",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.717080",
        "longitude": "9.199490"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084765",
          "id": "DE*STR*E10103*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116522",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084766",
          "id": "DE*STR*E10103*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116521",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751483",
      "name": "Theophil-Wurm-Straße 28 LADE / 411-N-03",
      "status": "active",
      "address": "Theophil-Wurm-Str. 28",
      "city": "Stuttgart",
      "postal_code": "70565",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.712480",
        "longitude": "9.154240"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084767",
          "id": "DE*STR*E10228*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116520",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084768",
          "id": "DE*STR*E10228*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116519",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751484",
      "name": "Veitstraße 81 LADE / 441-N-03",
      "status": "active",
      "address": "Veitstr. 81",
      "city": "Stuttgart",
      "postal_code": "70378",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.845776",
        "longitude": "9.232358"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084769",
          "id": "DE*STR*E10229*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116518",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084770",
          "id": "DE*STR*E10229*002",
          "status": "OUTOFORDER",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116517",
              "status": "OUTOFORDER",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751485",
      "name": "Verdistraße 51 LADE / 295-N-02",
      "status": "active",
      "address": "Verdistr. 51",
      "city": "Stuttgart",
      "postal_code": "70195",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.781480",
        "longitude": "9.123830"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084771",
          "id": "DE*STR*E10230*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116516",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084772",
          "id": "DE*STR*E10230*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116515",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751486",
      "name": "Vogelsangstraße 50 LADE / 186-N-03",
      "status": "active",
      "address": "Vogelsangstr. 50",
      "city": "Stuttgart",
      "postal_code": "70197",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.774250",
        "longitude": "9.152190"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084773",
          "id": "DE*STR*E10231*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116514",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084774",
          "id": "DE*STR*E10231*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116513",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751487",
      "name": "Waldburgstraße 21 LADE / 715-N-04",
      "status": "active",
      "address": "Waldburgstr. 21",
      "city": "Stuttgart",
      "postal_code": "70563",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.724510",
        "longitude": "9.107660"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084775",
          "id": "DE*STR*E10232*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116512",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084776",
          "id": "DE*STR*E10232*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116511",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751490",
      "name": "Wiesbadener Straße 52 LADE / 204-N-04",
      "status": "active",
      "address": "Wiesbadener Str. 52",
      "city": "Stuttgart",
      "postal_code": "70372",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.806460",
        "longitude": "9.225930"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084781",
          "id": "DE*STR*E10235*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116506",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084782",
          "id": "DE*STR*E10235*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116505",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751491",
      "name": "Wildunger Straße 53 LADE / 206-N-02",
      "status": "active",
      "address": "Wildunger Str. 53",
      "city": "Stuttgart",
      "postal_code": "70372",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.803360",
        "longitude": "9.225880"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084783",
          "id": "DE*STR*E10236*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116504",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084784",
          "id": "DE*STR*E10236*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116503",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751492",
      "name": "Wildunger Straße 86 LADE / 206-N-06",
      "status": "active",
      "address": "Wildunger Str. 86",
      "city": "Stuttgart",
      "postal_code": "70372",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.803830",
        "longitude": "9.229730"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084785",
          "id": "DE*STR*E10237*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116502",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084786",
          "id": "DE*STR*E10237*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116501",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751493",
      "name": "Schellingstr. 15 LADE / 104-N-05",
      "status": "active",
      "address": "Schellingstr. 15",
      "city": "Stuttgart",
      "postal_code": "70174",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.780100",
        "longitude": "9.173840"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084787",
          "id": "DE*STR*E10238*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116500",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084788",
          "id": "DE*STR*E10238*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116499",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751494",
      "name": "Winterbacher Straße 36 LADE / 210-N-04",
      "status": "active",
      "address": "Winterbacher Str. 36",
      "city": "Stuttgart",
      "postal_code": "70374",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.805580",
        "longitude": "9.244580"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084789",
          "id": "DE*STR*E10239*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116498",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084790",
          "id": "DE*STR*E10239*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116497",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751495",
      "name": "Im Wolfer 23 LADE / 551-N-07",
      "status": "active",
      "address": "Im Wolfer 23",
      "city": "Stuttgart",
      "postal_code": "70599",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.710007",
        "longitude": "9.201789"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084791",
          "id": "DE*STR*E10240*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116496",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084792",
          "id": "DE*STR*E10240*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116495",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751496",
      "name": "Wollinstraße 6 LADE / 863-N-01",
      "status": "active",
      "address": "Wollinstr. 6",
      "city": "Stuttgart",
      "postal_code": "70439",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.838120",
        "longitude": "9.147520"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084793",
          "id": "DE*STR*E10241*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116494",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084794",
          "id": "DE*STR*E10241*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116493",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751497",
      "name": "Württembergstraße 312 LADE / 681-N-01",
      "status": "active",
      "address": "Württembergstr. 312",
      "city": "Stuttgart",
      "postal_code": "70327",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.783310",
        "longitude": "9.270610"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084795",
          "id": "DE*STR*E10242*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116492",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084796",
          "id": "DE*STR*E10242*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116491",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "751498",
      "name": "Zanderweg 2 LADE / 461-N-02",
      "status": "active",
      "address": "Zanderweg 2",
      "city": "Stuttgart",
      "postal_code": "70378",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.843722",
        "longitude": "9.218977"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "2084797",
          "id": "DE*STR*E10243*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116490",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "2084798",
          "id": "DE*STR*E10243*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "240116489",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "1463360",
      "name": "SVG Autohof Süd",
      "status": "active",
      "address": "Hedelfinger Str. 25",
      "city": "Stuttgart",
      "postal_code": "70372",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.769719",
        "longitude": "9.248259"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "4475100",
          "id": "DE*STR*E20001*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "264979317",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2_COMBO",
              "format": "CABLE",
              "power_type": "DC",
              "ampere": "400",
              "voltage": "1000",
              "max_power": 300,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "4475101",
          "id": "DE*STR*E20001*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "264979318",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2_COMBO",
              "format": "CABLE",
              "power_type": "DC",
              "ampere": "400",
              "voltage": "1000",
              "max_power": 300,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "4475102",
          "id": "DE*STR*E20002*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "264979319",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2_COMBO",
              "format": "CABLE",
              "power_type": "DC",
              "ampere": "400",
              "voltage": "1000",
              "max_power": 300,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "4475103",
          "id": "DE*STR*E20002*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "264979320",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2_COMBO",
              "format": "CABLE",
              "power_type": "DC",
              "ampere": "400",
              "voltage": "1000",
              "max_power": 300,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "4475104",
          "id": "DE*STR*E20003*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "264979321",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2_COMBO",
              "format": "CABLE",
              "power_type": "DC",
              "ampere": "400",
              "voltage": "1000",
              "max_power": 300,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "4475105",
          "id": "DE*STR*E20003*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "264979322",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2_COMBO",
              "format": "CABLE",
              "power_type": "DC",
              "ampere": "400",
              "voltage": "1000",
              "max_power": 300,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "4475111",
          "id": "DE*STR*E20004*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "264979328",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2_COMBO",
              "format": "CABLE",
              "power_type": "DC",
              "ampere": "400",
              "voltage": "1000",
              "max_power": 300,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "4475112",
          "id": "DE*STR*E20004*002",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "264979329",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2_COMBO",
              "format": "CABLE",
              "power_type": "DC",
              "ampere": "400",
              "voltage": "1000",
              "max_power": 300,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "4475113",
          "id": "DE*STR*E20005*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "264979330",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2_COMBO",
              "format": "CABLE",
              "power_type": "DC",
              "ampere": "400",
              "voltage": "1000",
              "max_power": 300,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "4475114",
          "id": "DE*STR*E20005*002",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "264979331",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2_COMBO",
              "format": "CABLE",
              "power_type": "DC",
              "ampere": "400",
              "voltage": "1000",
              "max_power": 300,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848",
        "9126"
      ]
    },
    {
      "id": "1465678",
      "name": "Jakob-Bleyer-Straße",
      "status": "active",
      "address": "Jakob-Bleyer-Str. 2",
      "city": "Gerlingen",
      "postal_code": "70839",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.801625",
        "longitude": "9.076751"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "4491088",
          "id": "DE*STR*E10244*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "265177957",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "4491089",
          "id": "DE*STR*E10244*002",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "265177958",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "4491091",
          "id": "DE*STR*E10245*001",
          "status": "CHARGING",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "265177960",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "4491092",
          "id": "DE*STR*E10245*002",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "265177961",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "1499991",
      "name": "Meitnerstraße 10 LADE",
      "status": "active",
      "address": "Meitnerstr. 10",
      "city": "Stuttgart",
      "postal_code": "70563",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.738748",
        "longitude": "9.109618"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "4687951",
          "id": "DE*STR*E10234*001",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "267204922",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "4687952",
          "id": "DE*STR*E10234*002",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "267204923",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "2020962",
      "name": "Römerkastell Spange 2.1",
      "status": "active",
      "address": "Naststr. 17",
      "city": "Stuttgart",
      "postal_code": "70376",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.813000",
        "longitude": "9.209800"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "7349809",
          "id": "DE*STR*E2042546*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "290361448",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7349810",
          "id": "DE*STR*E2042546*002",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "290361449",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7349812",
          "id": "DE*STR*E2042548*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "290361451",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7349813",
          "id": "DE*STR*E2042548*002",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "290361452",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7349814",
          "id": "DE*STR*E2042551*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "290361453",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7349815",
          "id": "DE*STR*E2042551*002",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "290361454",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7349816",
          "id": "DE*STR*E2042553*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "290361455",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7349817",
          "id": "DE*STR*E2042553*002",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "290361456",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7349818",
          "id": "DE*STR*E2042554*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "325544696",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            },
            {
              "id": "290361457",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7349819",
          "id": "DE*STR*E2042554*002",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "290361458",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            },
            {
              "id": "325544697",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7349820",
          "id": "DE*STR*E2042555*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "290361459",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7349821",
          "id": "DE*STR*E2042555*002",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "290361460",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7349822",
          "id": "DE*STR*E2042556*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "290361461",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            },
            {
              "id": "290361462",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7349823",
          "id": "DE*STR*E2042556*002",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "290361463",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7349824",
          "id": "DE*STR*E2042557*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "290361464",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7349825",
          "id": "DE*STR*E2042557*002",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "290361465",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "2185120",
      "name": "B+B Tiefgarage / Kronprinzstr. 6 / 4. UG",
      "status": "active",
      "address": "Kronprinzstr. 6 / 4. UG",
      "city": "Stuttgart",
      "postal_code": "70173",
      "country": "DE",
      "directions": "Die Ladestationen befinden sich in der Tiefgarage im 4. UG.\r\n\r\nBitte beachten Sie: \r\n7 Ladestationen sind durchgehend verfügbar. Bei 3 Ladestationen sind die Öffnungszeiten eingeschränkt, genauere Infos finden Sie an der Beschilderung vor Ort.",
      "comment": "",
      "coordinates": {
        "latitude": "48.777410",
        "longitude": "9.176212"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+4971189121212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "7665438",
          "id": "DE*STR*E2209655*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "300771958",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7665440",
          "id": "DE*STR*E2209657*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "300771959",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7665443",
          "id": "DE*STR*E2209659*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "300771962",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7665445",
          "id": "DE*STR*E2209661*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "300771964",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7665447",
          "id": "DE*STR*E2209662*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "300771966",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7665450",
          "id": "DE*STR*E2209664*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "300771969",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7665451",
          "id": "DE*STR*E2209665*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "300771970",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7665452",
          "id": "DE*STR*E2209666*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "300771971",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7665453",
          "id": "DE*STR*E2209667*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "300771972",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7665454",
          "id": "DE*STR*E2209668*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "300771973",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "8840"
      ]
    },
    {
      "id": "2199469",
      "name": "SpOrt Stuttgart/ LADE",
      "status": "active",
      "address": "Fritz-Walter Weg 19",
      "city": "Stuttgart Bad Canstatt",
      "postal_code": "70372",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.793011",
        "longitude": "9.236277"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+4971189121212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "7697944",
          "id": "DE*STR*E2224956*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "301549998",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7697945",
          "id": "DE*STR*E2224956*002",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "301549999",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7697947",
          "id": "DE*STR*E2224958*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "301550001",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7697949",
          "id": "DE*STR*E2224958*002",
          "status": "CHARGING",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "301550003",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "2216397",
      "name": "Zedernweg 10  LADE / Gerlingen",
      "status": "active",
      "address": "Zedernweg 10",
      "city": "Gerlingen",
      "postal_code": "70839",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.799936",
        "longitude": "9.081416"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "7748442",
          "id": "DE*STR*E2242320*001",
          "status": "CHARGING",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "302614808",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7904465",
          "id": "DE*STR*E2242320*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "306981869",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "2265693",
      "name": "B+B Tiefgarage / Kronprinzstr. 6 / 2. UG / Teil 1",
      "status": "active",
      "address": "Kronprinzstr. 6 / 2. UG",
      "city": "Stuttgart",
      "postal_code": "70173",
      "country": "DE",
      "directions": "Die Ladestationen befinden sich in der Tiefgarage im 2. Untergeschoss.",
      "comment": "",
      "coordinates": {
        "latitude": "48.777610",
        "longitude": "9.176212"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+4971189121212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "7883816",
          "id": "DE*STR*E2294159*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": "01",
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "306301339",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7883817",
          "id": "DE*STR*E2294160*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": "02",
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "306301340",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7883818",
          "id": "DE*STR*E2294165*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": "03",
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "306301341",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7883821",
          "id": "DE*STR*E2294167*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": "04",
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "306301344",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7883834",
          "id": "DE*STR*E2294177*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": "05",
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "306301354",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7883836",
          "id": "DE*STR*E2294179*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": "06",
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "306301357",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7883837",
          "id": "DE*STR*E2294180*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": "07",
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "306301358",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7883839",
          "id": "DE*STR*E2294181*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": "08",
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "306301359",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7883840",
          "id": "DE*STR*E2294182*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": "09",
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "306301360",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7883842",
          "id": "DE*STR*E2294183*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": "10",
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "306301362",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7883843",
          "id": "DE*STR*E2294185*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": "11",
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "306301363",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7883846",
          "id": "DE*STR*E2294186*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": "12",
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "306301366",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7883847",
          "id": "DE*STR*E2294187*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": "13",
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "306301367",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7883848",
          "id": "DE*STR*E2294188*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": "14",
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "306301368",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7883849",
          "id": "DE*STR*E2294189*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": "15",
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "306301369",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7883852",
          "id": "DE*STR*E2294191*001",
          "status": "CHARGING",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": "16",
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "306301372",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7883853",
          "id": "DE*STR*E2294192*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": "17",
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "306301373",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7883854",
          "id": "DE*STR*E2294193*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": "18",
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "306301374",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7883857",
          "id": "DE*STR*E2294195*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": "19",
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "306301377",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7883858",
          "id": "DE*STR*E2294196*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": "20",
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "306301378",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "8840"
      ]
    },
    {
      "id": "2277081",
      "name": "Gerlingen Stadthalle Öffentlich",
      "status": "active",
      "address": "Hauptstr. 54",
      "city": "Gerlingen",
      "postal_code": "70839",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.798068",
        "longitude": "9.061606"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+4971189121212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "7904445",
          "id": "DE*STR*E2304245*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "306981848",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7904446",
          "id": "DE*STR*E2304246*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "306981849",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7904448",
          "id": "DE*STR*E2304248*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "306981851",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7904449",
          "id": "DE*STR*E2304249*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "306981852",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 11,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "2309904",
      "name": "Kesselstr. Ggü. 21 (LS1) LADE/ 761-N-04",
      "status": "active",
      "address": "Kesselstr. 21",
      "city": "Stuttgart",
      "postal_code": "70327",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.766521",
        "longitude": "9.250781"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "7983244",
          "id": "DE*STR*E10256*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "309495927",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7983245",
          "id": "DE*STR*E10256*002",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "309495928",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "2309907",
      "name": "Kesselstr. Ggü. 21 (LS2) LADE/ 761-N-06",
      "status": "active",
      "address": "Kesselstr. 21",
      "city": "Stuttgart",
      "postal_code": "70327",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.766563",
        "longitude": "9.250751"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "7983249",
          "id": "DE*STR*E10257*001",
          "status": "CHARGING",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "309495932",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7983250",
          "id": "DE*STR*E10257*002",
          "status": "CHARGING",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "309495933",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "2309909",
      "name": "Ruiter Straße 9/1 / LADE 361-N-06",
      "status": "active",
      "address": "Ruiter Str. 9/1",
      "city": "Stuttgart",
      "postal_code": "70329",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.756817",
        "longitude": "9.255856"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "7983251",
          "id": "DE*STR*E10255*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "309495934",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7983252",
          "id": "DE*STR*E10255*002",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "309495935",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "2309918",
      "name": "Blautopfstraße 21 / LADE 521-N-04",
      "status": "active",
      "address": "Blautopfstr. 21",
      "city": "Stuttgart",
      "postal_code": "70329",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.766540",
        "longitude": "9.268136"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "7983262",
          "id": "DE*STR*E10096*001",
          "status": "CHARGING",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "309495952",
              "status": "CHARGING",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "7983274",
          "id": "DE*STR*E10096*002",
          "status": "AVAILABLE",
          "reservable": True,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE",
            "RESERVABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "309495953",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    },
    {
      "id": "2496317",
      "name": "MTV Stuttgart Furtwänglerstr.",
      "status": "active",
      "address": "Furtwänglerstr. 145",
      "city": "Stuttgart",
      "postal_code": "70195",
      "country": "DE",
      "directions": "",
      "comment": "",
      "coordinates": {
        "latitude": "48.786602",
        "longitude": "9.132960"
      },
      "distance_in_m": "0",
      "operator": {
        "operatorId": "STR",
        "name": "Stadtwerke Stuttgart GmbH",
        "hotline": "+49711346501212"
      },
      "opening_times": {
        "twentyfourseven": True
      },
      "owner": None,
      "roaming": False,
      "evses": [
        {
          "uid": "8453403",
          "id": "DE*STR*E2533081*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "327200043",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "8453404",
          "id": "DE*STR*E2533081*002",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "327200044",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "8453405",
          "id": "DE*STR*E2533082*001",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "327200045",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        },
        {
          "uid": "8453406",
          "id": "DE*STR*E2533082*002",
          "status": "AVAILABLE",
          "reservable": False,
          "capabilities": [
            "RFID_READER",
            "REMOTE_START_STOP_CAPABLE"
          ],
          "physical_reference": "",
          "floor_level": "",
          "vehicle_type": "four_wheeled",
          "chargePointPosition": None,
          "chargePointPublicComment": None,
          "chargePointParkingSpaceNumbers": None,
          "chargingStationPosition": None,
          "roaming": False,
          "connectors": [
            {
              "id": "327200046",
              "status": "AVAILABLE",
              "standard": "IEC_62196_T2",
              "format": "SOCKET",
              "power_type": "AC_3_PHASE",
              "ampere": "32",
              "voltage": "400",
              "max_power": 22,
              "tariff_id": None
            }
          ]
        }
      ],
      "tariffZones": [
        "2848"
      ]
    }
  ],
  "status_code": 1000,
  "status_message": "Success",
  "timestamp": "2024-10-23T13:16:09+02:00"
}