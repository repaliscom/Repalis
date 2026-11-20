from datetime import timedelta

import pytest

from repalis.exceptions import Unauthorized
from repalis.integrations.discord.endpoints import get_decoded_token_state
from repalis.kit import jwt
from repalis.kit.utils import utc_now


@pytest.mark.anyio
class TestGetDecodedTokenState:
    async def test_expired_state_raises_unauthorized(self) -> None:
        expired_state = await jwt.encode(
            data={"auth_type": "bot", "return_to": "/"},
            type="discord_oauth",
            expires_at=utc_now() - timedelta(minutes=1),
        )

        with pytest.raises(Unauthorized):
            await get_decoded_token_state(expired_state)
