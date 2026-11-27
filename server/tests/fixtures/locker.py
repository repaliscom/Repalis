import pytest

from repalis.locker import Locker
from repalis.redis import Redis


@pytest.fixture
async def locker(redis: Redis) -> Locker:
    return Locker(redis)
