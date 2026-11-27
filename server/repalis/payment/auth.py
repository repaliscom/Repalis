from typing import Annotated

from fastapi import Depends

from repalis.auth.dependencies import Authenticator
from repalis.auth.models import AuthSubject, User
from repalis.auth.scope import Scope
from repalis.models.organization import Organization

_PaymentRead = Authenticator(
    required_scopes={
        Scope.payments_read,
    },
    allowed_subjects={User, Organization},
)
PaymentRead = Annotated[AuthSubject[User | Organization], Depends(_PaymentRead)]
