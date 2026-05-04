"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class MeasuredOrDerivedDataTypeEnum(Enum):
    HUMIDITYINFORMATION = 'humidityInformation'
    INDIVIDUALVEHICLEMEASUREMENTS = 'individualVehicleMeasurements'
    POLLUTIONINFORMATION = 'pollutionInformation'
    PRECIPITATIONINFORMATION = 'precipitationInformation'
    PRESSUREINFORMATION = 'pressureInformation'
    ROADSURFACECONDITIONINFORMATION = 'roadSurfaceConditionInformation'
    TEMPERATUREINFORMATION = 'temperatureInformation'
    TRAFFICCONCENTRATION = 'trafficConcentration'
    TRAFFICFLOW = 'trafficFlow'
    TRAFFICGAP = 'trafficGap'
    TRAFFICHEADWAY = 'trafficHeadway'
    TRAFFICSPEED = 'trafficSpeed'
    TRAFFICSTATUSINFORMATION = 'trafficStatusInformation'
    TRAVELTIMEINFORMATION = 'travelTimeInformation'
    VISIBILITYINFORMATION = 'visibilityInformation'
    WINDINFORMATION = 'windInformation'
    EXTENDEDG = 'extendedG'
