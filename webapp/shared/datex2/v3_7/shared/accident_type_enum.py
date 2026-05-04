"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class AccidentTypeEnum(Enum):
    ACCIDENT = 'accident'
    ACCIDENTINVOLVINGHAZARDOUSMATERIALS = 'accidentInvolvingHazardousMaterials'
    ACCIDENTINVOLVINGHEAVYLORRIES = 'accidentInvolvingHeavyLorries'
    ACCIDENTINVOLVINGMASSTRANSITVEHICLE = 'accidentInvolvingMassTransitVehicle'
    ACCIDENTINVOLVINGPUBLICTRANSPORT = 'accidentInvolvingPublicTransport'
    ACCIDENTINVOLVINGRADIOACTIVEMATERIAL = 'accidentInvolvingRadioactiveMaterial'
    ACCIDENTINVOLVINGTRAIN = 'accidentInvolvingTrain'
    COLLISION = 'collision'
    MULTIPLEVEHICLEACCIDENT = 'multipleVehicleAccident'
    SECONDARYACCIDENT = 'secondaryAccident'
    SERIOUSINJURYORFATALACCIDENT = 'seriousInjuryOrFatalAccident'
    VEHICLESTUCKUNDERBRIDGE = 'vehicleStuckUnderBridge'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
