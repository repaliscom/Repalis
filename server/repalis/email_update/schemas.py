from pydantic import field_validator

from repalis.kit.email import EmailStrDNS
from repalis.kit.http import get_safe_return_url
from repalis.kit.schemas import Schema


class EmailUpdateRequest(Schema):
    email: EmailStrDNS
    return_to: str | None = None

    @field_validator("return_to")
    @classmethod
    def validate_return_to(cls, v: str | None) -> str:
        return get_safe_return_url(v)
