"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class SourceTypeEnum(Enum):
    AUTOMOBILECLUBPATROL = 'automobileClubPatrol'
    CAMERAOBSERVATION = 'cameraObservation'
    FREIGHTVEHICLEOPERATOR = 'freightVehicleOperator'
    INDUCTIONLOOPMONITORINGSTATION = 'inductionLoopMonitoringStation'
    INFRAREDMONITORINGSTATION = 'infraredMonitoringStation'
    MICROWAVEMONITORINGSTATION = 'microwaveMonitoringStation'
    MOBILETELEPHONECALLER = 'mobileTelephoneCaller'
    NONPOLICEEMERGENCYSERVICEPATROL = 'nonPoliceEmergencyServicePatrol'
    OTHERINFORMATION = 'otherInformation'
    OTHEROFFICIALVEHICLE = 'otherOfficialVehicle'
    POLICEPATROL = 'policePatrol'
    PRIVATEBREAKDOWNSERVICE = 'privateBreakdownService'
    PUBLICANDPRIVATEUTILITIES = 'publicAndPrivateUtilities'
    REGISTEREDMOTORISTOBSERVER = 'registeredMotoristObserver'
    ROADAUTHORITIES = 'roadAuthorities'
    ROADOPERATORPATROL = 'roadOperatorPatrol'
    ROADSIDETELEPHONECALLER = 'roadsideTelephoneCaller'
    SPOTTERAIRCRAFT = 'spotterAircraft'
    TRAFFICMONITORINGSTATION = 'trafficMonitoringStation'
    TRANSITOPERATOR = 'transitOperator'
    VEHICLEPROBEMEASUREMENT = 'vehicleProbeMeasurement'
    VIDEOPROCESSINGMONITORINGSTATION = 'videoProcessingMonitoringStation'
    EXTENDEDG = 'extendedG'
