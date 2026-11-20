from typing import Annotated

from fastapi import Depends

from repalis.auth.dependencies import Authenticator
from repalis.auth.models import AuthSubject, Organization, User
from repalis.auth.scope import Scope

_CLIRead = Authenticator(
    required_scopes={
        Scope.webhooks_read,
        Scope.webhooks_write,
    },
    allowed_subjects={User, Organization},
)
CLIRead = Annotated[AuthSubject[User | Organization], Depends(_CLIRead)]
