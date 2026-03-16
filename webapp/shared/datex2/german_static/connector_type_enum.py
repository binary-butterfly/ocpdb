"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class ConnectorTypeEnum(Enum):
    CEE3 = 'cee3'
    CEE5 = 'cee5'
    CHADEMO = 'chademo'
    YAZAKI = 'yazaki'
    DOMESTIC = 'domestic'
    DOMESTICA = 'domesticA'
    DOMESTICB = 'domesticB'
    DOMESTICC = 'domesticC'
    DOMESTICD = 'domesticD'
    DOMESTICE = 'domesticE'
    DOMESTICF = 'domesticF'
    DOMESTICG = 'domesticG'
    DOMESTICH = 'domesticH'
    DOMESTICI = 'domesticI'
    DOMESTICJ = 'domesticJ'
    DOMESTICK = 'domesticK'
    DOMESTICL = 'domesticL'
    DOMESTICM = 'domesticM'
    DOMESTICN = 'domesticN'
    DOMESTICO = 'domesticO'
    IEC60309X2THREE16 = 'iec60309x2three16'
    IEC60309X2THREE32 = 'iec60309x2three32'
    IEC60309X2THREE64 = 'iec60309x2three64'
    IEC60309X2SINGLE16 = 'iec60309x2single16'
    IEC62196T1 = 'iec62196T1'
    IEC62196T1COMBO = 'iec62196T1COMBO'
    IEC62196T2 = 'iec62196T2'
    IEC62196T2COMBO = 'iec62196T2COMBO'
    IEC62196T3A = 'iec62196T3A'
    IEC62196T3C = 'iec62196T3C'
    MCS = 'mcs'
    PANTOGRAPHBOTTOMUP = 'pantographBottomUp'
    PANTOGRAPHTOPDOWN = 'pantographTopDown'
    TESLACONNECTOREUROPE = 'teslaConnectorEurope'
    TESLACONNECTORAMERICA = 'teslaConnectorAmerica'
    TESLAR = 'teslaR'
    TESLAS = 'teslaS'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
