from typing import Annotated

from fastapi import Depends

from repalis.auth.dependencies import Authenticator
from repalis.auth.models import AuthSubject, Organization, User
from repalis.auth.scope import Scope

_DisputesRead = Authenticator(
    required_scopes={Scope.disputes_read, Scope.disputes_write},
    allowed_subjects={User, Organization},
)
DisputesRead = Annotated[AuthSubject[User | Organization], Depends(_DisputesRead)]

_DisputesWrite = Authenticator(
    required_scopes={Scope.disputes_write},
    allowed_subjects={User, Organization},
)
DisputesWrite = Annotated[AuthSubject[User | Organization], Depends(_DisputesWrite)]
