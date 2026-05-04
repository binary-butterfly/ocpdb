"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class VehicleObstructionTypeEnum(Enum):
    ABANDONEDVEHICLE = 'abandonedVehicle'
    ABNORMALLOAD = 'abnormalLoad'
    BROKENDOWNVEHICLE = 'brokenDownVehicle'
    CONVOY = 'convoy'
    DAMAGEDVEHICLE = 'damagedVehicle'
    DANGEROUSSLOWMOVINGVEHICLE = 'dangerousSlowMovingVehicle'
    EMERGENCYVEHICLE = 'emergencyVehicle'
    HIGHSPEEDEMERGENCYVEHICLE = 'highSpeedEmergencyVehicle'
    LONGLOAD = 'longLoad'
    HIGHSPEEDCHASE = 'highSpeedChase'
    MEDICALEMERGENCY = 'medicalEmergency'
    MILITARYCONVOY = 'militaryConvoy'
    OVERHEIGHTVEHICLE = 'overheightVehicle'
    PROHIBITEDVEHICLEONTHEROAD = 'prohibitedVehicleOnTheRoad'
    RECKLESSDRIVER = 'recklessDriver'
    SLOWVEHICLE = 'slowVehicle'
    SPECIALPERMITTRANSPORT = 'specialPermitTransport'
    TRACKEDVEHICLE = 'trackedVehicle'
    UNLITVEHICLEONTHEROAD = 'unlitVehicleOnTheRoad'
    VEHICLEONFIRE = 'vehicleOnFire'
    VEHICLECARRYINGHAZARDOUSMATERIALS = 'vehicleCarryingHazardousMaterials'
    VEHICLEINDIFFICULTY = 'vehicleInDifficulty'
    VEHICLEONWRONGCARRIAGEWAY = 'vehicleOnWrongCarriageway'
    VEHICLESTUCK = 'vehicleStuck'
    VEHICLEWITHOVERHEIGHTLOAD = 'vehicleWithOverheightLoad'
    VEHICLEWITHOVERWIDELOAD = 'vehicleWithOverwideLoad'
    WINTERMAINTETANCEVEHICLEINTRANSFER = 'winterMaintetanceVehicleInTransfer'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
