"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class ReasonForRegulationEnum(Enum):
    OTHER = 'other'
    PROTECTIONOFNOISEANDEMISSIONS = 'protectionOfNoiseAndEmissions'
    PROTECTIONOFROAD = 'protectionOfRoad'
    PROTECTIONOFWATERS = 'protectionOfWaters'
    PUBLICSAFETY = 'publicSafety'
    RESEARCHANDTEST = 'researchAndTest'
    ROADWORKS = 'roadworks'
    TRAFFICORDER = 'trafficOrder'
    TRAFFICSAFETY = 'trafficSafety'
    EXTENDEDG = 'extendedG'
