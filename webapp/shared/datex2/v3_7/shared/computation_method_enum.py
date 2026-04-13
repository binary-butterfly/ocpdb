"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class ComputationMethodEnum(Enum):
    ARITHMETICAVERAGEOFSAMPLESBASEDONAFIXEDNUMBEROFSAMPLES = 'arithmeticAverageOfSamplesBasedOnAFixedNumberOfSamples'
    ARITHMETICAVERAGEOFSAMPLESINATIMEPERIOD = 'arithmeticAverageOfSamplesInATimePeriod'
    HARMONICAVERAGEOFSAMPLESINATIMEPERIOD = 'harmonicAverageOfSamplesInATimePeriod'
    MEDIANOFSAMPLESINATIMEPERIOD = 'medianOfSamplesInATimePeriod'
    MOVINGAVERAGEOFSAMPLES = 'movingAverageOfSamples'
    EXTENDEDG = 'extendedG'
