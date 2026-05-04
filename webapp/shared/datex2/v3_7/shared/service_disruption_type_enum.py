"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class ServiceDisruptionTypeEnum(Enum):
    BARCLOSED = 'barClosed'
    DIESELSHORTAGE = 'dieselShortage'
    FUELSHORTAGE = 'fuelShortage'
    LPGSHORTAGE = 'lpgShortage'
    METHANESHORTAGE = 'methaneShortage'
    NODIESELFORHEAVYVEHICLES = 'noDieselForHeavyVehicles'
    NODIESELFORLIGHTVEHICLES = 'noDieselForLightVehicles'
    NOPARKINGAVAILABILITY = 'noParkingAvailability'
    NOPUBLICTELEPHONES = 'noPublicTelephones'
    NOTOILETFACILITIES = 'noToiletFacilities'
    NOVEHICLEREPAIRFACILITIES = 'noVehicleRepairFacilities'
    PETROLSHORTAGE = 'petrolShortage'
    RESTAREABUSY = 'restAreaBusy'
    RESTAREACLOSED = 'restAreaClosed'
    RESTAREAOVERCROWDEDDRIVETOANOTHERRESTAREA = 'restAreaOvercrowdedDriveToAnotherRestArea'
    SERVICEAREABUSY = 'serviceAreaBusy'
    SERVICEAREACLOSED = 'serviceAreaClosed'
    SERVICEAREAFUELSTATIONCLOSED = 'serviceAreaFuelStationClosed'
    SERVICEAREAOVERCROWDEDDRIVETOANOTHERSERVICEAREA = 'serviceAreaOvercrowdedDriveToAnotherServiceArea'
    SERVICEAREARESTAURANTCLOSED = 'serviceAreaRestaurantClosed'
    SOMECOMMERCIALSERVICESCLOSED = 'someCommercialServicesClosed'
    WATERSHORTAGE = 'waterShortage'
    EXTENDEDG = 'extendedG'
