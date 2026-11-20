from typing import Annotated

from fastapi import Depends

from repalis.auth.dependencies import Authenticator
from repalis.auth.models import AuthSubject, User
from repalis.auth.scope import Scope
from repalis.models.organization import Organization

_CustomerSessionWrite = Authenticator(
    required_scopes={
        Scope.customer_sessions_write,
    },
    allowed_subjects={User, Organization},
)
CustomerSessionWrite = Annotated[
    AuthSubject[User | Organization], Depends(_CustomerSessionWrite)
]
