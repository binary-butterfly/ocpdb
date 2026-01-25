"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class MeansOfPaymentEnum(Enum):
    PAYMENTCREDITCARD = 'paymentCreditCard'
    CASHBILLSONLY = 'cashBillsOnly'
    CASHCOINSONLY = 'cashCoinsOnly'
    TOLLTAG = 'tollTag'
    MOBILEACCOUNT = 'mobileAccount'
    CASHCOINSANDBILLS = 'cashCoinsAndBills'
    PREPAY = 'prepay'
    PAYMENTDEBITCARD = 'paymentDebitCard'
    PAYMENTVALUECARD = 'paymentValueCard'
    NFC = 'nfc'
    EMV = 'emv'
    QRCODE = 'qrCode'
    WEBSITE = 'website'
    UNKNOWN = 'unknown'
    EXTENDEDG = 'extendedG'
