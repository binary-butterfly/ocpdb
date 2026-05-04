"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class TransitServiceInformationEnum(Enum):
    CANCELLATIONS = 'cancellations'
    DELAYDUETOBADWEATHER = 'delayDueToBadWeather'
    DELAYDUETOREPAIRS = 'delayDueToRepairs'
    DELAYEDUNTILFURTHERNOTICE = 'delayedUntilFurtherNotice'
    DELAYSDUETOFLOTSAM = 'delaysDueToFlotsam'
    DEPARTUREONSCHEDULE = 'departureOnSchedule'
    FERRYREPLACEDBYICEROAD = 'ferryReplacedByIceRoad'
    FREESHUTTLESERVICEOPERATING = 'freeShuttleServiceOperating'
    INFORMATIONSERVICENOTAVAILABLE = 'informationServiceNotAvailable'
    IRREGULARSERVICEDELAYS = 'irregularServiceDelays'
    LOADCAPACITYCHANGED = 'loadCapacityChanged'
    RESTRICTIONSFORLONGERVEHICLES = 'restrictionsForLongerVehicles'
    SERVICEDELAYS = 'serviceDelays'
    SERVICEDELAYSOFUNCERTAINDURATION = 'serviceDelaysOfUncertainDuration'
    SERVICEFULLYBOOKED = 'serviceFullyBooked'
    SERVICENOTOPERATING = 'serviceNotOperating'
    SERVICENOTOPERATINGSUBSTITUTESERVICEAVAILABLE = 'serviceNotOperatingSubstituteServiceAvailable'
    SERVICESUSPENDED = 'serviceSuspended'
    SERVICEWITHDRAWN = 'serviceWithdrawn'
    SHUTTLESERVICEOPERATING = 'shuttleServiceOperating'
    TEMPORARYCHANGESTOTIMETABLES = 'temporaryChangesToTimetables'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
