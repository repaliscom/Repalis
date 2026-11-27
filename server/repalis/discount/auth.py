from typing import Annotated

from fastapi import Depends

from repalis.auth.dependencies import Authenticator
from repalis.auth.models import Agent, AuthSubject, User
from repalis.auth.scope import Scope
from repalis.models.organization import Organization

_DiscountRead = Authenticator(
    required_scopes={
        Scope.discounts_read,
        Scope.discounts_write,
    },
    allowed_subjects={User, Organization, Agent},
)
DiscountRead = Annotated[
    AuthSubject[User | Organization | Agent], Depends(_DiscountRead)
]

_DiscountWrite = Authenticator(
    required_scopes={
        Scope.discounts_write,
    },
    allowed_subjects={User, Organization, Agent},
)
DiscountWrite = Annotated[
    AuthSubject[User | Organization | Agent], Depends(_DiscountWrite)
]
