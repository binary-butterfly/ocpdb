"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class AltitudeAccuracyEnum(Enum):
    EQUALTOORLESSTHAN1CENTIMETRE = 'equalToOrLessThan1Centimetre'
    EQUALTOORLESSTHAN2CENTIMETRES = 'equalToOrLessThan2Centimetres'
    EQUALTOORLESSTHAN5CENTIMETRES = 'equalToOrLessThan5Centimetres'
    EQUALTOORLESSTHAN10CENTIMETRES = 'equalToOrLessThan10Centimetres'
    EQUALTOORLESSTHAN20CENTIMETRES = 'equalToOrLessThan20Centimetres'
    EQUALTOORLESSTHAN50CENTIMETRES = 'equalToOrLessThan50Centimetres'
    EQUALTOORLESSTHAN1METRE = 'equalToOrLessThan1Metre'
    EQUALTOORLESSTHAN2METRES = 'equalToOrLessThan2Metres'
    EQUALTOORLESSTHAN5METRES = 'equalToOrLessThan5Metres'
    EQUALTOORLESSTHAN10METRES = 'equalToOrLessThan10Metres'
    EQUALTOORLESSTHAN20METRES = 'equalToOrLessThan20Metres'
    EQUALTOORLESSTHAN50METRES = 'equalToOrLessThan50Metres'
    EQUALTOORLESSTHAN100METRES = 'equalToOrLessThan100Metres'
    EQUALTOORLESSTHAN200METRES = 'equalToOrLessThan200Metres'
    EXTENDEDG = 'extendedG'
