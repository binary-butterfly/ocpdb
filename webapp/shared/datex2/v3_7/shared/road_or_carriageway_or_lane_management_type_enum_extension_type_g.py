"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class RoadOrCarriagewayOrLaneManagementTypeEnumExtensionTypeG(Enum):
    CREATEONEDIRECTIONWAY = 'createOneDirectionWay'
    CREATETWODIRECTIONWAY = 'createTwoDirectionWay'
    LANEINOPERATION = 'laneInOperation'
    LANEMOVED = 'laneMoved'
    LANENOTINOPERATION = 'laneNotInOperation'
    LANERESTRICTIONINOPERATION = 'laneRestrictionInOperation'
    PARKINGPROHIBITIONINOPERATION = 'parkingProhibitionInOperation'
    REVERSETRAFFICDIRECTION = 'reverseTrafficDirection'
    WAITINGPROHIBITIONINOPERATION = 'waitingProhibitionInOperation'
