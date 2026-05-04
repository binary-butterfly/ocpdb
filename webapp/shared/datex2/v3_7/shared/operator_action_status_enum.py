"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class OperatorActionStatusEnum(Enum):
    REQUESTED = 'requested'
    APPROVED = 'approved'
    BEINGIMPLEMENTED = 'beingImplemented'
    IMPLEMENTED = 'implemented'
    REJECTED = 'rejected'
    TERMINATIONREQUESTED = 'terminationRequested'
    BEINGTERMINATED = 'beingTerminated'
    EXTENDEDG = 'extendedG'
