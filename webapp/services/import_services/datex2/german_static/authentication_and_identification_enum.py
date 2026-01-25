"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class AuthenticationAndIdentificationEnum(Enum):
    ACTIVERFIDCHIP = 'activeRFIDChip'
    APPS = 'apps'
    CALYPSO = 'calypso'
    CASHPAYMENT = 'cashPayment'
    CREDITCARD = 'creditCard'
    DEBITCARD = 'debitCard'
    MIFARECLASSIC = 'mifareClassic'
    MIFAREDESFIRE = 'mifareDesfire'
    NFC = 'nfc'
    OVERTHEAIR = 'overTheAir'
    PHONEDIALOG = 'phoneDialog'
    PHONESMS = 'phoneSMS'
    PINPAD = 'pinpad'
    PLC = 'plc'
    PREPAIDCARD = 'prepaidCard'
    RFID = 'rfid'
    WEBSITE = 'website'
    UNLIMITEDACCESS = 'unlimitedAccess'
    NOACCESS = 'noAccess'
    EXTENDEDG = 'extendedG'
