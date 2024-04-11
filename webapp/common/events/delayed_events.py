"""
Giro-e OCPI
Copyright (c) 2021, binary butterfly GmbH
All rights reserved.
"""

from webapp.extensions import celery
from .enum import EventSource, EventType


@celery.task
def trigger_delayed_event(event_type_str, event_source_str, event_id: int, **kwargs):
    from webapp.dependencies import dependencies
    dependencies.get_event_helper().trigger_async(
        event_type=EventType[event_type_str],
        event_source=EventSource[event_source_str],
        event_id=event_id,
        **kwargs,
    )
