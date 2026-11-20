from math import ceil
from urllib.parse import urlencode

from sqlalchemy import delete

from repalis.auth.models import AuthSubject
from repalis.email.schemas import EmailUpdateEmail, EmailUpdateProps
from repalis.email.sender import enqueue_email_template
from repalis.exceptions import RepalisError, RepalisRequestValidationError
from repalis.integrations.resend.service import resend as resend_service
from repalis.kit.crypto import generate_token_hash_pair
from repalis.kit.services import ResourceServiceReader
from repalis.kit.utils import utc_now
from repalis.models import EmailVerification
from repalis.models.user import User
from repalis.postgres import AsyncSession
from repalis.user.repository import UserRepository

from .repository import EmailVerificationRepository

TOKEN_PREFIX = "repalis_ev_"


class EmailUpdateError(RepalisError): ...


class InvalidEmailUpdate(EmailUpdateError):
    def __init__(self) -> None:
        super().__init__(
            "This email update request is invalid or has expired.", status_code=401
        )


class EmailAlreadyInUse(EmailUpdateError):
    def __init__(self) -> None:
        super().__init__("Another user is already using this email.", status_code=409)


class EmailUpdateService(ResourceServiceReader[EmailVerification]):
    async def request_email_update(
        self,
        email: str,
        session: AsyncSession,
        auth_subject: AuthSubject[User],
    ) -> tuple[EmailVerification, str]:
        user = auth_subject.subject

        user_repository = UserRepository.from_session(session)
        existing_user = await user_repository.get_by_email(email)
        if existing_user is not None and existing_user.id != user.id:
            raise RepalisRequestValidationError(
                [
                    {
                        "type": "value_error",
                        "loc": ("body", "email"),
                        "msg": "Another user is already using this email.",
                        "input": email,
                    }
                ]
            )

        repository = EmailVerificationRepository.from_session(session)
        await repository.delete_by_user_id(user.id)

        token, token_hash = generate_token_hash_pair(prefix=TOKEN_PREFIX)
        email_update_record = EmailVerification(
            email=email, token_hash=token_hash, user=user
        )

        session.add(email_update_record)
        await session.flush()

        return email_update_record, token

    async def send_email(
        self,
        email_update_record: EmailVerification,
        token: str,
        base_url: str,
        *,
        extra_url_params: dict[str, str] | None = None,
    ) -> None:
        if extra_url_params is None:
            extra_url_params = {}
        delta = email_update_record.expires_at - utc_now()
        token_lifetime_minutes = ceil(delta.seconds / 60)

        email = email_update_record.email
        url_params = {"token": token, **extra_url_params}
        enqueue_email_template(
            EmailUpdateEmail(
                props=EmailUpdateProps(
                    email=email,
                    token_lifetime_minutes=token_lifetime_minutes,
                    url=f"{base_url}?{urlencode(url_params)}",
                )
            ),
            to_email_addr=email,
            subject="Update your email",
            unsuppress=True,
        )

    async def verify(self, session: AsyncSession, token: str, user: User) -> User:
        repository = EmailVerificationRepository.from_session(session)
        email_update_record = await repository.get_by_token(token)

        if email_update_record is None or email_update_record.user_id != user.id:
            raise InvalidEmailUpdate()

        # The email may have been taken since the update was requested.
        # Include deleted and blocked users: the unique index covers every row.
        user_repository = UserRepository.from_session(session)
        existing_user = await user_repository.get_by_email(
            email_update_record.email, include_deleted=True, included_blocked=True
        )
        if existing_user is not None and existing_user.id != user.id:
            raise EmailAlreadyInUse()

        user = email_update_record.user
        previous_email = user.email
        user.email = email_update_record.email
        user.email_verified = True
        session.add(user)

        await session.delete(email_update_record)

        resend_service.enqueue_sync_user(user.id, previous_email=previous_email)

        return user

    async def delete_expired_record(self, session: AsyncSession) -> None:
        statement = delete(EmailVerification).where(
            EmailVerification.expires_at < utc_now()
        )
        await session.execute(statement)
        await session.flush()


email_update = EmailUpdateService(EmailVerification)
