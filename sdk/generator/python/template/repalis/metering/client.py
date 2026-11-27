import typing

from repalis.base import AsyncClientBase
from repalis.metering.events import EventInput


class EventsClient(typing.Protocol):
    async def ingest(self, *, events: list[EventInput]) -> object: ...


class MeteringClient(typing.Protocol):
    @property
    def events(self) -> EventsClient: ...


class RepalisClient(MeteringClient, typing.Protocol):
    @property
    def _client(self) -> AsyncClientBase: ...
