"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class AuthorityOperationTypeEnum(Enum):
    ACCIDENTINVESTIGATIONWORK = 'accidentInvestigationWork'
    BOMBSQUADINACTION = 'bombSquadInAction'
    CIVILEMERGENCY = 'civilEmergency'
    CUSTOMSOPERATION = 'customsOperation'
    JURIDICALRECONSTRUCTION = 'juridicalReconstruction'
    POLICECHECKPOINT = 'policeCheckPoint'
    POLICEINVESTIGATION = 'policeInvestigation'
    ROADOPERATORCHECKPOINT = 'roadOperatorCheckPoint'
    SNOWCHAINONBOARDORSNOWTYRESMOUNTEDCHECK = 'snowChainOnBoardOrSnowTyresMountedCheck'
    SNOWCHAINORSNOWTYRESMOUNTEDCHECK = 'snowChainOrSnowTyresMountedCheck'
    SURVEY = 'survey'
    UNDEFINEDAUTHORITYACTIVITY = 'undefinedAuthorityActivity'
    TRANSPORTOFVIP = 'transportOfVip'
    VEHICLEINSPECTIONCHECKPOINT = 'vehicleInspectionCheckPoint'
    VEHICLEWEIGHING = 'vehicleWeighing'
    WEIGHINMOTION = 'weighInMotion'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
