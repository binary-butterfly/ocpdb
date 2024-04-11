"""
Giro-e OCPI
Copyright (c) 2024, binary butterfly GmbH
All rights reserved.
"""

from abc import ABC, abstractmethod

from webapp.services.base_service import BaseService


class PubSubBaseHandler(BaseService, ABC):

    @abstractmethod
    def handle(self, object_uid: str, value: str):
        pass
