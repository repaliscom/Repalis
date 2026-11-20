from typing import Annotated

from fastapi import Depends

from repalis.auth.dependencies import Authenticator
from repalis.auth.models import Agent, AuthSubject, User
from repalis.auth.scope import Scope
from repalis.models.organization import Organization

_CheckoutLinkRead = Authenticator(
    required_scopes={
        Scope.checkout_links_read,
        Scope.checkout_links_write,
    },
    allowed_subjects={User, Organization, Agent},
)
CheckoutLinkRead = Annotated[
    AuthSubject[User | Organization | Agent], Depends(_CheckoutLinkRead)
]

_CheckoutLinkWrite = Authenticator(
    required_scopes={
        Scope.checkout_links_write,
    },
    allowed_subjects={User, Organization, Agent},
)
CheckoutLinkWrite = Annotated[
    AuthSubject[User | Organization | Agent], Depends(_CheckoutLinkWrite)
]
