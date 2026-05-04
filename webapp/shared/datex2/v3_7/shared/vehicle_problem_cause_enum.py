"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class VehicleProblemCauseEnum(Enum):
    AIRSYSTEM = 'airSystem'
    BATTERY = 'battery'
    BRAKINGSYSTEM = 'brakingSystem'
    COOLINGSYSTEM = 'coolingSystem'
    DECOUPLEDTRAILER = 'decoupledTrailer'
    DIVERPROBLEM = 'diverProblem'
    ELECTRICALSYSTEM = 'electricalSystem'
    FLATTYRE = 'flatTyre'
    FUELSYSTEM = 'fuelSystem'
    GEAR = 'gear'
    LOADPROBLEM = 'loadProblem'
    LOSTWHEEL = 'lostWheel'
    MOTORMECHANICS = 'motorMechanics'
    OILLEAKAGE = 'oilLeakage'
    SUSPENSION = 'suspension'
    OTHER = 'other'
    UNKNOWN = 'unknown'
    EXTENDEDG = 'extendedG'
