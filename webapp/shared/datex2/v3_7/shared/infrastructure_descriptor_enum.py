"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class InfrastructureDescriptorEnum(Enum):
    ATMOTORWAYINTERCHANGE = 'atMotorwayInterchange'
    ATRESTAREA = 'atRestArea'
    ATSERVICEAREA = 'atServiceArea'
    ATTOLLPLAZA = 'atTollPlaza'
    ATTUNNELENTRYOREXIT = 'atTunnelEntryOrExit'
    INGALLERY = 'inGallery'
    INTUNNEL = 'inTunnel'
    ONBRIDGE = 'onBridge'
    ONCONNECTOR = 'onConnector'
    ONELEVATEDSECTION = 'onElevatedSection'
    ONFLYOVER = 'onFlyover'
    ONICEROAD = 'onIceRoad'
    ONLEVELCROSSING = 'onLevelCrossing'
    ONLINKROAD = 'onLinkRoad'
    ONROUNDABOUT = 'onRoundabout'
    ONTHEROADWAY = 'onTheRoadway'
    ONUNDERGROUNDSECTION = 'onUndergroundSection'
    ONUNDERPASS = 'onUnderpass'
    WITHINJUNCTION = 'withinJunction'
    EXTENDEDG = 'extendedG'
