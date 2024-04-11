"""
Giro-e OCPI
Copyright (c) 2021, binary butterfly GmbH
All rights reserved.
"""

from dataclasses import dataclass
from typing import Optional
from .enum import EventType, EventSource


@dataclass
class Event:
    type: EventType
    source: EventSource
    data: Optional[dict] = None
