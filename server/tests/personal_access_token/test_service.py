from datetime import timedelta
from unittest.mock import MagicMock

import pytest
from pytest_mock import MockerFixture

from repalis.email.schemas import PersonalAccessTokenLeakedEmail
from repalis.enums import TokenType
from repalis.kit.crypto import get_token_hash
from repalis.kit.utils import utc_now
from repalis.models import PersonalAccessToken, User
from repalis.personal_access_token.service import (
    personal_access_token as personal_access_token_service,
)
from repalis.postgres import AsyncSession
from tests.fixtures.database import SaveFixture


@pytest.fixture(autouse=True)
def enqueue_email_mock(mocker: MockerFixture) -> MagicMock:
    return mocker.patch(
        "repalis.personal_access_token.service.enqueue_email_template", autospec=True
    )


@pytest.mark.anyio
class TestRevokeLeaked:
    async def test_false_positive(
        self, session: AsyncSession, enqueue_email_mock: MagicMock
    ) -> None:
        result = await personal_access_token_service.revoke_leaked(
            session,
            "repalis_pat_123",
            TokenType.personal_access_token,
            notifier="github",
            url="https://github.com",
        )
        assert result is False

        enqueue_email_mock.assert_not_called()

    async def test_true_positive(
        self,
        save_fixture: SaveFixture,
        session: AsyncSession,
        user: User,
        mocker: MockerFixture,
        enqueue_email_mock: MagicMock,
    ) -> None:
        token_hash = get_token_hash("repalis_pat_123")
        personal_access_token = PersonalAccessToken(
            comment="Test",
            token=token_hash,
            user_id=user.id,
            expires_at=utc_now() + timedelta(days=1),
            scope="openid",
        )
        await save_fixture(personal_access_token)

        result = await personal_access_token_service.revoke_leaked(
            session,
            "repalis_pat_123",
            TokenType.personal_access_token,
            notifier="github",
            url="https://github.com",
        )
        assert result is True

        updated_personal_access_token = await session.get(
            PersonalAccessToken, personal_access_token.id
        )
        assert updated_personal_access_token is not None
        assert updated_personal_access_token.deleted_at is not None

        enqueue_email_mock.assert_called_once()
        assert isinstance(
            enqueue_email_mock.call_args[0][0], PersonalAccessTokenLeakedEmail
        )
