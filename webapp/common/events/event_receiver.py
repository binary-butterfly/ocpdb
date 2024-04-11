"""
Giro-e OCPI
Copyright (c) 2022, binary butterfly GmbH
All rights reserved.
"""

from typing import Optional, List
from abc import ABC, abstractmethod
from .enum import EventSource, EventType


class EventReceiver(ABC):
    """
    This class is the entrypoint for a event. Usually it initializes a service class with all its dependencies and
    runs the desired method.
    """

    delay_seconds: Optional[int] = None
    listen_to_event_source: Optional[EventSource] = None

    @property
    @abstractmethod
    def listen_to_event_types(self) -> List[EventType]:
        pass

    @property
    @abstractmethod
    def required_parameters(self) -> List[str]:
        pass

    @abstractmethod
    def run(self, event_source: EventSource, data: dict):
        pass
