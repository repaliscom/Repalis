from repalis.base import RepalisError


class RepalisOutpostError(RepalisError): ...


class NotReadyError(RepalisOutpostError):
    """A read Outpost cannot answer yet: Repalis has not sent the customer's snapshot
    in time."""


class UnavailableRedisError(RepalisOutpostError):
    def __init__(self) -> None:
        super().__init__("Redis is unavailable")


class MissingExternalIdError(RepalisOutpostError):
    def __init__(self) -> None:
        super().__init__("Outpost needs an external_id on every event")
