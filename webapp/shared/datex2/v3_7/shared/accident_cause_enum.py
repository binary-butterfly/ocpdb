"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class AccidentCauseEnum(Enum):
    AVOIDANCEOFOBSTACLES = 'avoidanceOfObstacles'
    DRIVERDISTRACTION = 'driverDistraction'
    DRIVERDRUGABUSE = 'driverDrugAbuse'
    DRIVERILLNESS = 'driverIllness'
    EXCEEDINGSPEEDSLIMITS = 'exceedingSpeedsLimits'
    EXCESSALCOHOL = 'excessAlcohol'
    EXCESSIVEDRIVERTIREDNESS = 'excessiveDriverTiredness'
    IMPERMISSIBLEMANOEUVRE = 'impermissibleManoeuvre'
    LIMITEDVISIBILITY = 'limitedVisibility'
    NOTKEEPINGASAFEDISTANCE = 'notKeepingASafeDistance'
    ONTHEWRONGSIDEOFTHEROAD = 'onTheWrongSideOfTheRoad'
    PEDESTRIANINROAD = 'pedestrianInRoad'
    POORLANEADHERENCE = 'poorLaneAdherence'
    POORMERGEENTRYOREXITJUDGEMENT = 'poorMergeEntryOrExitJudgement'
    POORROADSURFACECONDITION = 'poorRoadSurfaceCondition'
    POORSURFACEADHERENCE = 'poorSurfaceAdherence'
    UNDISCLOSED = 'undisclosed'
    UNKNOWN = 'unknown'
    VEHICLEFAILURE = 'vehicleFailure'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
