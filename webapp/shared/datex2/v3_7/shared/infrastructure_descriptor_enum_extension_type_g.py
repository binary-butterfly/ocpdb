"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class InfrastructureDescriptorEnumExtensionTypeG(Enum):
    INBICYCLEUNDERPASS = 'inBicycleUnderpass'
    INNONVEHICULARUNDERPASS = 'inNonVehicularUnderpass'
    INPEDESTRIANUNDERPASS = 'inPedestrianUnderpass'
    ONBICYCLEBRIDGE = 'onBicycleBridge'
    ONBICYCLECROSSING = 'onBicycleCrossing'
    ONFOOTBRIDGE = 'onFootBridge'
    ONGUIDEDBUSWAYCROSSING = 'onGuidedBusWayCrossing'
    ONHORSECROSSING = 'onHorseCrossing'
    ONLIGHTRAILCROSSING = 'onLightRailCrossing'
    ONMIXEDUSECROSSING = 'onMixedUseCrossing'
    ONNONVEHICULARBRIDGE = 'onNonVehicularBridge'
    ONPEDESTRIANCROSSING = 'onPedestrianCrossing'
    ONTRAMCROSSING = 'onTramCrossing'
