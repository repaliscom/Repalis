from typing import Annotated

from fastapi import Depends

from repalis.auth.dependencies import Authenticator
from repalis.auth.models import AuthSubject, Organization, User
from repalis.auth.scope import Scope

_SupportCasesRead = Authenticator(
    required_scopes={Scope.organizations_read, Scope.organizations_write},
    allowed_subjects={User, Organization},
)
SupportCasesRead = Annotated[
    AuthSubject[User | Organization], Depends(_SupportCasesRead)
]

_SupportCasesWrite = Authenticator(
    required_scopes={Scope.organizations_write},
    allowed_subjects={User},
)
SupportCasesWrite = Annotated[AuthSubject[User], Depends(_SupportCasesWrite)]
