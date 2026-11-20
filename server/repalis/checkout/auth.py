from typing import Annotated

from fastapi import Depends

from repalis.auth.dependencies import Authenticator
from repalis.auth.models import Agent, Anonymous, AuthSubject, User
from repalis.auth.scope import Scope
from repalis.models.organization import Organization

_CheckoutRead = Authenticator(
    required_scopes={
        Scope.checkouts_read,
        Scope.checkouts_write,
    },
    allowed_subjects={User, Organization, Agent},
)
CheckoutRead = Annotated[
    AuthSubject[User | Organization | Agent], Depends(_CheckoutRead)
]

_CheckoutWrite = Authenticator(
    required_scopes={Scope.checkouts_write},
    allowed_subjects={User, Organization, Agent},
)
CheckoutWrite = Annotated[
    AuthSubject[User | Organization | Agent], Depends(_CheckoutWrite)
]

_CheckoutWeb = Authenticator(
    required_scopes=set(),
    allowed_subjects={User, Anonymous},
)
CheckoutWeb = Annotated[AuthSubject[User | Anonymous], Depends(_CheckoutWeb)]
