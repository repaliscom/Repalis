import uuid
from typing import Annotated

import sentry_sdk

from repalis.dispute.service import DisputeAlertTransactionNotLinkedError
from repalis.dispute.service import dispute as dispute_service
from repalis.external_event.service import external_event as external_event_service
from repalis.models.external_event import ExternalEventSource
from repalis.observability.task_logging import LoggableField
from repalis.worker import AsyncSessionMaker, TaskPriority, actor


@actor(
    actor_name="chargeback_stop.webhook.alert.created",
    priority=TaskPriority.HIGH,
)
async def alert_created(event_id: Annotated[uuid.UUID, LoggableField]) -> None:
    async with AsyncSessionMaker() as session:
        async with external_event_service.handle(
            session, ExternalEventSource.chargeback_stop, event_id
        ) as event:
            try:
                await dispute_service.upsert_from_chargeback_stop(
                    session, event.data["data"]["object"]
                )
            except DisputeAlertTransactionNotLinkedError as e:
                sentry_sdk.capture_exception(e)


@actor(
    actor_name="chargeback_stop.webhook.alert.updated",
    priority=TaskPriority.HIGH,
)
async def alert_updated(event_id: Annotated[uuid.UUID, LoggableField]) -> None:
    async with AsyncSessionMaker() as session:
        async with external_event_service.handle(
            session, ExternalEventSource.chargeback_stop, event_id
        ) as event:
            try:
                await dispute_service.upsert_from_chargeback_stop(
                    session, event.data["data"]["object"]
                )
            except DisputeAlertTransactionNotLinkedError as e:
                sentry_sdk.capture_exception(e)
