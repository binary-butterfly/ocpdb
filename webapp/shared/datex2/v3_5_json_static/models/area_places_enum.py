"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class AreaPlacesEnum(Enum):
    ATBORDERS = 'atBorders'
    ATHIGHALTITUDES = 'atHighAltitudes'
    INBUILTUPAREAS = 'inBuiltUpAreas'
    INFORESTEDAREAS = 'inForestedAreas'
    INGALLERIES = 'inGalleries'
    INLOWLYINGAREAS = 'inLowLyingAreas'
    INRURALAREAS = 'inRuralAreas'
    INSHADEDAREAS = 'inShadedAreas'
    INTHEINNERCITYAREAS = 'inTheInnerCityAreas'
    INTUNNELS = 'inTunnels'
    ONBRIDGES = 'onBridges'
    ONDOWNHILLSECTIONS = 'onDownhillSections'
    ONELEVATEDSECTIONS = 'onElevatedSections'
    ONENTERINGORLEAVINGTUNNELS = 'onEnteringOrLeavingTunnels'
    ONFLYOVERS = 'onFlyovers'
    ONPASSES = 'onPasses'
    ONUNDERGROUNDSECTIONS = 'onUndergroundSections'
    ONUNDERPASSES = 'onUnderpasses'
    EXTENDEDG = 'extendedG'
