"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class CredentialTypeEnum(Enum):
    HANGTAG = 'hangtag'
    PERMIT = 'permit'
    LICENSEPLATE = 'licensePlate'
    TICKET = 'ticket'
    ETICKET = 'eticket'
    BARCODE = 'barcode'
    BLUETOOTH = 'bluetooth'
    RFID = 'rfid'
    QRCODE = 'qrCode'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
