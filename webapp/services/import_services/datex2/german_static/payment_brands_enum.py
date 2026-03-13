"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class PaymentBrandsEnum(Enum):
    AMERICANEXPRESS = 'americanExpress'
    APPLEPAY = 'applePay'
    CIRRUS = 'cirrus'
    DINERSCLUB = 'dinersClub'
    DISCOVERCARD = 'discoverCard'
    GIROCARD = 'giroCard'
    MAESTRO = 'maestro'
    MASTERCARD = 'masterCard'
    VISA = 'visa'
    VPAY = 'vpay'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
